#Script to pull descriptions of all the youtube videos
#using the Youtube API


import requests
import sys
import os
import re

url = "https://www.googleapis.com/youtube/v3/videos"
API_KEY = "AIzaSyBiIKmKVIDu-sgnE0m-qBePXip4FdCaaiU"
vidId = "6dACXPirT3s,lUA1LYCoIAg"

PROJECT_DIR = "/Users/abdullah/Documents/Emerge"

KAFolder = os.path.join(PROJECT_DIR, "KAVids")

vidList = os.listdir(KAFolder)

idList = []
for vid in vidList:
    idList.append(vid[-15:-4])
listOfLists = []
while len(idList) > 50:
    listOfLists.append(idList[:50])
    idList = idList[50:]
listOfLists.append(idList)

payload = {'part': 'snippet', 'key': API_KEY}
num = 1
with open('vidData.txt', 'w') as f:
    f.write("Number,Id,Title,Description\n")

    for listOf50 in listOfLists:
        print("started")
        idListStr = ",".join(listOf50)
        print(idListStr)
        payload["id"] = idListStr
        r = requests.get(url, params = payload)
        res = r.json()
        for vid in res["items"]:
            vid["snippet"]["description"] = re.sub(r'\s+', ' ', vid["snippet"]["description"])
            print("Writing")
            f.write("{num!s},{id},{title},{desc}\n".format(num=num, id=vid["id"], title=vid["snippet"]["title"], desc=vid["snippet"]["description"]))
            num = num + 1