from flask import Flask
import os
app = Flask(__name__)


env = os.environ.get("ENV")  # Will return "prod"

@app.route('/')
def home():
    return "Hello from Flask Microservice!"

@app.route("/env")
def show_env():
    return f"ENV: {os.getenv('ENV')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
