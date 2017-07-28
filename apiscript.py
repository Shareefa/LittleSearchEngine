#Script to pull descriptions of all the youtube videos
#using the Youtube API


import requests
import sys
import os
import re

url = "https://www.googleapis.com/youtube/v3/videos"
API_KEY = "AIzaSyBiIKmKVIDu-sgnE0m-qBePXip4FdCaaiU"
vidId = "6dACXPirT3s,lUA1LYCoIAg"

PROJECT_DIR = "/Users/abdullah/Documents/LittleSearchEngine"

KAFolder = os.path.join(PROJECT_DIR, "KAVids")

vidList = os.listdir(KAFolder)

idList = []

for vid in vidList:
    idList.append(vid[-15:-4])


if __name__ == "__main__":
    print("entered")
    listOfLists = []
    while len(idList) > 50:
        listOfLists.append(idList[:50])
        idList = idList[50:]
    listOfLists.append(idList)
    payload = {'part': 'snippet', 'key': API_KEY}
    num = 0
    with open('vidData.txt', 'w') as f:
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
                f.write("{id}\t{file}\tvideo\t{title}\t{desc}\n".format( id=vid["id"], file=vidList[num], title=vid["snippet"]["title"], desc=vid["snippet"]["description"]))
                num = num + 1
else:
    print("didn't work?")
