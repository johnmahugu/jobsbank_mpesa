import requests
import json
from bottle import *

@route('/hello')
def hello():
    return "Hello World!"
@route('/mpesa')
def mpesa():
    #run(host='localhost', port=8080, debug=True)
#   return 'Hello, World!'
    url = "http://5.189.139.236:8080/Dairy/api/PaymentAPI_V1/guyana_t"

    payload = "{\"mobile\":\"254799606060\",\"account\":\"254799101010\",\"amount\":\"7\",}"
    headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer c2xxOUFsZ2VMQ2JIOWFlSnhTUE5RVHdObkFTRkFBNk4yZktUU1hnM2luanB3RmNv'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
run()

"""from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
"""
