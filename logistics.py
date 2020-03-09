import os
from app import app
from app import logging

from deeputil import *
from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth


from mailing import send_mail
from db import load_data, DATABASE_FILE, BOOKINGS_FILE, TinyDB
SUCCESS = {"success": True, "message": "Booking Successfully!"}
FAILURE = {"success": False, "message": "Booking Unsuccessfully!"}
USER_DATA = {"admin": "admin123"}

resp_mail_html = open('templates/mail.html')
lines = resp_mail_html.readlines()
MAIL_CONTENT = ' '.join(lines)

admin_mail_html = open('templates/admin_mail.html')
ADMIN_MAIL_CONTENT = ' '.join(admin_mail_html.readlines())
if not os.path.exists(DATABASE_FILE):
    logging.info("DATABASE doesn't exists")
    load_data()

booking_db = TinyDB(BOOKINGS_FILE)
logging.info('DATABASE is ready')

auth = HTTPBasicAuth()

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

@app.route("/")
@app.route('/logistics')
def demo():
    return render_template('index.html')

@app.route("/submit", methods=['POST'])
def submit():
    data = dict(request.form)
    email =  data.get('email', '')
    booking_id = generate_random_string(length=24)
    data["booking_id"] = booking_id
    customer_mail_content = MAIL_CONTENT.format(name=data.get('firstName'), date=data.get('checkin'), booking_id=booking_id)
    send_mail(customer_mail_content, "Your Booking is confirmed", data.get('email', ''))
    admin_mail_content = ADMIN_MAIL_CONTENT.format(arrival=data.get('arrival', ''), title=data.get('Booking from '+data.get('firstName', '')),
                                                    departure=data.get('departure', ''),
                                                    checkin=data.get('checkin', ''),
                                                    time=data.get('time', ''),
                                                    test=data.get('test', ''),
                                                    firstName=data.get('firstName', ''),
                                                    mobile=data.get('mobile', ''),
                                                    email=data.get('email', '')
                                                    )
    send_mail(admin_mail_content, "New Booking !!", 'anilkumarsannamuri@gmail.com')
    booking_db.insert(data)
    return render_template('success.html', name=request.form.get('firstName'), date=request.form.get('checkin'))

def get_bookings():
    bookings = booking_db.storage.read()
    final_string = []
    for booking in bookings['_default']:
        data = bookings['_default'][booking]
        final_string.append(ADMIN_MAIL_CONTENT.format(arrival=data.get('arrival', ''), title="Booking No. "+ str(booking),
                                                    departure=data.get('departure', ''),
                                                    checkin=data.get('checkin', ''),
                                                    time=data.get('time', ''),
                                                    test=data.get('test', ''),
                                                    firstName=data.get('firstName', ''),
                                                    mobile=data.get('mobile', ''),
                                                    email=data.get('email', '')
                                                    ))
        final_string.append('</br>')


    return ''.join(final_string)

@app.route('/bookings', methods = ['GET', 'POST'])
@auth.login_required
def bookings():
    if request.method == 'GET':
        return get_bookings()
    #if request.method == 'POST':
    #    return create_booking(request.json)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
