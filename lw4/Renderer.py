from abc import ABC, abstractmethod
from typing import List
from Point import Point

class Renderer(ABC):
    @abstractmethod
    def draw_line(self, s: Point, e: Point) -> None:
        """
        Draw a line from point s to point e.
        """
        raise NotImplementedError

    @abstractmethod
    def fill_polygon(self, points: List[Point]) -> None:
        """
        Fill a polygon defined by a list of points.
        """
        raise NotImplementedError
    @abstractmethod
    def draw_oval(self, bounding_box):
        """
        Draw an oval with the given bounding box.
        """
        raise NotImplementedError
    @abstractmethod
    def draw_point(self,point):
        """
        Draw a point at the given point.
        """
        raise NotImplementedError