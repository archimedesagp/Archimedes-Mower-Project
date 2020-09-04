from __future__ import print_function

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    returnResponse = make_response(res)
    returnResponse.headers['Content-Type'] = 'application/json'
    return returnResponse

def processRequest(req):
    if req.get("queryResult").get("action") == "startMowing":
        # execute mowing script
        return{
            "fulfillmentText": "Commencing Mowing (200)",
            "source": "startMowing Request"
        }

    elif req.get("queryResult").get("action") == "stopMowing":
        # execute stop mowing script
        return{
            "fulfillmentText": "Stopping Mowing Process(200)",
            "source": "stopMowing Request"
        }
    #Go back to base (Reset)
    return{
        "fulfillmentText": "Commencing Reset (200)",
        "source": "Reset Request"
    }

@app.route('/test', methods = ['POST'])
def test():
    return "Hello, Webhook!"

if __name__ == '__main__':
    port = int(os.getenv('PORT',5000))
    print("Starting app on port %d" % port)
    app.run(debug = True, port = port, host='0.0.0.0')
