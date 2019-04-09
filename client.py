from auth import token
import json
from websocket import create_connection
import ssl
import time
import requests

receivedData = create_connection("wss://emotivcortex.com:54321", sslopt={"cert_reqs": ssl.CERT_NONE})

def setup():
    receivedData.send(json.dumps({
        "jsonrpc": "2.0",
        "method": "queryHeadsets",
        "params": {},
        "id": 1
    }))

    receivedData.send(json.dumps({
        "jsonrpc": "2.0",
        "method": "createSession",
        "params": {
            "_auth": token,
            "status": "open",
            "project": "test"
        },
        "id": 1
    }))

    receivedData.send(json.dumps({
        "jsonrpc": "2.0",
        "method": "subscribe",
        "params": {
            "_auth": token,
            "streams": [
                "sys"
            ]
        },
        "id": 1
    }))

    receivedData.send(json.dumps({
        "jsonrpc": "2.0",
        "method": "getDetectionInfo",
        "params": {
            "detection": "mentalCommand"
        },
        "id": 1
    }))

    receivedData.send(json.dumps({
        "jsonrpc": "2.0",
        "method": "getUserLogin",
        "id": 1
    }))

    profile = json.loads(receivedData.recv())["result"][0]

    receivedData.send(json.dumps({
        "jsonrpc": "2.0",
        "method": "subscribe",
        "params": {
            "_auth": token,
            "streams": [
                "fac"
            ]
        },
        "id": 1
    }))

    receivedData.send(json.dumps({
        "jsonrpc": "2.0",
        "method": "setupProfile",
        "params": {
            "_auth": token,
            "profile": profile,
            "status": "create"
        },
        "id": 1
    }))

    setup = json.loads(receivedData.recv())

    receivedData.send(json.dumps({
        "jsonrpc": "2.0",
        "method": "mentalCommandBrainMap",
        "params": {
            "_auth": token,
            "profile": profile

        },
        "id": 1
    }))

def get_value(prev_val):
    face_data = json.loads(receivedData.recv())
    if 'fac' in face_data:
        value_upper = face_data['fac'][2]
        action = face_data['fac'][1]
        return value_upper, action
    else:
        return prev_val, -1
            
                            
