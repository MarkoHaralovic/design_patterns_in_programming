from abc import ABC,abstractmethod

class EditAction(ABC):
    @abstractmethod
    def execute_do(self):
        raise NotImplementedError("Subclasses should implement this!")
    @abstractmethod
    def execute_undo(self):
        raise NotImplementedError("Subclasses should implement this!")
