#!/usr/bin/env python3

# Ref: https://keestalkstech.com/2019/10/simple-python-code-to-send-message-to-slack-channel-without-packages/

import requests
import json
import sys
import os
from dotenv import load_dotenv, find_dotenv # or importing variables into enviromental variables in system such as passwords/keys

load_dotenv(find_dotenv()) # Try to find the .env file

slack_token = os.environ.get("SLACK_TOKEN")
slack_channel = '#zabbix'
slack_icon_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTH-qkvoe5JfAM3GwYuQ5H_lHHStPq7r32pdg&usqp=CAU' # Google image link
slack_user_name = 'Zabbix (IOM) Starscloud'



def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': text,
        'icon_url': slack_icon_url,
        'username': slack_user_name,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()	


if __name__ == "__main__":
    alert = ""
    for x in sys.argv:
            if x == sys.argv[0]: # skip sys.argv[0]
                    continue
            else:
                    alert += f'{x} ' # include space after each argument

    post_message_to_slack(alert) # Send alert string to method post_message-slack