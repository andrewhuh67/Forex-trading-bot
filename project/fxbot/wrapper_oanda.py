import json, hmac, hashlib, time, requests, base64
from requests.auth import AuthBase

from credentials import CredentialsOanda

credentials = CredentialsOanda()

token = credentials.token_key()

class OandaApiAuth(AuthBase):
	def __init__(self, token):
		self.token = token
		

	def __call__(self, request):

		request.headers.update(
			{'Authorization': 'Bearer {}'.format(token),
			'Content-Type':'application/json'}
		)
		return request

practice_url = 'https://api-fxpractice.oanda.com'
realtime_url = 'https://api-fxtrade.oanda.com/'

class OandaAPI():

	def authenticate(self):
		auth = OandaApiAuth(token)
		return auth

	def list_accounts(self):
		auth = self.authenticate()

		r = requests.get(realtime_url + 'v3/accounts', auth=auth)

		return r.json()

	def get_candles(self, trading_pair):
		auth = self.authenticate()

		r = requests.get(realtime_url + 'v3/instruments/' + trading_pair + '/candles' + '?granularity=D' , auth=auth)

		return r.json()

class TradingTest():

	def __init__(self, lot_size, starting_balance):
		self.lot_size = lot_size
		self.starting_balance = starting_balance

	def test(self):
		api = OandaAPI()
		trading_pair = 'EUR_USD'
		candles = api.get_candles(trading_pair)['candles']

		for item in range(0, len(candles)-1):
			candle1 = item - 2
			candle2 = item - 1
			two_candles_ago = candles[candle1]['mid']
			last_candle = candles[candle2]['mid']
			current_candle = candles[item]['mid']

			if float(two_candles_ago['c']) > float(two_candles_ago['c']) > float(current_candle['c'])and float(last_candle['c'] > float(last_candle['c']))
				sell(self.lot_size, current_candle)
			print(two_candles_ago)
			print(last_candle)
			print(current_candle)
			print("-------------------------------------------------")

	def buy(lot_size, price):



def main():
	api = OandaAPI()

	trading_pair = 'EUR_USD'

	accounts = api.list_accounts()

	candles = api.get_candles(trading_pair)

	# print(candles['candles'][0], len(candles['candles']))

	# for item in range(0, len(candles['candles'])-1):
	# 	print(candles['candles'][item])

	test = TradingTest(.01, 1000)

	print(test.test())



if __name__ == '__main__':
	main()


