import os
from app import app
from app import logging

from flask import Flask, render_template, request
from flask_httpauth import HTTPBasicAuth

from db import load_data, DATABASE_FILE, BOOKINGS_FILE, TinyDB

SUCCESS = {"success": True, "message": "Booking Successfully!"}
FAILURE = {"success": False, "message": "Booking Unsuccessfully!"}
USER_DATA = {"admin": "admin123"}

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
    booking_db.insert(dict(request.form))
    return render_template('success.html', name=request.form.get('firstName'), date=request.form.get('checkin'))

def get_bookings():
    bookings = booking_db.storage.read()
    return bookings

@app.route('/bookings', methods = ['GET', 'POST'])
@auth.login_required
def bookings():
    if request.method == 'GET':
        return get_bookings()
    if request.method == 'POST':
        return create_booking(request.json)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
