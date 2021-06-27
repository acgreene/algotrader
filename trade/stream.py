# Stream live market data from Alpaca
import websocket, json
from config.config import *

# input: the reference to the websocket app
# output: none
# function: opens a connection to the alpaca market stream websocket

def on_open(ws):
    auth_data = {
        "action": "auth",
        "key": API_KEY,
        "secret": SECRET_KEY
    }
    ws.send(json.dumps(auth_data))

    subscribe = {
        "action":"subscribe",
        "trades":["SPY"],
        "quotes":[],
        "bars":["CHWY","CRSR"]
    }
    ws.send(json.dumps(subscribe))


def on_message(ws, message):
    print("received a message")
    print(message)

def on_close(ws):
    print("closed connection")

socket = "wss://stream.data.alpaca.markets/v2/iex"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message, on_close=on_close)
ws.run_forever()