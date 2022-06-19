import requests
import time
from keep_alive import keep_alive

repair = 0

header = {
    'authorization': 'TOKEN'
}

for i in range (100000):
    repair = repair + 1
    if repair == 30:
        payload = {
            'content': "m!repair"
        }
        r = requests.post('CHANNEL', data=payload, headers=header)
        repair = repair - repair

    else:
        payload = {
            'content': "m!m"
        }
        r = requests.post('CHANNEL', data=payload, headers=header)
    time.sleep(40)

keep_alive()