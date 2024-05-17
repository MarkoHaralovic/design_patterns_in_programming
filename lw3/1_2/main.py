from asyncio import sleep
import os
from myfactory import myfactory
import logging
logging.basicConfig(level=logging.ERROR)

printGreeting = lambda pet: pet.printGreeting()
printMenu = lambda pet: pet.printMenu()

def test():
   pets=[]
   # obiđi svaku datoteku kazala plugins 
   for mymodule in os.listdir('plugins'):
      logging.info('mymodule: %s', mymodule)
      moduleName, moduleExt = os.path.splitext(mymodule)
      logging.info('moduleName: %s, moduleExt: %s', moduleName, moduleExt)
      # ako se radi o datoteci s Pythonskim kodom ...
      if moduleExt=='.py':
        # instanciraj ljubimca ...
        ljubimac=myfactory(moduleName)('Ljubimac '+str(len(pets)))
        # ... i dodaj ga u listu ljubimaca
        pets.append(ljubimac)

   # ispiši ljubimce
   for pet in pets:
     printGreeting(pet)
     printMenu(pet)
    
def main():
   test()
   
if __name__ == "__main__":
    main()