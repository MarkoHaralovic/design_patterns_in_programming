class Point:
   def __init__(self, x: float, y: float):
       self.x = x
       self.y = y
   def getX(self):
       return self.x
    
   def getY(self):
       return self.y
    
   def translate(self,dp:'Point')->'Point':
      return Point(self.getX()+dp.getX(), self.y+dp.getY())
   
   def difference(self,p:'Point')->'Point':
       print(self)
       print(p)
       return Point(self.getX()-p.getX(), self.getY()-p.getY())
   