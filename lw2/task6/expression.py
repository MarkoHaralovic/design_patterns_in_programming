import ast
import re 
class ExpressionEvaluator:
    def __init__(self, sheet):
        self.sheet = sheet

    def parse_expression(self, expression, operators=False):
        if not operators:
            pattern = r'A\d+|\d+'
        else:
            pattern = r'A\d+|\d+|\+'
        return re.findall(pattern, expression)

    def eval_expression(self, expression):
        def _eval(node):
            if isinstance(node, ast.Num):
                return node.n
            elif isinstance(node, ast.Name):
                cell = self.sheet.cell(node.id)
                return cell.value if cell and cell.value is not None else 0
            elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
                return _eval(node.left) + _eval(node.right)
            else:
                raise Exception('Unsupported type {}'.format(node))
        node = ast.parse(expression, mode='eval')
        return _eval(node.body)