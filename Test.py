from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import pandas as pd
import Utils.Utils as util
# Get klines of BTCUSDT at 1m interval
#print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
#print(client.klines("BNBUSDT", "1h", limit=10))

# api key/secret are required for user data endpoints
client = Client('IasFiam7yUQneiVx1djOnUdz1vK4rKBlOobk6BkJFX762izFx9r3XBS2lUJT89F0','AU7lwvqsM10iE9BmQcJkU20fiI9ZQK8nhRidAsuNAeiBUjOxjBjiS55LuWp1VGG0',testnet=True)

# Get account and balance information
# print(client.get_avg_price(symbol='BNBBTC'))

#get data for certain symbol
#print(client.get_symbol_info('BNBBTC'))
#get data of account
#info = client.get_account()
#print(info)
#order = client.order_market_buy(
#    symbol='USDTBTC',
#    quantity=100)
#info2 = client.get_account()
#print(info)
# get pairs
print(util.Print_Account_Value(client))
#get all pairs
#print(client.get_recent_trades(symbol='BNBBTC'))
#info = client.get_account()
#for currency in info["balances"]:
#    print(currency["asset"],"/Prices:",currency["free"])

#print(client.get_avg_price(symbol='BNBUSD'))