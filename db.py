from os import path
from tinydb import TinyDB
from app import logging


DATABASE_FILE = "SiteDatabase.json"
BOOKINGS_FILE = "Bookings.json"

TRUCKS = [
        {"type": "small", "meta": "6 M3", "length": "2 m", "capacity": 800, "available": 10},
        {"type": "classic", "meta": "9 M3", "length": "2.5 m", "capacity": 1200, "available": 10},
        {"type": "large", "meta": "12 M3", "length": "3 m", "capacity": 1400, "available": 10},
        {"type": "jumbo", "meta": "20 M3", "length": "4 m", "capacity": 1700, "available": 10}
    ]

def create_database():
    logging.info('Creating Database..')
    return TinyDB(DATABASE_FILE)

def load_data():
    db = create_database()
    logging.info('-------------------')
    logging.info('Created Database..')
    logging.info('Loading Trucks data to Database')
    db.insert_multiple(TRUCKS)
    logging.info('Loading is done')
