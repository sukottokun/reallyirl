from flask import Flask, request, jsonify
from twilio.rest import Client
import os

app = Flask(__name__)

# Twilio setup
twilio_account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
twilio_auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'
client = Client(twilio_account_sid, twilio_auth_token)


if __name__ == '__main__':
    app.run(debug=True)
