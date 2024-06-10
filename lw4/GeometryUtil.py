from abc import ABC,abstractmethod
from Point import Point
from Rectangle import Rectangle
import math

class GeometryUtil:
   def distanceFromPoint(point1: Point, point2: Point) ->float:
      return math.sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
   
   def distanceFromLineSegment(s:Point,e:Point,p:Point) ->float:
      length_square = (e.x - s.x) ** 2 + (e.y - s.y) ** 2
      if length_square == 0:
         return GeometryUtil.distanceFromPoint(s, p)
      t = ((p.x - s.x) * (e.x - s.x) + (p.y - s.y) * (e.y - s.y)) / length_square
      t = max(0, min(1, t)) 
      
      closest = Point(s.x + t * (e.x - s.x), s.y + t * (e.y - s.y))
      
      return GeometryUtil.distanceFromPoint(p, closest)  
   