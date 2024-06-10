import tkinter as tk 
from Point import Point
from Oval import Oval
from LineSegment import LineSegment
from GUI import GUI
from DocumentModel import DocumentModel

   
def main():
   objects = [LineSegment(Point(80, 10), Point(10, 10)),Oval(Point(100,80),Point(60,120))]
   root = tk.Tk()
   model = DocumentModel()
   app = GUI(master=root,objects=objects,model=model)
   app.mainloop()
   
if __name__ == '__main__':
   main()