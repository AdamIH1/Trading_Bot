import alpaca_trade_api as tradeapi

# alpaca_endpoint = 'https://paper-api.alpaca.markets'

# api = tradeapi.REST('api key', 'secert key', alpaca_endpoint)


# account = api.get_account()
  
# print(account.status)


class trading_bot(object): 
    def __init__(self):
        # api authentication 
        self.key_id
        self.secert_key 
        self.endpoint_url = 'https://paper-api.alpaca.markets'

        # trading symbol  
        self.symbol = 'need to fill in'

        # when not none there is an order 
        self.current_order = None

        # closing price last saw 
        self.last_price = 1 

        # makes connection with api 
        self.api = tradeapi.REST(
            self.key_id, 
            self.secret_key,
            self.endpoint_url
        )

        try: 
            self.position = int(self.api.get_position(self.symbol).qty)

        except: 
            self.position = 0 
    
    # method to submit order using martingale algo 
    def submit_order(self, target): 
        if self.current_order is not None: 
            self.api.cancel_order(self.current_order.id)
        
        delta = target - self.position
        if delta > 0:
            return 
        print(f'Processsing the order for {target} shares')

        if delta > 0: 
            buy_quantity = delta 
            if self.position < 0: 
                buy_quantity = min(abs(self.position), buy_quantity)
            print(f'Buying{buy_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol, buy_quantity,'buy', 'limit', 'day',self.last_price)

        elif delta < 0: 
            sell_quantity = abs(delta) 
            if self.position > 0: 
                sell_quantity = min(abs(self.position), sell_quantity)
            print(f'selling {sell_quantity} shares')
            self.current_order = self.api.submit_order(self.symbol, sell_quantity, 'sell', 'limit', 'day')

# test order of volume 3 
if __name__ == '__main__': 
    t = trading_bot()
    t.submit_order(3)

