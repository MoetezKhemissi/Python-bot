

def find_stablecoin_selling_symbol_for_currency(SymbolPairsData,client,currency):
#TODO lazy logic find logic that takes into account type of coin took usd usdt usdb as bases
    SymbolPairsData = client.get_exchange_info()["symbols"]
    for symbolPair in SymbolPairsData:
        symbol=symbolPair["symbol"]
        base =symbolPair["baseAsset"]
        quote =symbolPair["quoteAsset"]
        if(base== currency and (quote=="USD"or quote=="USDT" or quote=="BUSD")):
            return symbol
            
    

def value_currency(client,SymbolPairsData,currency,quantity):
#TODO minus liquidation premium(how much liquidity to sell)
#TODO lazy logic find logic that takes into account type of coin took usd usdt usdb as bases
    if(currency=="BUSD" or currency=="USDT" or currency == "USD"):
        return quantity
    return quantity*float(client.get_avg_price(symbol=find_stablecoin_selling_symbol_for_currency(SymbolPairsData,client,currency))["price"])

#print(value_currency("BTC",1.5))
def Print_Account_Value(client):
    info = client.get_account()
    total_value=0
    SymbolPairsData = client.get_exchange_info()["symbols"]
    for balance in info["balances"]:
        #TODO ASYNCHRONOUS IMPLEMENTATION (load currencies -> async call for avg price -> add and show)
        Current_value=value_currency(client,SymbolPairsData,balance["asset"],float(balance["free"]))
        total_value=total_value+Current_value
        print("Currency :", balance["asset"],"Value:",Current_value)

    print("TOTAL VALUE IS :",total_value)
    return total_value