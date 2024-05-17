from EditAction import EditAction
from collections import deque

class UndoManagerObserver:
    def updateUndoRedoStatus(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class UndoManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UndoManager, cls).__new__(cls)
            cls._instance.undoStack = deque()
            cls._instance.redoStack = deque()
            cls._instance.observers = []
        return cls._instance

    def push(self, action: EditAction):
        self.redoStack.clear()
        self.undoStack.append(action)
        self.notifyObservers()

    def undo(self):
        if self.undoStack:
            action = self.undoStack.pop()
            action.execute_undo()
            self.redoStack.append(action)
            self.notifyObservers()

    def redo(self):
        if self.redoStack:
            action = self.redoStack.pop()
            action.execute_do()
            self.undoStack.append(action)
            self.notifyObservers()

    def registerObserver(self, observer: UndoManagerObserver):
        if observer not in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer: UndoManagerObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.updateUndoRedoStatus()

    def can_undo(self):
        return bool(self.undoStack)

    def can_redo(self):
        return bool(self.redoStack)
