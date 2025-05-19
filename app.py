from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask Microservice!"


@app.route('/getdata')
def home1():
    return "Hello from Flask Microservice for get data!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
