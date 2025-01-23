from SmartApi import SmartConnect
from SmartApi.smartWebSocketV2 import SmartWebSocketV2
import urllib.request
import os
import json
import pandas as pd
import numpy as np
import datetime as dt
from pyotp import TOTP
from datetime import datetime
import http.client
from logzero import logger




TOTP("UU4TPZJBCONMGK4DXAAUQP3E6E").now()

#Initialize the API
key_path = r"C:\Users\giris\DEVELOP\ANGEL_ONE_API"
os.chdir(key_path)
key_secret = open("key.txt","r").read().split()




action = 1
mode = 1

token_list = [
    {
        "exchangeType": 5,
        "tokens": ["26009"]
    }
]
token_list1 = [
    {
        "action": 0,
        "exchangeType": 1,
        "tokens": ["26009"]
    }
]

sws = SmartWebSocketV2(data['data']['jwtToken'], key_secret[0], key_secret[2], feed_token)


def on_data(wsapp, message):
    logger.info("Ticks: {}".format(message))
    # close_connection()

def on_open(wsapp):
    logger.info("on open")
    sws.subscribe(correlation_id, mode, token_list)
    # sws.unsubscribe(correlation_id, mode, token_list1)


def on_error(wsapp, error):
    logger.error(error)


def on_close(wsapp):
    logger.info("Close")



def close_connection():
    sws.close_connection()


# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error
sws.on_close = on_close

sws.connect()













