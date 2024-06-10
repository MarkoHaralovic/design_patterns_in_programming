from abc import ABC,abstractmethod
from typing import List
from Point import Point
from Rectangle import Rectangle
from Renderer import Renderer

class GraphicalObject(ABC):

    @abstractmethod
    def isSelected(self) -> bool:
        """Check if the object is selected"""
        raise NotImplementedError

    @abstractmethod
    def setSelected(self, selected: bool) -> None:
        """Set the object's selected state"""
        raise NotImplementedError

    @abstractmethod
    def getNumberOfHotPoints(self) -> int:
        """Return the number of hot points"""
        raise NotImplementedError

    @abstractmethod
    def getHotPoint(self, index: int) -> Point:
        """Get the hot point at the specified index"""
        raise NotImplementedError

    @abstractmethod
    def setHotPoint(self, index: int, point: Point) -> None:
        """Set the hot point at the specified index"""
        raise NotImplementedError

    @abstractmethod
    def isHotPointSelected(self, index: int) -> bool:
        """Check if the hot point at the specified index is selected"""
        raise NotImplementedError

    @abstractmethod
    def setHotPointSelected(self, index: int, selected: bool) -> None:
        """Set the selected state of the hot point at the specified index"""
        raise NotImplementedError

    @abstractmethod
    def getHotPointDistance(self, index: int, mouse_point: Point) -> float:
        """Calculate the distance from the hot point at the specified index to the mouse point"""
        raise NotImplementedError

    @abstractmethod
    def translate(self, delta: Point) -> None:
        """Translate the object by the specified delta"""
        raise NotImplementedError

    @abstractmethod
    def getBoundingBox(self) -> Rectangle:
        """Return the object's bounding box"""
        raise NotImplementedError

    @abstractmethod
    def selectionDistance(self, mouse_point: Point) -> float:
        """Calculate the selection distance from the object to the mouse point"""
        raise NotImplementedError

    @abstractmethod
    def render(self, renderer: Renderer) -> None:
        """Render the object using the given renderer"""
        raise NotImplementedError

    @abstractmethod
    def addGraphicalObjectListener(self, listener) -> None:
        """Add a listener for graphical object changes"""
        raise NotImplementedError

    @abstractmethod
    def removeGraphicalObjectListener(self, listener) -> None:
        """Remove a listener for graphical object changes"""
        raise NotImplementedError

    @abstractmethod
    def getShapeName(self) -> str:
        """Get the name of the shape"""
        raise NotImplementedError

    @abstractmethod
    def duplicate(self) -> 'GraphicalObject':
        """Create a duplicate of the graphical object"""
        raise NotImplementedError

   #  @abstractmethod
   #  def getShapeID(self) -> str:
   #      """Get the identifier of the shape"""
   #      raise NotImplementedError

   #  @abstractmethod
   #  def load(self, stack: List['GraphicalObject'], data: str) -> None:
   #      """Load the graphical object from data"""
   #      raise NotImplementedError

   #  @abstractmethod
   #  def save(self, rows: List[str]) -> None:
   #      """Save the graphical object to rows"""
   #      raise NotImplementedError