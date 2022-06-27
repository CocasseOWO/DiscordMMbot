import requests
import time

repair = 0

channel = "CHANNEL_HERE"

header = {
    'authorization': 'TOKEN_HERE'
}

for i in range (100000):
    payload = {
        'content': "m!m"
    }
    r = requests.post(channel, data=payload, headers=header)
    time.sleep(3)
