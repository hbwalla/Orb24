import ast
import json


class PyFileVisitor(ast.NodeVisitor):
    def __init__(self):
        self.result_dict = {}
        self.result_list = []
        self.current_class = None
        self.function_nesting_level = 0

    def visit_ClassDef(self, node):
        # self.current_class = node.name
        class_info = {"type": "class", "name": node.name, "methods": []}
        # self.result_dict[node.name] = {"type": "class", 'methods': {}} # update method?
        self.result_list.append(class_info)
        self.current_class = class_info
        self.generic_visit(node)
        self.current_class = None

    def visit_FunctionDef(self, node):
        args = [arg.arg for arg in node.args.args]
        # function_info = {"type": "function", 'arguments': args, 'level': self.function_nesting_level}
        function_info = {"type": "function", "name": node.name, 'arguments': args, 'level': self.function_nesting_level}
        if self.current_class:
            # self.result_dict[self.current_class]['methods'][node.name] = function_info
            self.current_class["methods"].append(function_info)
        else:
            # self.result_dict[node.name] = function_info
            self.result_list.append(function_info)

        self.function_nesting_level += 1
        self.generic_visit(node)
        self.function_nesting_level -= 1

def extract_classes_functions(filename):
    with open(filename, 'r') as file:
        tree = ast.parse(file.read(), filename=filename)
    visitor = PyFileVisitor()
    visitor.visit(tree)
    # return visitor.result_dict
    return visitor.result_list

if __name__ == '__main__':
    result = extract_classes_functions('/Users/haileywallace/Desktop/Brain Child/linear_algebra.py')
    with open('/Users/haileywallace/Desktop/orb_dev/Orb24/my_frontend/output.json', "w") as outfile:
        json.dump(result, outfile, indent = 4)
    print(result)

# have input for arguments in a function be a tuple to assign types (or multiple possible types)
# switch indentation of type and name of the function/class
# types have to match type
# self is a different data type, don't assign or delete it
# fix nesting level to update (inside function/class = level 1)
# functions within a class are called methods
# have this recognize files too
# lightweight ID with each block, could be generated here; ID for file, ID for code block in file, only checking 
    # once for file ID
# certain fileIDs/blocks will be written as connected to each other, positioned in canvas, save representation
    # of blocks. saves positioning

# drawing app- canva- for references for pan/zoom
# look at node-red
# administrators will populate code base with new code, including JSON associated with file
# save current state or several previous states- undo doesn't have a ton of utility
# compare changes in version management- if no changes made, don't update to server
# make new JSON file with changes
# Want to be able to name canvas and save, if account associated with canvases can open
    # and save
# How to organize toolbar?
    # like it node-red, file name dropdown, classes, etc, search bar, this will happen 
    # after I can put the file into the UI
# add connector not really necessary
    
# update: make "methods" within a class readable