from abc import ABC, abstractmethod
from typing import List
from Point import Point
from GraphicalObject import GraphicalObject
from GraphicalObjectListener import GraphicalObjectListener

class AbstractGraphicalObject(GraphicalObject):
    def __init__(self, hotPoints: List[Point], hotPointSelected: List[bool], selected: bool, listeners: List[GraphicalObjectListener]):
        self.hotPoints = hotPoints
        self.hotPointSelected = hotPointSelected
        self.selected = selected
        self.listeners = listeners

    def getHotPoint(self, index: int) -> Point:
        if index < 0 or index >= len(self.hotPoints):
            raise IndexError("Index out of range")
        return self.hotPoints[index]

    def setHotPoint(self, index: int, point: Point) -> None:
        if index < 0 or index >= len(self.hotPoints):
            raise IndexError("Index out of range")
        self.hotPoints[index] = point
        self.notifyListeners()

    def getNumberOfHotPoints(self) -> int:
        return len(self.hotPoints)

    def getHotPointDistance(self, index: int, mouse_point: Point) -> float:
        if index < 0 or index >= len(self.hotPoints):
            raise IndexError("Index out of range")
        return self.hotPoints[index].difference(mouse_point)

    def isHotPointSelected(self, index: int) -> bool:
        if index < 0 or index >= len(self.hotPointSelected):
            raise IndexError("Index out of range")
        return self.hotPointSelected[index]

    def setHotPointSelected(self, index: int, selected: bool) -> None:
        if index < 0 or index >= len(self.hotPointSelected):
            raise IndexError("Index out of range")
        self.hotPointSelected[index] = selected
        self.notifyListeners()

    def isSelected(self) -> bool:
        return self.selected

    def setSelected(self, selected: bool) -> None:
        self.selected = selected
        self.notifySelectionListeners()

    def translate(self, delta: Point) -> None:
        for i in range(len(self.hotPoints)):
            self.hotPoints[i] = self.hotPoints[i].translate(delta)
        self.notifyListeners()

    def addGraphicalObjectListener(self, listener) -> None:
        self.listeners.append(listener)

    def removeGraphicalObjectListener(self, listener) -> None:
        self.listeners.remove(listener)

    def notifyListeners(self) -> None:
        for listener in self.listeners:
            listener.graphicalObjectChanged(self)

    def notifySelectionListeners(self) -> None:
        for listener in self.listeners:
            listener.graphicalObjectSelectionChanged(self)
