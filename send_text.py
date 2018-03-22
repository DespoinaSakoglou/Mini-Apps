
"""
A program that sends a text message using twilio

Created on Mon Mar 19 16:38:13 2018

@author: Despoina
"""

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "*********************************"
# Your Auth Token from twilio.com/console
auth_token  = "**********************************"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+18*********", 
    from_="+18*********",
    body="Hello from Python!")

print(message.sid)
