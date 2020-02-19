from flask import Flask
app = Flask(__name__, template_folder='../templates', static_folder="static")

import logging

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG)
