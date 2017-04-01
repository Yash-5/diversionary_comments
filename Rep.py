import json
from pprint import pprint
import os

def replaceCorefs(filename):
    print "jsdhbjdsbdjhbv"
    os.chdir("stanford-corenlp-full-2016-10-31")
    with open(filename, "r") as data_file:    
        data = json.load(data_file)

    senten = {}
    for i in range(len(data["sentences"])):
        senten[i + 1] = {}
        for word in data["sentences"][i]["tokens"]:
            senten[i + 1][word["index"]] = word["word"]
    cnt = 1
    for key, coref in data["corefs"].iteritems():
        for curr in coref:
            if curr["isRepresentativeMention"]:
                hold = curr["text"]
                break
        for curr in coref:
            if not curr["isRepresentativeMention"]:
                senten[curr["sentNum"]][curr["startIndex"]] = hold
                for i in range(curr["startIndex"] + 1, curr["endIndex"]):
                    try:
                        del senten[curr["sentNum"]][i]
                    except KeyError:
                        continue
    os.chdir("..")
    return senten
