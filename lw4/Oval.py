from .AbstractGraphicalObject import AbstractGraphicalObject
from .Point import Point
from .GeometryUtil import GeometryUtil
from .Rectangle import Rectangle
from .GraphicalObject import GraphicalObject
from typing import Tuple

class LineSegment(AbstractGraphicalObject):
   def __init__(self, right_point_pos: Tuple = None, bottom_point_pos: Tuple = None):
        if right_point_pos is None or bottom_point_pos is None:
            right_point = Point(10, 0)
            bottom_point = Point(0, 10)
        else:
           right_point = Point(right_point_pos[0], right_point_pos[1])
           bottom_point = Point(bottom_point_pos[0], bottom_point_pos[1])
           
        super().__init__(hotPoints=[right_point, bottom_point], hotPointSelected=[False, False], selected=False, listeners=[])
        self.right_point = right_point
        self.bottom_point = bottom_point
        
   def selectionDistance(self, mouse_point: Point) -> float:
      return GeometryUtil.distanceFromLineSegment(self.right_point,self.bottom_point,mouse_point) 
     
   def getShapeName(self) -> str:
      return "Line"
   
   def getBoundingBox(self) -> Rectangle:
        minX = min(self.right_point.x, self.bottom_point.x)
        maxX = max(self.right_point.x, self.bottom_point.x)
        minY = min(self.right_point.y, self.bottom_point.y)
        maxY = max(self.right_point.y, self.bottom_point.y)
        return Rectangle(minX, minY, maxX - minX, maxY - minY)
   
   def duplicate(self) -> 'GraphicalObject':
      return LineSegment(self.right_point,self.bottom_point)