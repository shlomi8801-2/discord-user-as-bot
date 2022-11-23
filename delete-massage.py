import requests
import random, string
import time
import json
class discord:
    url = 'https://discord.com/api/v9/channels/<channelid>/messages?limit=50'
    delurl = "https://discord.com/api/v9/channels/<channelid>/messages/"
    token = "same token from the send massage file"
    token2 = "new token that require to inspect after deleting massage"
    contenttype = "application/json"
    channelid = "channel that the user will work with"
    id = "user id for the massages to delete"
while True:
    try:
        headers = {"Authorization": discord.token, "content-type": "application/json","limit": "50"}
        response = requests.get(discord.url, headers=headers)
        # print(json.loads(response.text))
        for x in range(len(json.loads(response.text))):
            jsonlist = json.loads(response.text)[x]
            print(str(jsonlist)[str(jsonlist).find("{'id': '")+len("{'id': '"):str(jsonlist).find("', 'type':")])


            messageid = str(jsonlist)[str(jsonlist).find("{'id': '")+len("{'id': '"):str(jsonlist).find("', 'type':")]
            headers2 = {"Authorization": discord.token2, "content-type": "application/json"}
            if str(jsonlist)[str(jsonlist).find("'author': {'id': '")+len("'author': {'id': '"):str(jsonlist).find("', 'username':")] == discord.id:
                response = requests.delete(discord.delurl+messageid, headers=headers2)
    except Exception as e:
        print(e)

    time.sleep(1)
