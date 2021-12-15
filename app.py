from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return {
      "data": 'Hello Flask!'
    }

@app.route('/current_datetime', methods=["GET"])
def time():
    get_date = datetime.now()
    date = get_date.strftime('%d/%m/%Y %T %p')
    hour = get_date.strftime('%H')
    hour = int(hour)

    if hour < 12:
        msg = "Bom dia!"
    elif hour < 18:
        msg = "Boa tarde!"
    else:
        msg = "Boa noite!"

    return {
      "current_datetime": date,
      "message": msg
    }