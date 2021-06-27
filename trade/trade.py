#https://alpaca.markets/docs/api-documentation/

from config.config import *
from selenium import webdriver
import asyncio, datetime, dotenv, json, requests 

def get_account():
    r = requests.get(ACCOUNT_URL, headers=HEADERS)
    return json.loads(r.content)

account = get_account()
print(account)

