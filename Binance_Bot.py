import os
from binance.client import Client

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client(api_key, api_secret)

# Demo Account
client.API_URL = 'https://testnet.binance.vision/api'

# get balances for all assets & some account information
print(client.get_account())
