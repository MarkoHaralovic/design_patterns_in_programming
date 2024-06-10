from Renderer import Renderer
from AbstractGraphicalObject import AbstractGraphicalObject
from Point import Point
from GeometryUtil import GeometryUtil
from Rectangle import Rectangle
from GraphicalObject import GraphicalObject
from typing import Tuple

class Oval(AbstractGraphicalObject):
   def __init__(self, right_point: Point = None, bottom_point: Point = None):
        if right_point is None:
            right_point = Point(10, 0)
        if bottom_point is None:
            bottom_point = Point(0, 10)

        super().__init__(hotPoints=[right_point, bottom_point], hotPointSelected=[False, False], selected=False, listeners=[])
        self.right_point = right_point
        self.bottom_point = bottom_point
        
   def selectionDistance(self, mouse_point: Point) -> float:
      return GeometryUtil.distanceFromLineSegment(self.right_point,self.bottom_point,mouse_point) 
     
   def getShapeName(self) -> str:
      return "Oval"
   
   def getBoundingBox(self) -> Rectangle:
        minX = min(self.right_point.x, self.bottom_point.x)
        maxX = max(self.right_point.x, self.bottom_point.x)
        minY = min(self.right_point.y, self.bottom_point.y)
        maxY = max(self.right_point.y, self.bottom_point.y)
        return Rectangle(minX, minY, maxX - minX, maxY - minY)
   
   def duplicate(self) -> 'GraphicalObject':
      return Oval(self.right_point, self.bottom_point)
   
   def render(self, renderer: Renderer) -> None:
      bounding_box = (self.right_point.x - abs(self.right_point.x - self.bottom_point.x),
                        self.right_point.y - abs(self.right_point.y - self.bottom_point.y),
                        self.right_point.x + abs(self.right_point.x - self.bottom_point.x),
                        self.right_point.y + abs(self.right_point.y - self.bottom_point.y))
      renderer.draw_oval(bounding_box)