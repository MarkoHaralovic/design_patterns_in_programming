from abc import ABC, abstractmethod
from Point import Point
from Renderer import Renderer
from GraphicalObject import GraphicalObject

class State(ABC):
   @abstractmethod
   def mouseDown(self,mousePoint: Point,shiftDown:bool,ctrlDown:bool) -> None:
      """ Called when the program registers that the left mouse button is pressed """
      raise NotImplementedError
   
   @abstractmethod
   def mouseUp(self,mousePoint: Point,shiftDown:bool,ctrlDown:bool) -> None:
      """ Called when the program registers that the left mouse button is released """
      raise NotImplementedError
   
   @abstractmethod
   def mouseDragged(self,mousePoint: Point) -> None:
      """ Called when the program registers that the user is moving the mouse while the button is pressed """
      raise NotImplementedError

   @abstractmethod
   def keyPressed(self,keyCode: int) -> None:
      """ Called when the program registers that the user clicked a key on the keyboard. """
      raise NotImplementedError

   @abstractmethod
   def afterDraw(self,r: Renderer,go:GraphicalObject) -> None:
      """ Called when GUI drew the object sent to draw."""
      raise NotImplementedError
   
   @abstractmethod
   def afterDraw(r: Renderer) -> None:
      """Called after the program finished drawing"""
      raise NotImplementedError
   
   @abstractmethod
   def onLeaving() -> None:
      """Called when the program is leaving this state, so it won'tenter another one."""
      raise NotImplementedError