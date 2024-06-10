from State import State
from GraphicalObject import GraphicalObject
from Point import Point
from Renderer import Renderer

class IdleState(State):
      def mouseDown(self,mousePoint,shiftDown,ctrlDown):
         pass
      def mouseUp(self, mousePoint: Point, shiftDown: bool, ctrlDown: bool) -> None:
        pass
      def mouseDragged(self, mousePoint: Point) -> None:
         pass
      def keyPressed(self, keyCode: int) -> None:
         pass
      def afterDraw(r: Renderer, go: GraphicalObject) -> None:
         pass
      def afterDraw(r: Renderer):
         pass
      def onLeaving(self) -> None:
         pass
                    