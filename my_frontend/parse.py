import json
import numpy as np

pathName = "/Users/haileywallace/desktop/Brain Child"
fileName = "/linear_algebra.py"

file = open(pathName + fileName, "r")

if ".py" in str(file):
    pass
else:
    raise(FileNotFoundError)

# contents = json.dumps(file.readlines())
contents = file.readlines()
#note: python isinstance

classCharacters = []
classLineNumber = []
classLines = []

program = dict()
scrapDict = dict()
scrapList = []

y = 0
for i in range(len(contents)):
    if "class" in contents[i]:
        classLineNumber.append(i)
        y += 1

for i in range(len(classLineNumber)):
    scrapDict["class" + str(i)] = {"begin": '', "end": '', "line": ''}
    program["class" + str(i)] = {"name": '', "line": classLineNumber[i]}
    # scrapList.append(i)

for i in range(len(classLineNumber)):
# for i in contents:
    if "class" in contents[classLineNumber[i]]:
        # x = 0
        # x +=1
        readClassLines = []
        # while x <= len(classLineNumber):
        # scrapDict["class" + classLineNumber[x]] = {"begin": '', "end": ''}
            # readClassLines = []
        # for j in i:
        for j in contents[classLineNumber[i]]:
            readClassLines.append(j)
        for k in range(len(readClassLines)):
            if readClassLines[k] == "c" and readClassLines[k + 1] == "l" and readClassLines[k + 2] == "a":
                    # classCharacters.append(k)
                # scrapDict["class" + str(x)]["begin"] = k
                scrapDict["class" + str(i)]["begin"] = k
            if readClassLines[k] == ":":
                scrapDict["class" + str(i)]["end"] = k
        scrapDict["class" + str(i)]["line"] = readClassLines
    # if "class" not in i:
    if "class" not in contents[classLineNumber[i]]:
        pass
        # x += 1
        # scrapDict["class" + str(x)] = {"begin": '', "end": ''}
        # continue
print(scrapDict)

for i in range(len(classLineNumber)):
    end = scrapDict["class" + str(i)]["end"] - 1
    lines = scrapDict["class" + str(i)]["line"]
    myRange = range(6, scrapDict["class" + str(i)]["end"], 1)
    name = ''
    for j in myRange:
        name += lines[j]
    program["class" + str(i)]["name"] = name
    
    
print(program)
    # diff = scrapDict["class" + str(i)]["end"] - (scrapDict["class" + str(i)]["begin"] + 6)

            # if readClassLines[k] == ":":
            #     classCharacters.append(k)
        # program["class" + i] =

# for i in range(len(classCharacters)):
#     if classCharacters[i] == 0:
#         print(classCharacters[i])

        # print(classCharacters[i + 1])
        # print(readClassLines[classCharacters[i]])

        #     if j == ":":
        #         list.append(np.where(i[j == ":"]))
        # program["class" + str(i)] = {"line": i, "name": "ooga booga!"}

    # if "(" in contents[i]:
    #     list.append("(", i)
    # if ")" in contents[i]:
    # if "def" in contents[i]:
        # program["function" + str(i)] = {"line": i, "name": "jeepers!"}
    #     print("function") 
    # if ":" in contents[i]:
    #     print("we're defining something!!")

# for line in contents:
#     for l in range(len(line)):
#         if line[l] == "c":
#             list.append(line)

# print(list)
        
# print(program)
# print(classCharacters)
# print(classLineNumber)
# print(classLines)
# print(readClassLines)
        