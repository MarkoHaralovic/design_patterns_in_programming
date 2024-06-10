import tkinter as tk 
from Point import Point
from Oval import Oval
from LineSegment import LineSegment
from GUI import GUI

   
def main():
   objects = [LineSegment(Point(80, 10), Point(10, 10)),Oval((100,80),(60,120)),
              LineSegment(Point(230, 50), Point(40, 90)),Oval((40,80),(60,120))]
   root = tk.Tk()
   app = GUI(master=root,objects=objects)
   app.setVisible(True)
   app.mainloop()
   
if __name__ == '__main__':
   main()