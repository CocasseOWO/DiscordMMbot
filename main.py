import requests
import time

repair = 0

header = {
    'authorization': 'TOKEN'
}

for i in range (100000):
    repair = repair + 1
    if repair == 5:
        payload = {
            'content': "m!repair"
        }
        r = requests.post('CHANNEL', data=payload, headers=header)
        time.sleep(3)
        payload = {
            'content': "m!sell all"
        }
        r = requests.post('CHANNEL', data=payload, headers=header)
        payload = {
            'content': "m!clan fight"
        }
        r = requests.post('CHANNEL', data=payload, headers=header)

        repair = repair - repair


    else:
        payload = {
            'content': "m!m"
        }
        r = requests.post('CHANNEL', data=payload, headers=header)
    time.sleep(3)
    print(i)
