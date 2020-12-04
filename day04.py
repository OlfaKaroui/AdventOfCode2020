from itertools import groupby
import re

# not a huge fan of this but 🤷‍♀️

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

def extractKeyValue(info):
    pattern = re.compile(r"^(?P<k>.[a-zA-Z]*)+\:+(?P<v>.*?)$", re.VERBOSE)
    match = pattern.match(info.strip())
    return (match.group("k"), match.group("v"))

def extractHeight(hgt):
    pattern = re.compile(r"^(?P<height>[0-9]{2,3})(cm|in)$", re.VERBOSE)
    match = pattern.match(hgt)
    return match.group("height")

def verifyPassport(passport):
    passportInfo = passport.split(" ")
    isValidByr , isValidIyr , isValidEyr , isValidHgt , isValidHcl , isValidEcl , isValidPid = (False,False,False,False,False,False,False)
    for info in passportInfo:
        (key,value) = extractKeyValue(info)
        if(key == "byr"):
            isValidByr = int(value) in range(1920,2003)
        elif (key == "iyr"):
            isValidIyr = int(value) in range(2010,2021)
        elif (key == "eyr"):
            isValidEyr = int(value) in range(2020,2031)
        elif (key == "hgt"):
            if "cm" in value:   
                isValidHgt = int(extractHeight(value)) in range(150,194)
            elif "in" in value:   
                isValidHgt = int(extractHeight(value)) in range(59,77)
        elif (key == "hcl"):
            isValidHcl = bool(re.match(r"^#(?:[0-9a-fA-F]{6})$", value))
        elif (key == "ecl"):
            isValidEcl = value in ["amb","blu","brn","gry","grn","hzl","oth"]
        elif (key == "pid"):
            isValidPid = bool(re.match(r"^(?:[0-9]{9})$", value))
    return isValidByr and isValidIyr and isValidEyr and isValidHgt and isValidHcl and isValidEcl and isValidPid
        
with open('data_day04', 'r') as f:
    reader = f.readlines()
    data = [list(group) for item,group in groupby(reader, lambda string: string != "\n")]
    data = [' '.join(item).replace('\r', '').replace('\n', '') for item in data]
    data = [item for item in data if item != '']
    valid = 0
    for info in data:
        if verifyPassport(info):
            valid +=1

    
