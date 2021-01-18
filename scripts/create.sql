CREATE TABLE tickers(
	symbol TEXT PRIMARY KEY 
);

CREATE TABLE signals(
	signal_name TEXT PRIMARY KEY
);

CREATE TABLE signal_results(
	symbol TEXT NOT NULL,
	signal_name TEXT NOT NULL,
	result BOOLEAN NOT NULL,
	PRIMARY KEY(symbol, signal_name)
);

INSERT INTO tickers VALUES('TQQQ');
INSERT INTO tickers VALUES('VXX');
INSERT INTO tickers VALUES('UVXY');
INSERT INTO tickers VALUES('SPXS');
INSERT INTO tickers VALUES('SOXL');
INSERT INTO tickers VALUES('FAS');
INSERT INTO tickers VALUES('TECL');
INSERT INTO tickers VALUES('TNA');
INSERT INTO tickers VALUES('NUGT');