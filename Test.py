from binance.spot import Spot 
from binance.spot import Spot as Client
client = Spot()

# Get server timestamp
print(client.time())
# Get klines of BTCUSDT at 1m interval
#print(client.klines("BTCUSDT", "1m"))
# Get last 10 klines of BNBUSDT at 1h interval
#print(client.klines("BNBUSDT", "1h", limit=10))

# api key/secret are required for user data endpoints
client = Spot(key='IasFiam7yUQneiVx1djOnUdz1vK4rKBlOobk6BkJFX762izFx9r3XBS2lUJT89F0', secret='AU7lwvqsM10iE9BmQcJkU20fiI9ZQK8nhRidAsuNAeiBUjOxjBjiS55LuWp1VGG0',base_url='https://testnet.binance.vision')

# Get account and balance information

print(client.account())