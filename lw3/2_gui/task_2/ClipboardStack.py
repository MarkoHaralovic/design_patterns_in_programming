class ClipboardObserver:
    def updateClipboard(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class ClipboardStack:
    def __init__(self):
        self.stack = []
        self.observers = []

    def push(self, text):
        self.stack.append(text)
        self.notifyObservers()

    def pop(self):
        if not self.isEmpty():
            text = self.stack.pop()
            self.notifyObservers()
            return text
        return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        return None

    def isEmpty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack = []
        self.notifyObservers()

    def registerObserver(self, observer: ClipboardObserver):
        if observer not in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer: ClipboardObserver):
        if observer in self.observers:
            self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.updateClipboard()
