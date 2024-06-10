from Renderer import Renderer
from AbstractGraphicalObject import AbstractGraphicalObject
from Point import Point
from GeometryUtil import GeometryUtil
from Rectangle import Rectangle
from GraphicalObject import GraphicalObject

class LineSegment(AbstractGraphicalObject):
   def __init__(self, start_point: Point = None, end_point: Point = None):
        if start_point is None or end_point is None:
            start_point = Point(0, 0)
            end_point = Point(10, 0)
        super().__init__(hotPoints=[start_point, end_point], hotPointSelected=[False, False], selected=False, listeners=[])
        self.start_point = start_point
        self.end_point = end_point
        
   def selectionDistance(self, mouse_point: Point) -> float:
      return GeometryUtil.distanceFromLineSegment(self.start_point,self.end_point,mouse_point) 
     
   def getShapeName(self) -> str:
      return "Line"
   
   def getBoundingBox(self) -> Rectangle:
        minX = min(self.start_point.x, self.end_point.x)
        maxX = max(self.start_point.x, self.end_point.x)
        minY = min(self.start_point.y, self.end_point.y)
        maxY = max(self.start_point.y, self.end_point.y)
        return Rectangle(minX, minY, maxX - minX, maxY - minY)
   
   def duplicate(self) -> 'GraphicalObject':
      return LineSegment(self.start_point,self.end_point)
   
   def render(self, renderer: Renderer) -> None:
       return renderer.draw_line(self.start_point, self.end_point)