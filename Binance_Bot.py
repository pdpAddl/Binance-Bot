import os
from binance.client import Client

# init
api_key = os.environ.get('binance_api')
api_secret = os.environ.get('binance_secret')

client = Client("kXGSgmxSbYqY5G1OgeU1ypaZ2yebh8FXH9i73aLttMATci9YHy48FPNi1VghVBYt", "xW79WjCMIZqxeKP13z9yZRUSAxViqbejlclbNVdk3wSSZprbK8Uv4jbR9j4DhVG8")

print(client)

# Demo Account
client.API_URL = 'https://testnet.binance.vision/api'

# get balances for all assets & some account information
print(client.get_asset_balance(asset='BTC'))
