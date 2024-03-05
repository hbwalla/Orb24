import ast

class ClassFunctionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.output_file = open("/Users/haileywallace/Desktop/orb_dev/Orb24/my_frontend/text.txt", "w")
        self.in_class = False
        self.function_nesting_level = 0

    def visit_ClassDef(self, node):
        self.in_class = True
        print(f'Class: {node.name}')
        self.output_file.write(f'Class: {node.name} \n')
        # self.output_file.write('---\n')
        self.generic_visit(node)
        self.in_class = False
        print('---')  # Separator between classes

    def visit_FunctionDef(self, node):
        if self.in_class:
            prefix = '  Method' if self.function_nesting_level == 0 else '    Nested Function'
            args = [arg.arg for arg in node.args.args]
            print(f'  Nested Function: {node.name}')
            self.output_file.write(f'   Nested Function: {node.name} \n')
            self.output_file.write(f'       Arguments: {args} \n')
        else:
            prefix = 'Function' if self.function_nesting_level == 0 else '  Nested Function'
            args = [arg.arg for arg in node.args.args]
            print(f'Function: {node.name}')
            self.output_file.write(f'Function: {node.name} \n')
            self.output_file.write(f'       Arguments: {args} \n')

        print(f'{prefix} (Level {self.function_nesting_level}): {node.name}')
        # self.output_file.write(f'{prefix} (Level {self.function_nesting_level}): {node.name}')

        # args = [arg.arg for arg in node.args.args]
        # print(f'  Arguments: {args}')
        # self.output_file.write(f'   Arguments: {args} \n')

        self.function_nesting_level += 1
        self.generic_visit(node)
        self.function_nesting_level -= 1


# need to update to account for nested functions

def extract_classes_functions(filename):
    with open(filename, 'r') as file:
        tree = ast.parse(file.read(), filename=filename)
    visitor = ClassFunctionVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    extract_classes_functions('/Users/haileywallace/Desktop/Brain Child/linear_algebra.py')


