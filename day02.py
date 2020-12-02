
import re
from data_day02 import *

def getIfMatchesNumber(input):
    minimum, maximum, character, password = extractRule(input)
    count = password.count(character)
    return count in range(int(minimum), int(maximum) + 1)


def getIfMatchesPosition(input, number):
    minimum, maximum, character, password = extractRule(input)
    firstCharMatches = password[int(minimum) -1] == character
    secondCharMatches = password[int(maximum) -1] == character
    return secondCharMatches is not firstCharMatches


def extractRule(input):
    pattern = re.compile(r"^(?P<min>.\d?)+\-(?P<max>.\d?)+\s+(?P<character>.[a-zA-Z]?)+\:\s+(?P<password>.*?)$", re.VERBOSE)
    match = pattern.match(input)

    return (match.group("min"), match.group("max"),match.group("character"), match.group("password"))


number = 0
numberPositions = 0
for input in inputs : 
    if getIfMatchesNumber(input):
        number+= 1
    if getIfMatchesPosition(input,numberPositions):
        numberPositions+= 1

print number
print numberPositions

















