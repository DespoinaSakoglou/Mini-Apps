# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:38:13 2018

@author: Despoina
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC046d10a9159023f402e440b1d6b3cb87"
# Your Auth Token from twilio.com/console
auth_token  = "781357f82829876d2d301d4d7858c1b7"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18438133730", 
    from_="+18548886908",
    body="Hello from Python!")

print(message.sid)
