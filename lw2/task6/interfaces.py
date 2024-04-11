from abc import ABC, abstractmethod

class IObservable(ABC):
   @abstractmethod
   def add_observer(self, observer):
      pass
   @abstractmethod
   def remove_observer(self, observer):
      pass
   @abstractmethod
   def notify_observers(self):
      pass

class IObserver(ABC):
   @abstractmethod
   def update_value(self,*args):
      pass  