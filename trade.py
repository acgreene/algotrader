# check out esignal for market data
# ninjatrader8 for charting?
# python import docker for multiple instances of processing
# tda-api documentation: https://tda-api.readthedocs.io/en/stable/

from config import *
from selenium import webdriver
import datetime, json, requests, dotenv

def get_account(broker):
    if broker == 'apca':
        # http request mode 'GET' is used to request data from a specified resource.
        r = requests.get(APCA_ACCOUNT_URL, APCA_HEADERS)
        return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
    data = {
        "symbol": symbol,
        "qty": qty,
        "side": side, 
        "type": type,
        "time_in_force": time_in_force
    }
    # http request mode 'POST' is used to send data to a server to create/update a resource.
    r = requests.post(ORDERS_URL, json= data, headers= HEADERS)
    return json.loads(r.content)

def get_orders():
    r = requests.get(ORDERS_URL, headers= HEADERS)
    return json.loads(r.content)

def access_data():
    r = requests.get(DATA_URL, headers= HEADERS)
    return json.loads(r.content)

response = access_data()
print(response)

try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    
    with webdriver.Firefox(executable_path= '/Users/alecgreene/Documents/Coding Projects/tda-algotrader/geckodriver') as driver:
        c = auth.client_from_login_flow(driver, config.api_key, config.redirect_url, config.token_path)
            