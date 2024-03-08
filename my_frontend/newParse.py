import ast
import json

# class ClassFunctionVisitor(ast.NodeVisitor):
#     def __init__(self):
#         self.output_file = open("/Users/haileywallace/Desktop/orb_dev/Orb24/my_frontend/text.txt", "w")
#         self.in_class = False
#         self.function_nesting_level = 0

#     def visit_ClassDef(self, node):
#         self.in_class = True
#         print(f'Class: {node.name}')
#         self.output_file.write(f'Class: {node.name} \n')
#         # self.output_file.write('---\n')
#         self.generic_visit(node)
#         self.in_class = False
#         print('---')  # Separator between classes

#     def visit_FunctionDef(self, node):
#         if self.in_class:
#             prefix = '  Method' if self.function_nesting_level == 0 else '    Nested Function'
#             args = [arg.arg for arg in node.args.args]
#             print(f'  Nested Function: {node.name}')
#             self.output_file.write(f'   Nested Function: {node.name} \n')
#             self.output_file.write(f'       Arguments: {args} \n')
#         else:
#             prefix = 'Function' if self.function_nesting_level == 0 else '  Nested Function'
#             args = [arg.arg for arg in node.args.args]
#             print(f'Function: {node.name}')
#             self.output_file.write(f'Function: {node.name} \n')
#             self.output_file.write(f'       Arguments: {args} \n')

#         print(f'{prefix} (Level {self.function_nesting_level}): {node.name}')
#         # self.output_file.write(f'{prefix} (Level {self.function_nesting_level}): {node.name}')

#         # args = [arg.arg for arg in node.args.args]
#         # print(f'  Arguments: {args}')
#         # self.output_file.write(f'   Arguments: {args} \n')

#         self.function_nesting_level += 1
#         self.generic_visit(node)
#         self.function_nesting_level -= 1


# # need to update to account for nested functions

# def extract_classes_functions(filename):
#     with open(filename, 'r') as file:
#         tree = ast.parse(file.read(), filename=filename)
#     visitor = ClassFunctionVisitor()
#     visitor.visit(tree)

# if __name__ == '__main__':
#     extract_classes_functions('/Users/haileywallace/Desktop/Brain Child/linear_algebra.py')

# -------------------


# class ClassFunctionVisitor(ast.NodeVisitor):
#     def __init__(self):
#         self.dictionary1 = dict()
#         self.output_file = open("/Users/haileywallace/Desktop/orb_dev/Orb24/my_frontend/text.txt", "w")
#         self.in_class = False
#         self.function_nesting_level = 0

#     def visit_ClassDef(self, node):
#         self.in_class = True
#         self.dictionary2 = dict()
#         print(f'Class: {node.name}')
#         self.dictionary2["class:"] = node.name
#         self.generic_visit(node)
#         self.in_class = False

#     def visit_FunctionDef(self, node):
#         if self.in_class:
#             prefix = '  Method' if self.function_nesting_level == 0 else '    Nested Function'
#             args = [arg.arg for arg in node.args.args]
#             print(f'  Nested Function: {node.name}')
#             self.output_file.write(f'   Nested Function: {node.name} \n')
#             self.dictionary["nested function:"] = {node.name}
#             self.output_file.write(f'       Arguments: {args} \n')
#             self.dictionary["arguments:"] = {i for i in args}
#         else:
#             prefix = 'Function' if self.function_nesting_level == 0 else '  Nested Function'
#             args = [arg.arg for arg in node.args.args]
#             print(f'Function: {node.name}')
#             self.dictionary3 = dict()
#             self.output_file.write(f'Function: {node.name} \n')
#             self.dictionary3["function:"] = {node.name}
#             self.output_file.write(f'       Arguments: {args} \n')
#             self.dictionary3["arguments"] = {i for i in args}

#         print(f'{prefix} (Level {self.function_nesting_level}): {node.name}')
#         # self.output_file.write(f'{prefix} (Level {self.function_nesting_level}): {node.name}')

#         # args = [arg.arg for arg in node.args.args]
#         # print(f'  Arguments: {args}')
#         # self.output_file.write(f'   Arguments: {args} \n')

#         self.function_nesting_level += 1
#         self.generic_visit(node)
#         self.function_nesting_level -= 1
#         newdict = self.dictionary1 | self.dictionary2 | self.dictionary3
#         print(newdict)


# # need to update to account for nested functions

# def extract_classes_functions(filename):
#     with open(filename, 'r') as file:
#         tree = ast.parse(file.read(), filename=filename)
#     visitor = ClassFunctionVisitor()
#     visitor.visit(tree)

# if __name__ == '__main__':
#     extract_classes_functions('/Users/haileywallace/Desktop/Brain Child/linear_algebra.py')


class ClassFunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.result_dict = {}
        self.current_class = None
        self.function_nesting_level = 0

    def visit_ClassDef(self, node):
        self.current_class = node.name
        self.result_dict[node.name] = {"type": "class", 'methods': {}} # update method?
        # classdict = {"type": "class", "name": node.name, "methods": {}}
        # self.result_dict.update(classdict)
        self.generic_visit(node)
        self.current_class = None

    def visit_FunctionDef(self, node):
        args = [arg.arg for arg in node.args.args]
        function_info = {"type": "function", 'arguments': args, 'level': self.function_nesting_level}
        if self.current_class:
            self.result_dict[self.current_class]['methods'][node.name] = function_info
        else:
            self.result_dict[node.name] = function_info

        self.function_nesting_level += 1
        self.generic_visit(node)
        self.function_nesting_level -= 1

def extract_classes_functions(filename):
    with open(filename, 'r') as file:
        tree = ast.parse(file.read(), filename=filename)
    visitor = ClassFunctionVisitor()
    visitor.visit(tree)
    # with open("result.json", "w") as fp:
    #     json.dump(visitor.result_dict, fp)
    return visitor.result_dict

if __name__ == '__main__':
    result = extract_classes_functions('/Users/haileywallace/Desktop/Brain Child/linear_algebra.py')
    with open('/Users/haileywallace/Desktop/orb_dev/Orb24/my_frontend/output.json', "w") as outfile:
        json.dump(result, outfile, indent = 4)
    print(result)