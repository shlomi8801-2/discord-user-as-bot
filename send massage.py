import requests
import random, string
import time

class discord:
    url = 'https://discord.com/api/v9/channels/'
    token = "TOKEN"
    message = "roy is homo"
    contenttype = "application/json"
    channelid = "1034035170463973418"
discord.url = discord.url + discord.channelid + "/messages"
while True:


    headers = {"Authorization": discord.token, "content-type": "application/json"}
    body='{"content": "'+discord.message+'", "nonce": "' + str(random.randint(0, 1000000000000)) + '", "tts": false}'
    try:
        response = requests.post(discord.url, headers=headers, data=body)
        if str(response) == '<Response [200]>':
            print("Message sent")
    except Exception as e:
        print(e)
    time.sleep(60)
