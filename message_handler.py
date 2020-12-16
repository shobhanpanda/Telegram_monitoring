# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:31:16 2020

@author: shobhan
"""
import configparser
import re
from telethon import TelegramClient, events
from twilio.rest import Client

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

account_sid = config['Twilio']['account_sid']
auth_token = config['Twilio']['auth_token']
twilioClient = Client(account_sid, auth_token)

from_number = config['Twilio']['from_number']
to_number = config['Twilio']['to_number']

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']

client = TelegramClient('anon', api_id, api_hash)

#Function which runs on every message
@client.on(events.NewMessage)
async def my_event_handler(event):
    # Regex on every message. For now, it checks for go messages and triggers the call and SMS through Twilio
    if re.search(r'(?i).*\b(?:go)\b',event.raw_text):
        message = twilioClient.messages.create(
                              from_= from_number,
                              body= event.raw_text[0:130],
                              to= to_number
                              )
        print(message.sid)
        call = twilioClient.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to= to_number,
                        from_= from_number
                    )
        print(call.sid)
    print(event)
    print(event.raw_text)
    print("\n\n")


client.start()
client.run_until_disconnected()