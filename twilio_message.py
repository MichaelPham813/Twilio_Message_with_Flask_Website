from twilio.rest import Client
import weather
import characters_HP
import total_people
import json
import os

#Variable that have been embedded into the environment for secret
account_sid = os.environ['SID_CODE']
account_auth = os.environ['ACCOUNT_TOKEN']
account_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
##########################################################

#My number
target_phone_number = os.getenv("OWNER_PHONE_NUMBER")

#Messages
msg = f"Hello you have been selected to attend CIA secret program, {characters_HP.character_selection()}, they will be your mentor, {weather.weather()} is your location and temperature, {total_people.total_people_space()} number of people in space"

#Since we only need to use 1 number
#We don't need to create a dictionary


def messaging():
    client = Client(account_sid, account_auth)

    #Basic messages implementation
    message = client.messages \
                .create(
                    body = msg,
                    from_ = account_phone_number,
                    to = target_phone_number
                )
    with open('message.json', 'a') as f:
        f.write(msg + "\n")
