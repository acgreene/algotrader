import os
from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

#webdriver to open Firefox with selenium
geckodriver_path = os.getenv('path_to_webdriver')

# Alpaca account info
API_KEY = os.getenv('APCA_API_KEY')
SECRET_KEY = os.getenv('APCA_SECRET_KEY')
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
POSITIONS_URL = "{}/v2/positions".format(BASE_URL)
HEADERS = {'APCA-API-KEY-ID': API_KEY, 
                'APCA-API-SECRET-KEY': SECRET_KEY}

#TD Ameritrade
TDA_API_KEY = os.getenv('TDA_API_KEY')
TDA_ACCOUNT_ID = os.getenv('TDA_ACCOUNT_ID')
TDA_TOKEN_PATH = 'token'
TDA_REDIRECT_URL = 'https://localhost' #set here since we are running algo on our local computer