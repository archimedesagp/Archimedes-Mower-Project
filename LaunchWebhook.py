# Senior Design Project: Team Eureka
# Prototype: Archimedes AGP
# Language of use: Python
# Purpose of file: To host a local webhook that will be sent POST requests
#                  in order to send back feedback from the mower's raspberry pi.

# Basic tools for dealing with local files and json files
import json
import os

# Web Framework
from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

# Main entry point for our webhook
@app.route('/webhook', methods=['POST'])
def webhook():
    #Get the request from DialogFlow in the form of a json file
    req = request.get_json(silent=True, force=True)

    # takes the json file to see what intent was triggered in DialogFlow and
    # executes the intent while storing it back into res.
    res = processRequest(req)
    res = json.dumps(res, indent=4)

    # Takes our response, parses it into a readable format for DialogFlow
    # and returns it.
    returnResponse = make_response(res)
    returnResponse.headers['Content-Type'] = 'application/json'
    return returnResponse


# XXX: Would prefer this be in switch case form to save resources
def processRequest(req):
    # TODO: Make Initialization script for mower
    if req.get("queryResult").get("action") == "Initialize":
        pass

    #The intent was to start the mower
    elif req.get("queryResult").get("action") == "startMowing":
        # TODO: Make script to start the mower
        return{
            "fulfillmentText": "Commencing Mowing (200)",
            "source": "startMowing Request"
        }

    # The intent was to stop the mower
    elif req.get("queryResult").get("action") == "stopMowing":
        # TODO: Make script to stop the mower
        return{
            "fulfillmentText": "Stopping Mowing Process(200)",
            "source": "stopMowing Request"
        }

    # TODO: Make better handling code for intent not being recognized
    return{
        "fulfillmentText": "Command Recognized (200)",
        "source": "POST Request"
    }

# XXX: Use this endpoint only for testing reasons such as confirming webhook
#      connection
@app.route('/test', methods = ['POST'])
def test():
    return "Hello, Webhook!"

#Hosts the app locally for ngrok to see.
if __name__ == '__main__':
    port = int(os.getenv('PORT',5000))
    print("Starting app on port %d" % port)
    app.run(debug = True, port = port, host='0.0.0.0')
