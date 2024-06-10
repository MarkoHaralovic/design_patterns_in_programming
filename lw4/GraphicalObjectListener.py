from abc import ABC,abstractmethod
from typing import List
from .GraphicalObject import GraphicalObject

class GraphicalObjectListener(ABC):
   @abstractmethod
   def graphicalObjectChanged(self, go:GraphicalObject) -> None:
      """Notify the listener that the specified graphical object has changed"""
      pass
   @abstractmethod
   def graphicalObjectSelectionChanged(self, go:GraphicalObject) -> None:
      """Notify the listener that the specified graphical object's selection state has changed"""
      pass