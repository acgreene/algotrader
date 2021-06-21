import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

#webdriver to open Firefox with selenium
geckodriver_path='/Users/Alec Greene/Desktop/Alec/CODING/algotrader/geckodriver'

# Alpaca 
APCA_BASE_URL = "https://paper-api.alpaca.markets"
APCA_ACCOUNT_URL = "{}/v2/account".format(APCA_BASE_URL)
APCA_ORDERS_URL = "{}/v2/orders".format(APCA_BASE_URL)
APCA_POSITIONS_URL = "{}/v2/positions".format(APCA_BASE_URL)
APCA_HEADERS = {'APCA-API-KEY-ID': os.getenv('APCA_API_KEY'), 
                'APCA-API-SECRET-KEY': os.getenv('APCA_SECRET_KEY')}

#TD Ameritrade
TDA_API_KEY = os.getenv('TDA_API_KEY')
TDA_ACCOUNT_ID = os.getenv('TDA_ACCOUNT_ID')
TDA_TOKEN_PATH = 'token'
TDA_REDIRECT_URL = 'https://localhost' #set here since we are running algo on our local computer