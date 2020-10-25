'''
If I want to use this I will have to set up a TRIAL TWILIO ACCOUNT

Step 1:  [Text Messages]  Create a list of text messages to choose from to send
my_messages = ['',''] '''

GOOD_MORNING_QUOTES = ['Good Morning!', 'Dude, this totally me.', 'Hope you are having a good morning :P']


''' Step 2: Send out message to who the target is.  Send a preset message using API send_message(my_messages[0])'''

from twilio.rest import Client
import schedule
import random

from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

cellphone = 123
twilio_number = 234


def send_message(quotes_list = GOOD_MORNING_QUOTES):
    account = twilio_account
    token = twilio_token
    client = Client(account, token)

    quote = quotes_list[random.randint(0,len(quotes_list)-1)]

    client.messages.create(to = cellphone,
                           from = twilio_number,
                           body = quote)

'''Step 3: Schedule that job and you are all done'''
# send message in the morning
schedule.every().day.at('10:30').do(send_message,quote)

# schedule.every(10).minutes.do(job)
