from abc import ABC,abstractmethod
from typing import List
from .Point import Point
from .Rectangle import Rectangle
from .Renderer import Renderer
from .GraphicalObject import GraphicalObject

class GraphicalObject(ABC):

    @abstractmethod
    def isSelected(self) -> bool:
        """Check if the object is selected"""
        pass

    @abstractmethod
    def setSelected(self, selected: bool) -> None:
        """Set the object's selected state"""
        pass

    @abstractmethod
    def getNumberOfHotPoints(self) -> int:
        """Return the number of hot points"""
        pass

    @abstractmethod
    def getHotPoint(self, index: int) -> Point:
        """Get the hot point at the specified index"""
        pass

    @abstractmethod
    def setHotPoint(self, index: int, point: Point) -> None:
        """Set the hot point at the specified index"""
        pass

    @abstractmethod
    def isHotPointSelected(self, index: int) -> bool:
        """Check if the hot point at the specified index is selected"""
        pass

    @abstractmethod
    def setHotPointSelected(self, index: int, selected: bool) -> None:
        """Set the selected state of the hot point at the specified index"""
        pass

    @abstractmethod
    def getHotPointDistance(self, index: int, mouse_point: Point) -> float:
        """Calculate the distance from the hot point at the specified index to the mouse point"""
        pass

    @abstractmethod
    def translate(self, delta: Point) -> None:
        """Translate the object by the specified delta"""
        pass

    @abstractmethod
    def getBoundingBox(self) -> Rectangle:
        """Return the object's bounding box"""
        pass

    @abstractmethod
    def selectionDistance(self, mouse_point: Point) -> float:
        """Calculate the selection distance from the object to the mouse point"""
        pass

   #  @abstractmethod
   #  def render(self, renderer: Renderer) -> None:
   #      """Render the object using the given renderer"""
   #      pass

    @abstractmethod
    def addGraphicalObjectListener(self, listener) -> None:
        """Add a listener for graphical object changes"""
        pass

    @abstractmethod
    def removeGraphicalObjectListener(self, listener) -> None:
        """Remove a listener for graphical object changes"""
        pass

    @abstractmethod
    def getShapeName(self) -> str:
        """Get the name of the shape"""
        pass

    @abstractmethod
    def duplicate(self) -> 'GraphicalObject':
        """Create a duplicate of the graphical object"""
        pass

   #  @abstractmethod
   #  def getShapeID(self) -> str:
   #      """Get the identifier of the shape"""
   #      pass

   #  @abstractmethod
   #  def load(self, stack: List['GraphicalObject'], data: str) -> None:
   #      """Load the graphical object from data"""
   #      pass

   #  @abstractmethod
   #  def save(self, rows: List[str]) -> None:
   #      """Save the graphical object to rows"""
   #      pass