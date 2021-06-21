# check out esignal for market data
# tda-api documentation: https://tda-api.readthedocs.io/en/stable/

from config import *
from selenium import webdriver
from tda import auth, client, orders
import datetime, json, requests, dotenv

# authenticate
try:
    # Once you have a token written on disk, you can reuse it without going 
    # through the login flow again.
    c = auth.client_from_token_file(TDA_TOKEN_PATH, TDA_API_KEY)
except FileNotFoundError:
    # Be sure to have the correct webdriver installed
    with webdriver.Firefox(executable_path=geckodriver_path) as driver:
        # Uses the webdriver to perform an OAuth webapp login flow and creates 
        # a client wrapped around the resulting token. The client will be 
        # configured to refresh the token as necessary, writing each updated 
        # version to token_path.
        c = auth.client_from_login_flow(
            driver, TDA_API_KEY, TDA_REDIRECT_URL, TDA_TOKEN_PATH)

