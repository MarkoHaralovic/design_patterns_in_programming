import re

def parse_expression(expression, operators=False):
    print(f"In parse expression, dealing with this expression: {expression}")
    if not operators:
        pattern = r'A\d+|\d+'
    else:
        pattern = r'A\d+|\d+|\+'
    matches = re.findall(pattern, expression)
    print(f"Matches: {matches}")
    return matches

parse_expression('2+A3',operators=True)
