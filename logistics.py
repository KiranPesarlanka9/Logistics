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
#@app.route("/")
@app.route('/logistics')
def demo():
    return render_template('index.html')

@app.route("/test")
def hello():
    #return render_template('echo.html')
    return render_template('login.html')

@app.route("/echo", methods=['POST'])
def echo():
    return render_template('echo.html', text=request.form['text'])

@app.route("/signup",methods=['GET','POST'])
def signup():
    email = request.form.get('InputEmail')
    password = request.form.get('InputPassword')
    confirm_password = request.form.get('InputConfirmPassword')
    print(str(email))
    print(str(password))
    print(str(confirm_password))
    return "You have signed up!"

@app.route("/submit", methods=['POST'])
def submit():
    return render_template('success.html')





def get_bookings():
    bookings = booking_db.storage.read()
    return bookings

def get_tarif(start, end):

    #calculate tarif
    if end-start <= 10:
        tarif = 51
    elif end-start <= 20:
        tarif = 74.90
    elif end-start <= 30:
        tarif = 79.40
    elif end-start <= 40:
        tarif = 85.20
    else:
        tarif = 0
    return tarif

def create_booking(data):


    if not data:
        return FAILURE
    else:
        #dump the data into DB
        _from = data.get('from', '')
        _to = data.get('to', '')
        start = data.get('start', 0)
        end = data.get('end', 0)
        _type = data.get('type', 'classic')
        tarif = get_tarif(start, end)
        if not tarif:
            SUCCESS["message"] = "Please contact Admin!! If you are making booking more than 3 days"
            return SUCCESS

        booking_db.insert({"from": _from, "to": _from, "start": start, "end": end, "_type": _type, "tarif": tarif})
        return SUCCESS


@app.route('/bookings', methods = ['GET', 'POST'])
def bookings():
    if request.method == 'GET':
        return get_bookings()
    if request.method == 'POST':
        return create_booking(request.json)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

