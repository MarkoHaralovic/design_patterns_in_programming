class Parrot:
    def __init__(self, name):
        self._name = name

    def printGreeting(self):
        print("Ja sam opasni, crveni papagaj!")

    def printMenu(self):
        print("Volim orahe!")

    def name(self):
        return str(self._name)