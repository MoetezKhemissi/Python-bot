from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import datetime

def fun(): 
    pass
client = Client('IasFiam7yUQneiVx1djOnUdz1vK4rKBlOobk6BkJFX762izFx9r3XBS2lUJT89F0','AU7lwvqsM10iE9BmQcJkU20fiI9ZQK8nhRidAsuNAeiBUjOxjBjiS55LuWp1VGG0',testnet=True)
# Pinging two simultaneous pings to see time difference
time1 =client.get_server_time()["serverTime"]
time2 =client.get_server_time()["serverTime"]
time3 = time2-time1
# Convert Posix TimeStamp to time
print(time3,"MS")
fun()