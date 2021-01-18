import os
from urllib.parse import urlparse

class Environment:
	def __init__(self):
		self.database_url = urlparse(os.environ.get("DATABASE_URL"))
		self.creds = {
			'host': self.database_url.hostname,
			'db':   self.database_url.path[1:],
			'usr':  self.database_url.username,
			'pswd': self.database_url.password
		}
