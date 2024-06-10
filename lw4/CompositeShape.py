from Rectangle import Rectangle
from GraphicalObject import GraphicalObject

class CompositeShape(GraphicalObject):
    def __init__(self, children=[]):
        super().__init__()
        self.children = children

    def getBoundingBox(self):
        if not self.children:
            return Rectangle(0, 0, 0, 0) 
         
        minX = minY = float('inf')
        maxX = maxY = float('-inf')
        for child in self.children:
            bbox = child.getBoundingBox()
            minX = min(minX, bbox.getX())
            minY = min(minY, bbox.getY())
            maxX = max(maxX, bbox.getX() + bbox.getWidth())
            maxY = max(maxY, bbox.getY() + bbox.getHeight())
        
        return Rectangle(minX, minY, maxX - minX, maxY - minY)

    def render(self, renderer):
        for child in self.children:
            child.render(renderer)

    def translate(self, delta):
        for child in self.children:
            child.translate(delta)

    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def getNumberOfHotPoints(self):
        return 0  

    def setHotPoint(self, index, point):
        pass  
