import time

from binance import ThreadedWebsocketManager
#TODO fix the stream to get real time data
api_key = 'IasFiam7yUQneiVx1djOnUdz1vK4rKBlOobk6BkJFX762izFx9r3XBS2lUJT89F0'
api_secret = 'AU7lwvqsM10iE9BmQcJkU20fiI9ZQK8nhRidAsuNAeiBUjOxjBjiS55LuWp1VGG0'

def main():

    symbol = 'BNBBTC'

    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    # start is required to initialise its internal loop
    twm.start()

    def handle_socket_message(msg):
        print(f"message type: {msg['e']}")
        print(msg)

    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)

    # multiple sockets can be started
    twm.start_depth_socket(callback=handle_socket_message, symbol=symbol)

    # or a multiplex socket can be started like this
    # see Binance docs for stream names
    streams = ['bnbbtc@kline_1s', 'bnbbtc@bookTicker']
    twm.start_multiplex_socket(callback=handle_socket_message, streams=streams)

    twm.join()


if __name__ == "__main__":
   main()