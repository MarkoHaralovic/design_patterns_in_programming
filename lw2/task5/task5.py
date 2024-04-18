import watchdog , watchdog.events , watchdog.observers
from abc import ABC, abstractmethod
import time 
from datetime import datetime
import numpy as np
import os.path

SOURCE_FILE_PATH = "source.txt"
DESTINATION_FILE_PATH = "destination.txt"

class IzvorBrojeva(ABC):
   @abstractmethod
   def citaj_brojeve(self):
      pass
   
class Observer(ABC):
   @abstractmethod
   def on_change(self,*args,**kwargs):
      pass
      
      
class SlijedBrojeva():
   def __init__(self,stream,observers):
      self._number_collection = []
      self._stream = stream
      self.observers = observers
   def dodaj_promatraca(self,observer):
      self.observers.append(observer)
   def obavijesti_promatrace(self):
      for observer in self.observers:
         observer.on_change(self._number_collection)
   def metoda_kreni(self):
      try:
         while True:
            broj = self._stream.citaj_brojeve()
            if broj == -1:
               break
            self._number_collection.append(broj)
            self.obavijesti_promatrace()
            time.sleep(1)
      except KeyboardInterrupt:
         return
   
class TipkovnickiIzvor(IzvorBrojeva):
   def citaj_brojeve(self):
      return int(input("Unesite broj: "))

class DatoteckiIzvor(IzvorBrojeva):
   def __init__(self,file_path):
      self.line_num = 1
      self.file_path = file_path
      if not os.path.exists(self.file_path):
         with open(self.file_path, 'w') as f:
            pass
   def citaj_brojeve(self):
      line_count = 0
      with open(self.file_path,'r+') as file:
         for line in file:
            line_count+=1
            if line_count == self.line_num: 
               self.line_num+=1
               return int(line.strip())
      return
   
class LogData:
   def __init__(self,file_path):
      self.file_path = file_path
   def on_change(self,data):
      if self.file_path is None:
         raise Exception("File path not specified.")
      if not os.path.isfile(self.file_path):
         raise FileNotFoundError(f"File does not exists on the provided path : {self.path}")
      with open(self.file_path,'a') as file:
         for element in data:
            file.write(f"{element} - {datetime.now()}\n")

class DataSum(Observer):
   def on_change(self,data):
      print(f"Trenutna suma brojeva jest : {np.sum(data)}")
      
class DataMedian(Observer):
   def on_change(self,data):
      print(f"Trenutni medijan brojeva jest : {np.median(data)}")

class DataAverage(Observer):
   def on_change(self,data):
      print(f"Trenutni prosjek brojeva jest : {np.average(data)}")
      
      
def main():
   data_sum = DataSum()
   data_median = DataMedian()
   data_average = DataAverage()
   data_log = LogData(DESTINATION_FILE_PATH)
   
   tipkovnica= TipkovnickiIzvor()
   datotecni_izvor = DatoteckiIzvor(file_path = SOURCE_FILE_PATH)
   slijed_brojeva_tipkovnica = SlijedBrojeva(tipkovnica,[data_sum, data_median, data_average, data_log])
   slijed_brojeva_datoteka = SlijedBrojeva(datotecni_izvor,[data_sum, data_median, data_average, data_log])
   
   slijed_brojeva_tipkovnica.metoda_kreni()
   slijed_brojeva_datoteka.metoda_kreni()
   
if __name__ == "__main__":
   main()