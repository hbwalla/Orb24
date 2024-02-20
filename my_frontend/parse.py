import json
import numpy as np

pathName = "/Users/haileywallace/desktop/Brain Child"
fileName = "/linear_algebra.py"

file = open(pathName + fileName, "r")

# Note: versions for javascript and c++ will be made!
# This file is specifically for python

if ".py" in str(file):
    pass
else:
    raise(FileNotFoundError)

contents = file.readlines()

# gathering classes

classCharacters = []
classLineNumber = [] # this is actually index number in list of lines (i.e. line1 = CLN[0]), easier that way!
classLines = []

program = dict()
scrapDict1 = dict()
scrapList = []

for i in range(len(contents)):
    if "class" in contents[i]:
        classLineNumber.append(i)

for i in range(len(classLineNumber)):
    scrapDict1["class" + str(i)] = {"begin": '', "end": '', "line": '', "indent": ''}
    program["class" + str(i)] = {"name": '', "line": classLineNumber[i] + 1, "indent": ''}

for i in range(len(classLineNumber)):
    if "class" in contents[classLineNumber[i]]:
        readClassLines = []
        for j in contents[classLineNumber[i]]:
            readClassLines.append(j)
        for k in range(len(readClassLines)):
            if (readClassLines[k] == " " and readClassLines[k + 1] == " " and readClassLines[k + 2] == " " and \
                readClassLines[k + 3] == " "):
                scrapDict1["class" + str(i)]["indent"] = 1
            if readClassLines[k] == "c" and readClassLines[k + 1] == "l" and readClassLines[k + 2] == "a":
                scrapDict1["class" + str(i)]["begin"] = k
            if readClassLines[k] == ":":
                scrapDict1["class" + str(i)]["end"] = k
        scrapDict1["class" + str(i)]["line"] = readClassLines
    if "class" not in contents[classLineNumber[i]]:
        pass

for i in range(len(classLineNumber)):
    lines = scrapDict1["class" + str(i)]["line"]
    myRange = range(6, scrapDict1["class" + str(i)]["end"], 1)
    name = ''
    for j in myRange:
        name += lines[j]
    program["class" + str(i)]["name"] = name
    program["class" + str(i)]["indent"] = scrapDict1["class" + str(i)]["indent"]
    if program["class" + str(i)]["indent"] == '':
        program["class" + str(i)]["indent"] = 0

# gathering functions

functionLineNumber = []
functionException = []
scrapDict2 = dict()
functionDict = dict()

for i in range(len(contents)):
    if "def" in contents[i]:
        functionLineNumber.append(i)

for i in range(len(functionLineNumber)):
    scrapDict2["function" + str(i)] = {"begin": '', "end": '', "line": '', "indent": ''}
    functionDict["function" + str(i)] = {"name": '', "line": functionLineNumber[i] + 1, "indent": '', "status": '', "input": {''}}

# this could go very wrong and pick up on a lot of other stuff... fix later :D
for i in range(len(contents)):
    if ("):" or ") :")  in contents[i]:
        functionException.append(i)

for i in range(len(functionLineNumber)):
    if "def" in contents[functionLineNumber[i]]:
        readFunctionLines = []
        for j in contents[functionLineNumber[i]]:
            readFunctionLines.append(j)
        for k in range(len(readFunctionLines)):
            if readFunctionLines[k] == "d" and readFunctionLines[k + 1] == "e" and readFunctionLines[k + 2] == "f":
                scrapDict2["function" + str(i)]["begin"] = k + 4
            if (readFunctionLines[k] == " " and readFunctionLines[k + 1] == " " and readFunctionLines[k + 2] == " " and \
                readFunctionLines[k + 3] == " "):
                scrapDict2["function" + str(i)]["indent"] = 1
            if (readFunctionLines[k] == " " and readFunctionLines[k + 1] == " " and readFunctionLines[k + 2] == " " and \
                readFunctionLines[k + 3] == " " and readFunctionLines[k + 4] == " " and readFunctionLines[k + 5] == " " and \
                readFunctionLines[k + 6] == " " and readFunctionLines[k + 7] == " "):
                scrapDict2["function" + str(i)]["indent"] = 2
            if readFunctionLines[k] == "(":
                scrapDict2["function" + str(i)]["end"] = k
        scrapDict2["function" + str(i)]["line"] = readFunctionLines
    if "def" not in contents[functionLineNumber[i]]:
        pass

for i in range(len(functionLineNumber)):
    lines = scrapDict2["function" + str(i)]["line"]
    myRange = range(scrapDict2["function" + str(i)]["begin"], scrapDict2["function" + str(i)]["end"], 1)
    name = ''
    for j in myRange:
        name += lines[j]
    functionDict["function" + str(i)]["name"] = name
    functionDict["function" + str(i)]["indent"] = scrapDict2["function" + str(i)]["indent"]
    if functionDict["function" + str(i)]["indent"] == '':
        functionDict["function" + str(i)]["indent"] = 0

# commonFunctionList = []
# differentFunctionList = []

# for i in range(len(functionException)):
#     if functionException[i] != functionLineNumber[i]:
#         differentFunctionList.append(functionException[i])
#     if functionException[i] == functionLineNumber[i]:
#         commonFunctionList.append(functionException[i])

for i in functionDict:
    if functionDict[i]["name"] == '__init__':
        functionDict[i]["status"] = 'classInit'
    else:
        functionDict[i]["status"] = 'lone'

pairs = []

if len(functionException) == len(functionLineNumber):
    for i, j in zip(functionLineNumber, functionException):
        if i != j:
            pairs.append([i, j])
else:
    raise(IndexError)

pairDict = dict()

for i in range(len(pairs)):
    pairDict["pair" + str(i)] = {"range": '', "begin": '', "end": ''}
    pairDict["pair" + str(i)]["range"] = range(pairs[i][0], pairs[i][1] + 1, 1)

# print(pairDict)

lastDict = dict()

for i in range(len(pairs)):
    tempRange = pairDict["pair" + str(i)]["range"]
    for j in tempRange:
        myList = []
        for k in contents[j]:
            myList.append(k)
    # conacanate list into one string and remove all unnecessary stuff like "def"!
    myList.strip("\n")
    myList.strip("\\")
    print(myList)

# for i in range(len(pairs)):
#     tempRange = pairDict["pair" + str(i)]["range"]
#     tempLines = []
#     for j in tempRange:
#         tempLines.append(contents[j])
#         tempCharacters = []
#         tempDict = dict()

#         for k in range(len(contents[j])):
#             if contents[j][k] == "(":
#                 # pairDict["pair" + str(i)]["begin"] = k + 1
#                 tempDict["line" + str()]
#             if contents[j][k] == ")" and contents[j][k + 1] == ":":
#                 pairDict["pair" + str(i)]["end"] = k - 1
#             print(range(pairDict))

    
        # if "(" in contents[j]:
        #     print(j)

        
# for i in range(len(functionLineNumber)):
#     specLines = range(pairs[i][0], pairs[i][1], 1)
#     print(specLines)
    # if "def" in contents[functionLineNumber[i]]:
    #     readFunctionLines = []
    #     for j in contents[functionLineNumber[i]]:
    #         readFunctionLines.append(j)
        