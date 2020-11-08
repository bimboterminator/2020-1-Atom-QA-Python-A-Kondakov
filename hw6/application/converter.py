import threading
import requests
import json
from flask import Flask, request, jsonify
import settings

app = Flask(__name__)


def run_app():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.APP_HOST,
        'port': settings.APP_PORT
    })

    server.start()
    return server


# Добавляем точку завершения приложения, чтобы мы могли его при необходимостм правильно закрыть
def shutdown_app():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_app()
    return 'OK'


@app.route('/send', methods=['POST'])
def index():
    transaction = request.get_json()
    from_curr = transaction['emitent_curr']
    to_curr = transaction['reciever_curr']
    amount = transaction['amount']
    # конвертация
    if from_curr != to_curr:
        data = requests.get(settings.USD_URL).json()
        currencies = data['rates']
        if from_curr != 'USD':
            amount = amount / currencies[from_curr]
        amount = round(amount * currencies[to_curr], 4)
    transaction['amount'] = amount

    if to_curr == 'USD':
        mock_response = requests.post(settings.MOCK_USD_URL, json.dumps(transaction))
        if mock_response.status_code == 200:
            return jsonify({'status': 'ok', 'transaction': transaction}), 200
    if to_curr == 'EUR':
        mock_response = requests.post(settings.MOCK_EUR_URL, json.dumps(transaction))
        if mock_response.status_code == 200:
            return jsonify({'status': 'ok', 'transaction': transaction}), 200
    if to_curr != 'USD' and to_curr != 'EUR':
        return jsonify({'status': 'wrong reciever currency'}), 400


@app.route('/history', methods=['GET'])
def hist():
    response = requests.get(settings.MOCK_GET_URL, headers=request.headers)
    if response.status_code == 403:
        return jsonify('Wrong username'), 403
    elif response.status_code == 200:
        return response.json(), 200
    elif response.status_code == 400:
        return jsonify('No auth header'), 400

@app.route('/mockdown')
def mock_is_down():
    try:
         requests.get(f'http://{settings.MOCK_HOST}:1054', timeout=0.5)
    except requests.exceptions.ConnectionError:
        return jsonify('Mock is down'), 500

@app.route('/timeout')
def mock_timeout():
    try:
         requests.get(settings.MOCK_TIME, timeout=0.5)

    except requests.exceptions.ReadTimeout:
        return jsonify('Timeout error'), 408

@app.route('/bank')
def mock_error():
    response = requests.get(settings.MOCK_ERROR)
    if response.status_code == 500:
        return jsonify('Internal server error') ,500


if __name__ == '__main__':
    run_app()
