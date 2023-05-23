import json
import os

from flask import Flask, render_template, request

app = Flask(__name__)

WEBHOOK_DATA: dict = {}


@app.route("/")
def index():
    return render_template('index.html', data=WEBHOOK_DATA)


@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    global WEBHOOK_DATA
    if request.method == 'POST':
        try:
            WEBHOOK_DATA = request.json
            data = {"status": "success"}
            return data, 200
        except Exception:
            bytes_value = request.data
            decode_json = bytes_value.decode('utf8').replace("'", '"')
            data = {"status": "success"}
            WEBHOOK_DATA = json.loads(decode_json)
            return data, 200
    if request.method == 'GET':
        return WEBHOOK_DATA


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
