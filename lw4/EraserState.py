from State import State
from Point import Point
from GeometryUtil import GeometryUtil
class EraserState(State):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.path = []

    def mouseDown(self, mousePoint, shiftDown, ctrlDown):
        self.path = [mousePoint]

    def mouseDragged(self, mousePoint):
        self.path.append(mousePoint)
        self.model.refreshCanvas()  # This should trigger the GUI to redraw including the afterDraw

    def mouseUp(self, mousePoint):
        self.path.append(mousePoint)
        self.erase_objects()
        self.path = []
        self.model.refreshCanvas()

    def erase_objects(self):
        objects_to_remove = [obj for obj in self.model.objects if self.intersects(obj)]
        for obj in objects_to_remove:
            self.model.remove_graphical_object(obj)

    def intersects(self, obj):
        for point in self.path:
           bbox = obj.getBoundingBox()
            
           points = [
               Point(bbox.getX(), bbox.getY()),  
               Point(bbox.getX() + bbox.getWidth(), bbox.getY()),  
               Point(bbox.getX() + bbox.getWidth(), bbox.getY() + bbox.getHeight()),  
               Point(bbox.getX(), bbox.getY() + bbox.getHeight())  
          ]
           for _point in points:
              if GeometryUtil.distanceFromPoint(_point, point) < 3:
                  return True
        return False

    def afterDraw(self, renderer):
        if self.path:
            renderer.draw_polyline(self.path)

    def keyPressed(self, keyCode):
        pass

    def onLeaving(self):
        pass
