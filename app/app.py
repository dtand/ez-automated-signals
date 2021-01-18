from flask import Flask, request
from flask_restful import Resource, Api
from flask import render_template
from app.postgres import fetch_signal_results
from jobs.generate_historical_signals import generate_results
import json

## Main app object
app = Flask(__name__)

'''
    Renders main template parameters and points to index.html
'''
@app.route('/')
def index():
    return render_template('index.html', "Hello World")

'''
    Fetches all current signals for all tickers and signals
'''
@app.route('/v1/signal-results', methods = ['GET'])
def get_signal_results():
    signal_results = fetch_signal_results()
    format_param = request.args.get('format')
    if format_param is not None and format_param == 'csv':
        return results_as_csv(signal_results)
    else:
        print(signal_results)
        return json.dumps(results_as_json_array(signal_results))

def results_as_json_array(signal_results):
    json_array = []
    for result in signal_results:
        json_result = {
            'symbol': result[0],
            'signal': result[1],
            'result': result[2]
        }
        json_array.append(json_result)
    return json_array

def results_as_csv(signal_results):
    csv_result = "SYMBOL, SIGNAL, RESULT<br/>"
    for result in signal_results:
        csv_result = csv_result + "{},{},{}<br/>".format(result[0],result[1],result[2])
    return csv_result

'''
    Fetches hisotrical results for specified ticker and signal
'''
@app.route('/v1/historical/signal-results', methods = ['GET'])
def get_historical_signal_results():
    ticker_param = request.args.get('ticker')
    signal_param = request.args.get('signal')
    if ticker_param is None or signal_param is None:
        return "ERR: ticker or signal not provided"
    results = generate_results(ticker_param, signal_param)
    csv_result = "TIMESTAMP,RESULT<br/>"
    for result in results:
        csv_result = (csv_result + ','.join(result)) + '<br/>'
    return csv_result



