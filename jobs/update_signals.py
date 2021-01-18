import yfinance as yf
import time
from app.postgres import fetch_tickers
from app.postgres import insert_or_update_signal_result
from signals.PA1 import PA1

'''
	Job which performs the following actions:
	1. Grab all supported tickers
	2. Iterate over supported tickers
	3. Resolve ticker (update signal results)
'''
def run_job():
	print("==> Running signal update job...")
	tickers = fetch_tickers()
	for ticker in tickers:
		resolve_ticker(ticker[0])

def resolve_ticker(ticker):
	print("==> Evaluating ticker: {}".format(ticker))
	yf_ticker = yf.Ticker(ticker)
	pa1 = PA1()
	print("==> Ticker data fetched: {}".format(ticker))
	result = pa1.evaluate(yf_ticker.history(period="max"))
	success = insert_or_update_signal_result(ticker, pa1.name, result)
	if not success:
		print("==> Failed to update result for ticker: {}".format(ticker))
	else:
		print("==> Result updated for ticker: {}, {}".format(ticker, result))

if __name__ == "__main__":
	run_job()