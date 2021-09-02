import alpaca_trade_api as tradeapi

alpaca_endpoint = 'https://paper-api.alpaca.markets'

api = tradeapi.REST('api key', 'secert key', alpaca_endpoint)


account = api.get_account()
  
print(account.status)