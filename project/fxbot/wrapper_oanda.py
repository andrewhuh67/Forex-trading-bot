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

def main():
	api = OandaAPI()

	accounts = api.list_accounts()

	print(accounts)

if __name__ == '__main__':
	main()


