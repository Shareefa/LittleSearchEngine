#Script to build the search engine index data structure
#Parse text file to get all keywords in a file
#Then Build inverted index
import os
import apiscript
from nltk.corpus import stopwords

PROJECT_DIR = "/Users/abdullah/Documents/LittleSearchEngine"
KAFolder = os.path.join(PROJECT_DIR, "KAVids")

vidList = os.listdir(KAFolder)

num = 0
with open("vidData.txt", "r") as f:
    for line in f:
        line = line.lower()
        print(line)
        break
