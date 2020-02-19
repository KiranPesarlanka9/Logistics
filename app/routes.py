from app import app, logging
@app.route('/')
@app.route('/index')
def index():
    logging.info("Test")
    return "Hello, World!"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
