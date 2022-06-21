import requests
import time

repair = 0

channel = "CHANNEL"

header = {
    'authorization': 'TOKEN'
}

for i in range (100000):
    repair = repair + 1
    if repair == 30:
        payload = {
            'content': "m!repair"
        }
        r = requests.post(channel, data=payload, headers=header)
        time.sleep(3)
        payload = {
            'content': "m!sell all"
        }
        r = requests.post(channel, data=payload, headers=header)
        payload = {
            'content': "m!clan fight"
        }
        r = requests.post(channel, data=payload, headers=header)

        repair = repair - repair


    else:
        payload = {
            'content': "m!m"
        }
        r = requests.post(channel, data=payload, headers=header)
    time.sleep(3)
    print(i)
