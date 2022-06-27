import requests
import websocket
import json
import threading
import time
import cv2
import numpy as np
from pytesseract import pytesseract
import shutil

TOKEN = 'TOKEN_HERE'
CHANNEL = 'CHANNEL_HERE'
pytesseract.tesseract_cmd = "tesseract way here"
BOTID = '520282851925688321'

def send_json_request(ws,request):
    ws.send(json.dumps(request))

def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def heartbeat(interval,ws):
    print('Heartbeat begin')
    while True:
        time.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        send_json_request(ws, heartbeatJSON)
        print('Heartbeat sent')

ws = websocket.WebSocket()
ws.connect('wss://gateway.discord.gg/?v=6&encording=json')
event = recieve_json_response(ws)

heartbeat_interval = event['d']['heartbeat_interval'] / 1000
threading._start_new_thread(heartbeat, (heartbeat_interval, ws))

token = f"{TOKEN}"
payload = {
    'op': 2,
    "d": {
        "token": token,
        "properties": {
            "$os": "windows",
            "$browser": "chrome",
            "$device": 'pc'
        }
    }
}
send_json_request(ws, payload)

header = {
    'authorization': f'{TOKEN}'
}
chan = f"https://discord.com/api/v9/channels/{CHANNEL}/messages"

while True:
    event = recieve_json_response(ws)

    try:
        if event['d']['channel_id'] == f"{CHANNEL}" and "Your pickaxe is broken" in event['d']['content'] and event['d']['author']['id'] == f"{BOTID}":
            print('repairing pickaxe')
            payload = {
                'content': "m!repair"
            }
            r = requests.post(chan, data=payload, headers=header)
            time.sleep(3)
            payload = {
                'content': "m!sell all"
            }
            r = requests.post(chan, data=payload, headers=header)
            time.sleep(3)
            payload = {
                'content': "m!clan fight"
            }
            r = requests.post(chan, data=payload, headers=header)
            time.sleep(3)

        elif event['d']['channel_id'] == f"{CHANNEL}" and "being attacked" in event['d']['embeds'][0]['description'] and event['d']['author']['id'] == f"{BOTID}":
            image_url = event['d']['embeds'][0]['image']['url']
            print(f"checking captcha {image_url}")
            filename = image_url.split("/")[-1]

            r = requests.get(image_url, stream=True)

            if r.status_code == 200:
                r.raw.decode_content = True

                with open(filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

                print('Image sucessfully Downloaded: ', filename)
            else:
                print('Image Couldn\'t be retreived')
            print('analysing image...')

            img = cv2.imread('test.jpeg')
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            sensitivity = 70
            lower_range = np.array([0, 0, 255 - sensitivity])
            upper_range = np.array([255, sensitivity, 255])

            mask = cv2.inRange(hsv, lower_range, upper_range)
            img = mask

            words_in_image = pytesseract.image_to_string(img)
            time.sleep(2)

            payload = {
                'content': f"m!f {words_in_image}"
            }
            r = requests.post(chan, data=payload, headers=header)
            time.sleep(3)

        elif event['d']['author']['id'] == f"{BOTID}" and "During the session you found" in event['d']['embeds'][0]['fields'][0]['name']:
            print("prouuuuuuutXD")
            payload = {
                'content': "m!m"
            }
            r = requests.post(chan, data=payload, headers=header)
            time.sleep(3)

    except:
        pass