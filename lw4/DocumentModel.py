from Point import Point
from Rectangle import Rectangle
from DocumentModelListener import DocumentModelListener
from GraphicalObject import GraphicalObject
from typing import List
from collections.abc import Sequence

class ReadOnlyList(Sequence):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)
     
class DocumentModel:
    SELECTION_PROXIMITY = 10

    def __init__(self):
        self._objects = []
        self._selected_objects = []
        self.listeners = []
    
    @property
    def objects(self):
        return ReadOnlyList(self._objects)
     
    @property
    def selected_objects(self):
        return ReadOnlyList(self._selected_objects)
     
    def add_graphical_object(self, obj: GraphicalObject):
        self._objects.append(obj)
        obj.addGraphicalObjectListener(self)
        self.notify_listeners("Added a new object")
        if obj.selected:
            self._selected_objects.append(obj)

    def remove_graphical_object(self, obj: GraphicalObject):
        if obj in self._objects:
            self._objects.remove(obj)
            obj.remove_listener(self)
            self.notify_listeners("Removed an object")
            if obj in self._selected_objects:
                self._selected_objects.remove(obj)

    def clear(self):
        for obj in self.objects[:]:
            self.remove_graphical_object(obj)
        self.notify_listeners("Cleared all objects")

    def list(self) -> List[GraphicalObject]:
        return self.objects.copy()

    def get_selected_objects(self) -> List[GraphicalObject]:
        return self.selected_objects.copy()

    def add_document_model_listener(self, listener: DocumentModelListener):
        if listener not in self.listeners:
            self.listeners.append(listener)

    def remove_document_model_listener(self, listener: DocumentModelListener):
        if listener in self.listeners:
            self.listeners.remove(listener)

    def notify_listeners(self, msg: str):
        for listener in self.listeners:
            listener.model_updated(self, msg)

    def find_selected_graphical_object(self, mouse_point: Point) -> GraphicalObject:
        closest, min_dist = None, float('inf')
        for obj in self._objects:
            print(f"Mouse point x : {mouse_point.getX()}")
            print(f"Mouse point y : {mouse_point.getY()}")
            print(f"Obj : {obj}")
            dist = obj.selectionDistance(mouse_point)
            if dist <= self.SELECTION_PROXIMITY and dist < min_dist:
                closest, min_dist = obj, dist
        print(f"Closest : {closest}")
        return closest

    def increase_z(self, obj: GraphicalObject):
        if obj in self.objects:
            index = self.objects.index(obj)
            if index < len(self.objects) - 1:
                self._objects[index], self._objects[index + 1] = self._objects[index + 1], self._objects[index]
                self.notify_listeners("Increased Z position")

    def decrease_z(self, obj: GraphicalObject):
        if obj in self.objects:
            index = self.objects.index(obj)
            if index > 0:
                self._objects[index], self._objects[index - 1] = self._objects[index - 1], self._objects[index]
                self.notify_listeners("Decreased Z position")
        
    def graphicalObjectChanged(self, obj: GraphicalObject):
        """Handle notifications that a graphical object has changed."""
        self.notify_listeners(f"Graphical object {obj} has changed.")
    