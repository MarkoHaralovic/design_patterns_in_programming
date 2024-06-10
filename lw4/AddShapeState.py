from State import State
from Renderer import Renderer
from Point import Point
from GraphicalObject import GraphicalObject
from DocumentModel import DocumentModel

class AddShapeState(State):
   def __init__(self,model:DocumentModel,prototype:GraphicalObject):
      self.model = model
      self.prototype = prototype
      
   def mouseDown(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
        new_object = self.prototype.duplicate()
        self.adjustObjectPosition(new_object, mousePoint)
        self.model.add_graphical_object(new_object)
        print("Added new object at:", mousePoint)
        
   def adjustObjectPosition(self, obj, new_position):
       if hasattr(obj, 'translate'):
            delta = new_position.difference(obj.getHotPoint(0))
            obj.translate(delta)    
   
   def mouseUp(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
      pass

   def mouseDragged(self, mousePoint: Point):
      pass

   def keyPressed(self, keyCode: int): 
      pass

   def afterDraw(self, r: Renderer, go: GraphicalObject):
      pass

   def afterDraw(self, r: Renderer):
      pass

   def onLeaving(self):
      pass