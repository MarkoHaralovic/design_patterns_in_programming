#!/usr/bin/python

from TextEditor import TextEditor
from TextEditorModel import TextEditorModel
from tkinter import Tk, BOTH

def main():
    root = Tk()
    text = "Hello, World!\nThis is a simple text editor.\nEnjoy editing!"
    model = TextEditorModel(text)
    editor = TextEditor(model)
    editor.pack(fill=BOTH, expand=1)
    root.geometry("420x250+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()
