import json

pathName = "/Users/haileywallace/desktop/Brain Child"
fileName = "/linear_algebra.py"

file = open(pathName + fileName, "r")

if ".py" in str(file):
    pass
else:
    raise(FileNotFoundError)

contents = json.dumps(file.readlines())
#note: python isinstance

for line in contents:
    if type(line.find("class")) == int:
        print("yay")