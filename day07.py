from collections import defaultdict
import re

goldSupporters = []

def getColor(colorString):
    colorsPattern = re.compile(r"^(?P<color>.[a-zA-Z\s]*)\s(bags)$", re.VERBOSE)
    return colorsPattern.match(colorString).group("color")

# for part 1
def getInnerColors(innerColorsString, color, colorCouples):
    innerColorsPattern = re.compile(r"^(?P<number>.\d?)\s(?P<color>.[a-zA-Z\s]*)\s(bags|bag)[.]{0,1}$", re.VERBOSE)
    if not "no other bags" in innerColorsString:
        for edge in innerColorsString.split(","):
            colorCouples[innerColorsPattern.match(edge).group("color")].add(color)

# for part 2
def getColorsGraph(innerColorsString, color, colorGraph):
    innerColorsPattern = re.compile(r"^(?P<number>.\d?)\s(?P<color>.[a-zA-Z\s]*)\s(bags|bag)[.]{0,1}$", re.VERBOSE)
    if not "no other bags" in innerColorsString:
        for edge in innerColorsString.split(","):
            colorGraph[color].append((innerColorsPattern.match(edge).group("color"), innerColorsPattern.match(edge).group("number")))


def DFS(color, visited):
    visited.append(color)
    for outerColor in colorCouples[color]:
        if outerColor not in goldSupporters:
            goldSupporters.append(outerColor)
            if outerColor not in visited:
                DFS(outerColor,visited)

def getCost(color):
    total = 0
    for color, number in colorGraph[color]:
        total += int(number) + int(number) * getCost(color)
    return total
    
with open('./data/data_day07', 'r') as f:
    data = f.readlines()
    colorCouples = defaultdict(set)
    colorGraph = defaultdict(list)
    for rule in data:
        rule = rule.replace('\n', '')
        color = getColor(rule.split("contain",1)[0].lstrip().rstrip())
        getInnerColors(rule.split("contain",1)[1], color, colorCouples)
        getColorsGraph(rule.split("contain",1)[1], color, colorGraph)
    DFS("shiny gold", [])
    print len(goldSupporters)
    print(getCost("shiny gold"))
    
    