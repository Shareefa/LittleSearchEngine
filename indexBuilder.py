#Script to build the search engine index data structure
#Parse text file to get all keywords in a file
#Then Build inverted index
import os

PROJECT_DIR = "/Users/abdullah/Documents/LittleSearchEngine"
KAFolder = os.path.join(PROJECT_DIR, "KAVids")

vidList = os.listdir(KAFolder)


with open("vidData.txt", "r") as f:
    for line in f:
