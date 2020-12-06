from itertools import groupby
import re

def getUniqueLettersTotal(data):
    data = [''.join(item).replace('\r', '').replace('\n', '') for item in data]
    valid = 0
    for info in data:
        valid += len("".join(dict.fromkeys(info)))
    return valid

def getAllVotesLetterTotal(reader):
    valid = 0
    for info in data:
        peopleNumber = len(info)
        info = ''.join(info).replace('\r', '').replace('\n', '')
        if info != "" :
            allLetters = "".join(dict.fromkeys(info))
            for letter in allLetters:
                count = info.count(letter)
                if count == peopleNumber:
                    valid += 1
    return valid

with open('data_day06', 'r') as f:
    reader = f.readlines()
    data = [list(group) for item,group in groupby(reader, lambda string: string != "\n")]
    print(getUniqueLettersTotal(data))
    print(getAllVotesLetterTotal(data))
    
    
   
        

    
