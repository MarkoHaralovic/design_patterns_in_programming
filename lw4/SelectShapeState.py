from State import State
from Renderer import Renderer
from Point import Point
from GraphicalObject import GraphicalObject
from DocumentModel import DocumentModel
from GeometryUtil import GeometryUtil
from CompositeShape import CompositeShape

class SelectShapeState(State):
    def __init__(self, model: DocumentModel):
        self.model = model
        self.selected_objects = []
        self.dragging = False
        self.dragged_hot_point_index = None

    def mouseDown(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
        if not ctrlDown and len(self.selected_objects) == 1:
            clicked_object = self.selected_objects[0]
            for i in range(clicked_object.getNumberOfHotPoints()):
                if GeometryUtil.distanceFromPoint(clicked_object.getHotPoint(i),mousePoint) < DocumentModel.SELECTION_PROXIMITY:
                    self.dragging = True
                    self.dragged_hot_point_index = i
                    return  
        
        clicked_object = self.model.find_selected_graphical_object(mousePoint)
        if clicked_object:
            if ctrlDown:
                if clicked_object in self.selected_objects:
                    self.selected_objects.remove(clicked_object)
                else:
                    self.selected_objects.append(clicked_object)
            else:
                self.selected_objects = [clicked_object]
            
            self.model.notify_listeners(clicked_object.getShapeName())
               
    def mouseDragged(self, mousePoint: Point):
        if self.dragging and self.dragged_hot_point_index is not None:
            obj = self.selected_objects[0]
            obj.setHotPoint(self.dragged_hot_point_index, mousePoint)
            self.model.notify_listeners()

    def mouseUp(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool):
        self.dragging = False
        self.dragged_hot_point_index = None

    def afterDraw(self, r: Renderer):
        print("AfterDraw")
        for obj in self.selected_objects:
            bbox = obj.getBoundingBox()
            
            points = [
            Point(bbox.getX(), bbox.getY()),  
            Point(bbox.getX() + bbox.getWidth(), bbox.getY()),  
            Point(bbox.getX() + bbox.getWidth(), bbox.getY() + bbox.getHeight()),  
            Point(bbox.getX(), bbox.getY() + bbox.getHeight())  
        ]
            r.fill_polygon(points)
            
            if len(self.selected_objects)==1:
                r.draw_point(Point(bbox.getX(), bbox.getY()))
                r.draw_point(Point(bbox.getX() + bbox.getWidth(), bbox.getY() + bbox.getHeight()))

    def keyPressed(self, keyCode: int):
        if keyCode == ord('G'):
            self.group_selected_objects()
        elif keyCode == ord('U'):
            self.ungroup_selected_objects()
            
        dx, dy = 0, 0
        if keyCode in [37, 38, 39, 40]:  
            dx = (keyCode == 39) - (keyCode == 37)  
            dy = (keyCode == 38) - (keyCode == 40)  
            for obj in self.selected_objects:
                obj.translate(Point(dx, dy))
        
        if keyCode == 107:  # Plus 
            for obj in self.selected_objects:
                self.model.increase_z(obj)
        elif keyCode == 109:  # Minus 
            for obj in self.selected_objects:
                self.model.decrease_z(obj)
                self.model.notify_listeners(obj.getShapeName())

    def onLeaving(self):
        self.selected_objects = []
        self.model.notify_listeners()
        
    def group_selected_objects(self):
        if not self.selected_objects:
            return
        composite = CompositeShape(self.selected_objects)
        for obj in self.selected_objects:
            self.model.remove_graphical_object(obj)
        self.model.add_graphical_object(composite)
        self.selected_objects = [composite]

    def ungroup_selected_objects(self):
        if len(self.selected_objects) == 1 and isinstance(self.selected_objects[0], CompositeShape):
            composite = self.selected_objects[0]
            children = composite.children
            self.model.remove_graphical_object(composite)
            for child in children:
                self.model.add_graphical_object(child)
            self.selected_objects = children

