from client import FtxClient
import os
import time
import sys

          
#common function to call api for all coins 
def executeaccount(arg1, arg2, arg3, pub, sec, phrase, cp, account, tradetype):

    api_key = pub
    api_secret = sec
    api_passphrase = phrase
    subaccount_name = account    
    #print('api_key: ', api_key)
    #print('api_secret: ', api_secret)
    #print('api_passphrase: ', api_passphrase)
    #print('subaccount_name: ', subaccount_name) 
    #print('//--------------------------')
    

    #client = FtxClient(api_key,api_secret)
    clientsub = FtxClient(api_key,api_secret,subaccount_name)

    sourc = phrase
    destinatio = cp         
    #print('market: ', cp, 'cp') 
    #print('side: ', arg1, 'arg1') 
    #print('price: ', arg2, 'arg2') 
    #print('size: ', arg3, 'arg3') 
    #print('type: ', tradetype, 'type') 
    #print('//--------------------------')
    
    
          
    try:               
      if arg1 == 'buy':        
        result = clientsub.place_order(market=cp, side=arg1, price=arg2, size=arg3, type=tradetype)   #   
      if arg1 == 'sell':  
        result = clientsub.place_order(market=cp, side=arg1, price=arg2, size=arg3, type=tradetype)   # 
      if arg1 == 'check':
        result = clientsub.get_order_status(arg2)  #
      if arg1 == 'getorders':      
        result = clientsub.get_open_orders(market=cp)         #
      if arg1 == 'getpositions':
        result = clientsub.get_positions()         #        
      if arg1 == 'cancel':
        result = clientsub.cancel_order(arg2)                #
      if arg1 == 'accounts':
        result = clientsub.get_balances()      #    
      if arg1 == 'ticker':
        result = clientsub.get_orderbook(market=destinatio) #     
      if arg1 == 'modify':
        result = clientsub.modify_order(existing_order_id=arg3, price=arg2) #
      if arg1 == 'subaccounts':
        result = clientsub.get_balances()    #  
      if arg1 == 'transfer':
        result = clientsub.transfer_fund(coin='USDT', size=arg2, source=sourc, destination=destinatio)        #
      if arg1 == 'spotmargin':
        print(subaccount_name)
        result = clientsub.spot_margin(market=subaccount_name) #             
      if arg1 == 'borrow_history':
        result = clientsub.borrow_history()    #  
      print(result)
    except:
      print('error', arg1)     
      

      
      
if __name__ == "__main__":
    arg1 = sys.argv[1] #action
    arg2 = sys.argv[2] #price    || #orderid
    arg3 = sys.argv[3] #qty
    pub = sys.argv[4] #pub
    sec = sys.argv[5] #sec
    phrase = sys.argv[6] #phrase
    coinpair = sys.argv[7] #coinpair   
    account = sys.argv[8] #account
    tradetype = sys.argv[9] #tradetype
    
    #print('sys.argv[1]: ', sys.argv[1])
    #print('sys.argv[2]: ', sys.argv[2])
    #print('sys.argv[3]: ', sys.argv[3])
    #print('sys.argv[4]: ', sys.argv[4])
    #print('sys.argv[5]: ', sys.argv[5])
    #print('sys.argv[6]: ', sys.argv[6])
    #print('sys.argv[7]: ', sys.argv[7])
    #print('sys.argv[8]: ', sys.argv[8])
    #print('sys.argv[9]: ', sys.argv[9]) 
    #print('//--------------------------')

    executeaccount(arg1, arg2, arg3, pub, sec, phrase, coinpair, account, tradetype)      
    

    
    """
                
from client import FtxClient, FtxWebsocketClient
YOUR_API_KEY = 'YOUR_API_KEY' 
YOUR_API_SECRET = 'YOUR_API_SECRET'

# Initialise a new client called 'rest'
rest = FtxClient(api_key=YOUR_API_KEY,api_secret=YOUR_API_SECRET)

# Mention the market of interest
market_name = 'ETH/USDT' # Bitcoin Cash Perpetual Futures

# Get orderbook for that market
rest_orderbook = rest.get_orderbook(market_name)

# Initialise a new client called 'socket'
socket = FtxWebsocketClient()

# Get orderbook for that market
socket_orderbook = socket.get_orderbook(market_name)

# Prints the orderbook on REST and on Socket 
print(f'Order book on REST\n{rest_orderbook}')
print(f'Order book on Socket\n{socket_orderbook}') 
lf = rest.list_futures()
#print(f'list_futures\n{lf}')

# Places market order
try:
    rest.place_order(market=market_name,
                     side="buy",
                     size=0.01,
                     type='market')
except:
    print('Something went wrong while placing the order')
    
input('Press Any Key To Exit')
"""
