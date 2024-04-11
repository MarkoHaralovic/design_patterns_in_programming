import numpy as np 
import re  
import sys
import ast

class CircularDefinitionError(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)
        
def parse_expression(expression, operators=False):
    if not operators:
        pattern = r'A\d+|\d+'
    else:
        pattern = r'A\d+|\d+|\+'
    matches = re.findall(pattern, expression)
    return matches
    
class Cell :
   def __init__(self,sheet,id):
      self.id = id
      self.observers = [] 
      self.exp = None
      self.value = None  
      self._Sheet = sheet
   def add_observer(self,observer):
      self.observers.append(observer)
   def notify_observers(self):
      for observer in self.observers:
         self._Sheet.evaluate(observer.id)
   def update_value(self,value):
      self.value = value
      self.notify_observers()
      
class Sheet:
   def __init__(self,width,height):
      self._sheet = [[Cell(self,f"A{y*width+x+1}") for x in range(width)] for y in range(height)]
      self.width,self.height = width,height
      
   def cell(self,ref):
      for w in range(self.width):
         for y in range(self.height):
            if self._sheet[w][y].id == ref:
               return self._sheet[w][y] if self._sheet[w][y]  is not None else print("No cell with ref :{ref}")
            
   def set(self,cell_id,exp):
      cell = self.cell(cell_id)
      cell.exp = exp
      value = self.evaluate(cell_id)
      cell.update_value(value)
      for tracked_cell_id in self.getrefs(cell_id):
         tracked_cell = self.cell(tracked_cell_id)
         if tracked_cell:
            tracked_cell.add_observer(self.cell(cell_id))
   def getrefs(self,cell_id):
      cell = self.cell(cell_id)
      expression = cell.exp
      referenced_cells = parse_expression(expression,operators=False)
      return referenced_cells
   
   def eval_expression(self, expression):
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Name):
            cell = self.cell(node.id)
            return cell.value if cell and cell.value is not None else 0
        elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return _eval(node.left) + _eval(node.right)
        else:
            raise Exception('Unsupported type {}'.format(node))
    node = ast.parse(expression, mode='eval')
    return _eval(node.body)
 
   def evaluate(self, cell_id):
        cell = self.cell(cell_id)
        expression_ = parse_expression(cell.exp, operators=True)
        try:
           self.detect_circular_reference(cell_id,expression_)
        except CircularDefinitionError as e:
           print(e.message)
           sys.exit(1)
        formula = []
        all_cells_ready = True
        for part in expression_:
            if part.isdigit():
                formula.append(part)
            elif part != '+':
                referenced_cell = self.cell(part)
                if referenced_cell.value is not None:
                   formula.append(str(referenced_cell.value))
                elif referenced_cell.value is None and referenced_cell:
                   all_cells_ready = False
                   break
                elif referenced_cell:
                    exp_ = parse_expression(referenced_cell.exp, operators=True)
                    if cell_id in exp_:
                        raise CircularDefinitionError("Circular reference detected")
                    else:
                        formula.append(str(self.evaluate(part)))
        if not all_cells_ready:
           return None 
        cell.value = self.eval_expression('+'.join(formula))
        cell.notify_observers()
        return cell.value
   def detect_circular_reference(self, original_cell_id, expression, visited=None):
        if visited is None:
            visited = set()

        for exp_part in expression:
            if exp_part.isdigit() or exp_part == '+':
                continue
            elif exp_part == original_cell_id:
                raise CircularDefinitionError(f"Circular reference detected: cell {original_cell_id} indirectly refers to itself in expression {expression}")
            elif exp_part not in visited:
                visited.add(exp_part)
                cell = self.cell(exp_part)
                if cell and cell.exp:
                    cell_exp = parse_expression(cell.exp, operators=True)
                    self.detect_circular_reference(original_cell_id, cell_exp, visited)
            
   def print(self):
      for w in range(self.width):
         for y in range(self.height):
            print(f"Cell id : {self._sheet[w][y].id}, cell value : {self._sheet[w][y].value}")
              
if __name__=="__main__":
  s=Sheet(5,5)
  print()

  s.set('A1','A2')
  s.set('A2','A5')
  s.set('A3','A1+A2')
  s.set('A5','2')
  s.print()
  print()

  s.set('A1','4')
  s.set('A4','A1+A3')
  s.set('A6','10')
  s.print()
  print()

  s.set('A1','A3')
  s.print()
  print()