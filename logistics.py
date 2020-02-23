import os
from app import app
from db import load_data, DATABASE_FILE, BOOKINGS_FILE, TinyDB
from app import logging
from flask import Flask, render_template, request

SUCCESS = {"success": True, "message": "Booking Successfully!"}
FAILURE = {"success": False, "message": "Booking Unsuccessfully!"}

if not os.path.exists(DATABASE_FILE):
    logging.info("DATABASE doesn't exists")
    load_data()


booking_db = TinyDB(BOOKINGS_FILE)


logging.info('DATABASE is ready')
@app.route("/")
@app.route('/logistics')
def demo():
    return render_template('index.html')

"""
@app.route("/admin",methods=['GET','POST'])
def admin():
    email = request.form.get('InputEmail')
    password = request.form.get('InputPassword')
    confirm_password = request.form.get('InputConfirmPassword')
    print(str(email))
    print(str(password))
    print(str(confirm_password))
    return "You have signed up!"
"""
@app.route("/submit", methods=['POST'])
def submit():
    booking_db.insert(dict(request.form))
    return render_template('success.html', name=request.form.get('firstName'), date=request.form.get('checkin'))

def get_bookings():
    bookings = booking_db.storage.read()
    return bookings


@app.route('/bookings', methods = ['GET', 'POST'])
def bookings():
    if request.method == 'GET':
        return get_bookings()
    if request.method == 'POST':
        return create_booking(request.json)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

