import tkinter as tk 
from Point import Point
from Oval import Oval
from LineSegment import LineSegment
from GUI import GUI
from DocumentModel import DocumentModel

   
def main():
   objects = [LineSegment(Point(80, 110), Point(30, 10)),Oval(Point(180,100),Point(150,80)),
              LineSegment(Point(40, 10), Point(20, 5)),Oval(Point(220,200),Point(180,120))
              ]
   root = tk.Tk()
   model = DocumentModel()
   app = GUI(master=root,objects=objects,model=model)
   app.mainloop()
   
if __name__ == '__main__':
   main()