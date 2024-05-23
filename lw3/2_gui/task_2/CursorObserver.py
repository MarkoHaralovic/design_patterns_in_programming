from abc import ABC,abstractmethod
class CursorObserver(ABC):
    @abstractmethod
    def updateCursorLocation(self, loc):
        pass
