from itertools import islice

class PA1:

	def __init__(self):
		self.name = "PA1"

	def evaluate_historical(self, candles):
		results = []
		starting_index = 2
		index = 2
		for ts, row in islice(candles.iterrows(), starting_index, None):
			subset = candles.iloc[[index-2,index-1]]
			result = self.evaluate(subset)
			results.append([str(ts), str(result)])
			index = index + 1
		return results

	def evaluate(self, candles):
		yesterday = candles.iloc[[-1]]
		two_days_ago = candles.iloc[[-2]]
		return  self.evaluate_first(yesterday, two_days_ago) or \
				self.evaluate_second(yesterday) or \
				self.evaluate_third(yesterday, two_days_ago) or \
				self.evaluate_fourth(yesterday, two_days_ago) or \
				self.evaluate_fifth(yesterday) or \
				self.evaluate_sixth(yesterday)

	def evaluate_first(self, yesterday, two_days_ago):
		return yesterday['Close'][0] > (two_days_ago['Open'][0] * 1.1)

	def evaluate_second(self, yesterday):
		return yesterday['Close'][0] > (yesterday['Low'][0] * 1.08)

	def evaluate_third(self, yesterday, two_days_ago):
		return yesterday['Close'][0] > (two_days_ago['Close'][0] * 1.08)

	def evaluate_fourth(self, yesterday, two_days_ago):
		return yesterday['Close'][0] > (two_days_ago['Open'][0] * 1.1)

	def evaluate_fifth(self, yesterday):
		return yesterday['Close'][0] > yesterday['Open'][0] and yesterday['Close'][0] < (yesterday['High'][0] * .97)

	def evaluate_sixth(self, yesterday):
		return yesterday['Close'][0] > yesterday['Open'][0] and yesterday['High'][0] > (yesterday['Open'][0] * 1.05)
