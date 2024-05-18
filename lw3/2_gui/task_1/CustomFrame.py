#!/usr/bin/python

from tkinter import Tk, Canvas, Frame, BOTH, W

class CustomFrame(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Lyrics")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_line(10, 25, 200, 25)
        canvas.create_line(300, 35, 300, 200)
        canvas.create_text(30, 40, anchor=W, font="Purisa",text="Line number one.")
        canvas.create_text(30, 60, anchor=W, font="Purisa",text="Line number two.")
        canvas.pack(fill=BOTH, expand=1)
 
def main():
    root = Tk()
    ex = CustomFrame()
    root.geometry("420x250+300+300")
    root.bind('<Return>', lambda event: root.destroy())
    root.mainloop()


if __name__ == '__main__':
    main()