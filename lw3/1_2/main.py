import os
from myfactory import myfactory
import logging

logging.basicConfig(level=logging.ERROR)

printGreeting = lambda pet: pet.printGreeting()
printMenu = lambda pet: pet.printMenu()
printName = lambda pet: print(pet.name())

def test():
    pets = []
    # Iterate over each file in the plugins directory
    for mymodule in os.listdir('plugins'):
        logging.info('mymodule: %s', mymodule)
        moduleName, moduleExt = os.path.splitext(mymodule)
        logging.info('moduleName: %s, moduleExt: %s', moduleName, moduleExt)
        # If it's a Python file...
        if moduleExt == '.py':
            # Instantiate the pet...
            try:
                PetClass = myfactory(moduleName)
                ljubimac = PetClass('Ljubimac ' + str(len(pets)))
                # ... and add it to the list of pets
                pets.append(ljubimac)
            except Exception as e:
                logging.error('Failed to create instance for %s: %s', moduleName, e)

    # Print the pets
    for pet in pets:
        printName(pet)
        printGreeting(pet)
        printMenu(pet)

def main():
    test()

if __name__ == "__main__":
    main()
