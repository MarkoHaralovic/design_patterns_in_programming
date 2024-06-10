from State import State
from Renderer import Renderer
from Point import Point
from GraphicalObject import GraphicalObject
from DocumentModel import DocumentModel

class SelectShapeState(State):
    def __init__(self, model: DocumentModel):
        self.model = model
        self.selected_objects = []

    def mouseDown(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
        clicked_object = self.model.find_selected_graphical_object(mousePoint)
        if not clicked_object:
            return
        if ctrlDown:
            if clicked_object in self.selected_objects:
                self.selected_objects.remove(clicked_object)
            else:
                self.selected_objects.append(clicked_object)
        else:
            self.selected_objects = [clicked_object]
        
        self.model.notify_listeners()  

    def afterDraw(self, r: Renderer):
        for obj in self.selected_objects:
            r.draw_rectangle(obj.getBoundingBox()) 
            if len(self.selected_objects) == 1:  
                for hot_point in obj.hot_points:
                    r.draw_point(hot_point)

    def keyPressed(self, keyCode: int):
        dx, dy = 0, 0
        if keyCode == 37:  # Left
            dx = -1
        elif keyCode == 38:  # Up
            dy = -1
        elif keyCode == 39:  # Right
            dx = 1
        elif keyCode == 40:  # Down
            dy = 1

        for obj in self.selected_objects:
            obj.translate(Point(dx, dy))  
        
        if keyCode == 107:  # Plus
            for obj in self.selected_objects:
                self.model.increase_z(obj)
        elif keyCode == 109:  # Minus
            for obj in self.selected_objects:
                self.model.decrease_z(obj)
        
        self.model.notify_listeners()

    def onLeaving(self):
        self.selected_objects = []
        self.model.notify_listeners()

    def mouseUp(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
        pass

    def mouseDragged(self, mousePoint: Point):
        pass
