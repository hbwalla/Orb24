# import xml.etree.ElementTree as ET

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

functionLineNumber = [] # where the 'def's are
functionException = [] # where the '):'s are
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


# maybe update these for if first spacing is 2 spaces and not 4
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


for i in functionDict:
    if functionDict[i]["name"] == '__init__':
        functionDict[i]["status"] = 'classInit'
    else:
        functionDict[i]["status"] = 'lone' # this will be updated later if function is nested

pairs = []

# if # is after the colon, it's fine, but if it's before... problematic. might have to make new list...

print(functionLineNumber)
newFLN = []

for i in functionLineNumber:
    if ("# def" not in contents[i]) or ("#def" not in contents[i]):
        newFLN.append(i)

print(newFLN)


if len(functionException) == len(functionLineNumber):
    for i, j in zip(functionLineNumber, functionException):
        if i != j:
            pairs.append([i, j])
else:
    raise(IndexError)

pairDict = dict()

for i in range(len(pairs)):
    pairDict["pair" + str(i)] = {"range": '', "begin": '', "end": '', "string": ''}
    pairDict["pair" + str(i)]["range"] = range(pairs[i][0], pairs[i][1] + 1, 1)

lastDict = dict()

for i in range(len(pairs)):
    tempRange = pairDict["pair" + str(i)]["range"]
    indices = []
    lineString = ''
    for j in tempRange:
        indices.append(j)
    for k in indices:
        lineString += contents[k]
    pairDict["pair" + str(i)]["string"] = lineString


for i in range(len(pairs)):
    if type(pairDict["pair" + str(i)]["string"]) == str:
        testList = []
        string = pairDict["pair" + str(i)]["string"]
        for j in string:
            testList.append(j)
            if k == ' ':
                testList.remove(k)
        for k in testList:
            if k == '\n':
                testList.remove(k)
        for k in testList:
            if k == '\\':
                testList.remove(k)
        for k in testList:
            if k == ':':
                testList.remove(k)
        nums = []
        for k in range(len(testList)):
            if testList[k] == '(':
                nums.append(k)
            if testList[k] == ')':
                nums.append(k)
        for l in range(len(nums)):
            if len(nums) == 2:
                start = nums[0]
                end = nums[1]
        inputRange = range(start, end, 1)
        input = ''
        for i in inputRange:
            if (testList[i] != ' ') and (testList[i] != '('):
                input += testList[i]


