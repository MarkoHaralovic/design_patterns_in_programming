from abc import ABC, abstractmethod
from typing import List
from .Point import Point

class Renderer(ABC):
    @abstractmethod
    def draw_line(self, s: Point, e: Point) -> None:
        """
        Draw a line from point s to point e.
        """
        pass

    @abstractmethod
    def fill_polygon(self, points: List[Point]) -> None:
        """
        Fill a polygon defined by a list of points.
        """
        pass
