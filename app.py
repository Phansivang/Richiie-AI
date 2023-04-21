from flask import Flask, render_template, request
from main import Service
from flask_sslify import SSLify
from rate_limit import limit_requests

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template(str('index.html'))


@app.route('/get/respond')
def get_bot_response():
    message = request.args.get('msg')
    return Service().send(message)


@app.route('/v1/message', methods=['GET'])
@limit_requests
def get():
    request_data = request.get_json()
    message = request_data['message']
    return Service().send(message)


if __name__ == "__main__":
    SSLify(app)
    app.run()
