from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import datetime
import unittest
class TestLatency(unittest.TestCase):
    def test_ping(self): 
        client = Client('IasFiam7yUQneiVx1djOnUdz1vK4rKBlOobk6BkJFX762izFx9r3XBS2lUJT89F0','AU7lwvqsM10iE9BmQcJkU20fiI9ZQK8nhRidAsuNAeiBUjOxjBjiS55LuWp1VGG0',testnet=True)
        # Pinging two simultaneous pings to see time difference
        time1 =client.get_server_time()["serverTime"]
        time2 =client.get_server_time()["serverTime"]
        time3 = time2-time1
        self.assertTrue(time3<5000,"Good ping")
    def test_ping2(self): 
        client2 = Client('IasFiam7yUQneiVx1djOnUdz1vK4rKBlOobk6BkJFX762izFx9r3XBS2lUJT89F0','AU7lwvqsM10iE9BmQcJkU20fiI9ZQK8nhRidAsuNAeiBUjOxjBjiS55LuWp1VGG0',testnet=True)
        # Pinging two simultaneous pings to see time difference
        time1 =client2.get_server_time()["serverTime"]
        time2 =client2.get_server_time()["serverTime"]
        time3 = time2-time1
        self.assertTrue(time3<5000,"Good ping")