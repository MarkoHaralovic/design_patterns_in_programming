from abc import ABC,abstractmethod

class Plugin(ABC):
    @abstractmethod
    def get_name(self):
        raise NotImplementedError
    
    @abstractmethod
    def get_description(self):
        raise NotImplementedError
    
    @abstractmethod 
    def execute(self, model, undo_manager, clipboard_stack):
        raise NotImplementedError
