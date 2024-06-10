from abc import ABC,abstractmethod
from typing import List
from GraphicalObject import GraphicalObject

class GraphicalObjectListener(ABC):
   @abstractmethod
   def graphicalObjectChanged(self, go:GraphicalObject) -> None:
      """Notify the listener that the specified graphical object has changed"""
      raise NotImplementedError
   @abstractmethod
   def graphicalObjectSelectionChanged(self, go:GraphicalObject) -> None:
      """Notify the listener that the specified graphical object's selection state has changed"""
      raise NotImplementedError