import threading
import requests
import json
from flask import Flask, request, jsonify


app = Flask(__name__)

DATA = []
CURR = {"base":"USD","date":"2020-11-15","time_last_updated":1605398651,"rates":{"USD":1,"AED":3.672032,"ARS":79.561975,"AUD":1.378187,"BGN":1.654831,"BRL":5.45975,"BSD":1,"CAD":1.313596,"CHF":0.913796,"CLP":759.667436,"CNY":6.608396,"COP":3606.809524,"CZK":22.402988,"DKK":6.301689,"DOP":57.907492,"EGP":15.60103,"EUR":0.845766,"FJD":2.103914,"GBP":0.759027,"GTQ":7.766123,"HKD":7.753283,"HRK":6.406894,"HUF":300.815658,"IDR":14294.656641,"ILS":3.367301,"INR":74.614091,"ISK":136.980851,"JPY":104.836813,"KRW":1110.735282,"KZT":427.926554,"MVR":15.42,"MXN":20.481873,"MYR":4.123826,"NOK":9.14893,"NZD":1.462498,"PAB":1,"PEN":3.640715,"PHP":48.24212,"PKR":157.469854,"PLN":3.799777,"PYG":6885.727273,"RON":4.120417,"RUB":77.420149,"SAR":3.750579,"SEK":8.67495,"SGD":1.348415,"THB":30.175487,"TRY":7.677017,"TWD":28.499165,"UAH":28.072019,"UYU":42.720248,"ZAR":15.565851}}


@app.route('/')
def index():
    return "HELLO WORLD!!!"

@app.route('/send', methods=['POST'])
def convert():
    transaction = request.get_json()
    from_curr = transaction['emitent_curr']
    to_curr = transaction['reciever_curr']
    amount = transaction['amount']
    # конвертация
    if from_curr != to_curr:
        data = CURR
        currencies = data['rates']
        if from_curr != 'USD':
            amount = amount / currencies[from_curr]
        amount = round(amount * currencies[to_curr], 4)
    transaction['amount'] = amount
    DATA.append(transaction)
    return jsonify('Everything is ok'), 200


@app.route('/hist', methods=['GET'])
def hist():
    return jsonify({'transactions': DATA}), 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5555)
