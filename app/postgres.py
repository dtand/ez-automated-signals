import psycopg2
from app.environment import Environment

ENVIRONMENT = Environment()
creds = ENVIRONMENT.creds

def fetch_tickers():
	try:
		conn = psycopg2.connect(host=creds['host'], database=creds['db'], user=creds['usr'], password=creds['pswd'])
		cur = conn.cursor()
		cur.execute("SELECT symbol from tickers")
		tickers = cur.fetchall()
		conn.commit()
		cur.close()
		conn.close()
		return tickers
	except Exception as e:
		print(e)
	return None

def fetch_signal_results():
	try:
		conn = psycopg2.connect(host=creds['host'], database=creds['db'], user=creds['usr'], password=creds['pswd'])
		cur = conn.cursor()
		cur.execute("SELECT * FROM signal_results")
		signal_results = cur.fetchall()
		conn.commit()
		cur.close()
		conn.close()
		return signal_results
	except Exception as e:
		print(e)
	return None

def fetch_signals():
	try:
		conn = psycopg2.connect(host=creds['host'], database=creds['db'], user=creds['usr'], password=creds['pswd'])
		cur = conn.cursor()
		cur.execute("SELECT * FROM signals")
		signals = cur.fetchall()
		conn.commit()
		cur.close()
		conn.close()
		return signals
	except Exception as e:
		print(e)
	return None

def insert_or_update_signal_result(signal, signal_name, result):
	query = "INSERT INTO signal_results VALUES('{}','{}',{}) ON CONFLICT (symbol, signal_name) DO UPDATE SET result={}"
	try:
		conn = psycopg2.connect(host=creds['host'], database=creds['db'], user=creds['usr'], password=creds['pswd'])
		cur = conn.cursor()
		cur.execute(query.format(signal, signal_name, result, result))
		conn.commit()
		cur.close()
		conn.close()
		return True
	except Exception as e:
		print(e)
	return False

def add_ticker(signal_name):
	query = "INSERT INTO signals VALUES('{}')"
	try:
		conn = psycopg2.connect(host=creds['host'], database=creds['db'], user=creds['usr'], password=creds['pswd'])
		cur = conn.cursor()
		cur.execute(query.format(signal_name))
		conn.commit()
		cur.close()
		conn.close()
		return True
	except Exception as e:
		print(e)
	return False
