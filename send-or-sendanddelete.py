import requests
import random, string
import time
import json

class discord:
    token = "TOKEN"
    userid = "uour user id"




def sendmassageanddel(userid,channelid,massagecontent,token,delete):
    headers = {"Authorization": token, "content-type": "application/json"}
    body='{"content": "'+massagecontent+'", "nonce": "' + str(random.randint(0, 1000000000000)) + '", "tts": false}'
    try:
        response = requests.post('https://discord.com/api/v9/channels/'+channelid+'/messages', headers=headers, data=body)
        print("massage sent")
    except:
        print("something went wrong")
        return
    if delete == True:
        try:
            headers = {"Authorization": token, "content-type": "application/json","limit": "50"}
            response = requests.get('https://discord.com/api/v9/channels/'+channelid+'/messages?limit=50', headers=headers)
            for x in range(len(json.loads(response.text))):
                jsonlist = json.loads(response.text)[x]
                print(str(jsonlist)[str(jsonlist).find("{'id': '")+len("{'id': '"):str(jsonlist).find("', 'type':")])


                messageid = str(jsonlist)[str(jsonlist).find("{'id': '")+len("{'id': '"):str(jsonlist).find("', 'type':")]
                headers2 = {"Authorization": token, "content-type": "application/json"}
                if str(jsonlist)[str(jsonlist).find("'author': {'id': '")+len("'author': {'id': '"):str(jsonlist).find("', 'username':")] == userid:
                    response = requests.delete('https://discord.com/api/v9/channels/'+channelid+'/messages/'+messageid, headers=headers2)
        except Exception as e:
            if str(e) == "Expecting value: line 1 column 1 (char 0)":
                print("massage deleted")
            else:
                print("something went wrong")

while True:
    sendmassageanddel(discord.userid,"1044896654240784464","hello",discord.token,True)

    time.sleep(60)
