from app import app, logging
@app.route('/')
@app.route('/index')
def index():
    logging.info("Test")
    return "Hello, World!"
