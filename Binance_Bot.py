import os
from binance.client import Client
from time import sleep
from dotenv import dotenv_values, load_dotenv

from binance import ThreadedWebsocketManager

# get API Keys
config=dotenv_values("local.env")

api_key = config["binance_api"]
api_secret = config["binance_secret"]

print(api_key, api_secret)

client = Client(api_key, api_secret)

# Demo Account
client.API_URL = 'https://testnet.binance.vision/api'


print(client.get_asset_balance(asset='BTC'))

# Init bitcoin price variable
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
btc_price = {'error':False}

print(btc_price)

'''
def btc_trade_history(msg):
    #define how to process incoming WebSocket messages 
    if(msg['e'] != 'error'):
        print(msg['c'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
        btc_price['error'] = False
    else:
        btc_price['error'] = True

async def stream():
    # init and start the WebSocket
    bsm = ThreadedWebsocketManager()
    bsm.start()

    # subscribe to a stream
    bsm.start_symbol_ticker_socket(callback=btc_trade_history, symbol='BTCUSDT')
    '''
