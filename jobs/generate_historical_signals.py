import yfinance as yf
import time
from app.postgres import fetch_tickers
from app.postgres import fetch_signals
from app.postgres import insert_or_update_signal_result
from signals.PA1 import PA1

'''
	Job which performs the following actions:
	1. Grab all supported tickers and symbols
	2. Generate historical reports for all combinations
'''
def run_job():
	print("==> Running generate historical signals job...")
	tickers = fetch_tickers()
	signals = fetch_signals()
	for ticker in tickers:
		for signal in signals:
			generate_results(ticker[0], signal[0])

def generate_results(ticker, signal):
	print("==> Evaluating ticker / signal: {} / {}".format(ticker, signal))
	yf_ticker = yf.Ticker(ticker)
	signal_obj = get_signal_from_name(signal)

	print("==> Ticker data fetched: {}".format(ticker))
	result = signal_obj.evaluate_historical(yf_ticker.history(period="max"))

	if not None:
		print("==> Report generated for: {} / {}".format(ticker, signal))
		return result
	else:
		print("==> Failed to generate report for: {} / {}".format(ticker, signal))
		return None

def get_signal_from_name(signal):
	if signal == "PA1":
		return PA1()
	else:
		return None

if __name__ == "__main__":
	run_job()