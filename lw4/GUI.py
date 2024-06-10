import tkinter as tk
from TkRendererImpl import TkRendererImpl
from IdleState import IdleState
from Point import Point
from tkinter import Button
from AddShapeState import AddShapeState

class GUI(tk.Frame):
    def __init__(self, master=None, objects=None, model=None):
        super().__init__(master)
        self.currentState = IdleState()
        self.master = master
        self.model = model
        self.pack()
        
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side='top', fill='x')  

        self.objects = objects
        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack(fill='both', expand=True)  
        
        self.renderer = TkRendererImpl(self.canvas)
        
        for obj in objects:
            button = Button(self.button_frame, text=obj.getShapeName(), command=lambda o=obj: self.setAddShapeState(o))
            button.pack(side='left')  

        self.canvas.bind("<Button-1>", self.onMouseDown)

    def setAddShapeState(self, prototype):
        print("Switching to AddShapeState with prototype:", prototype.getShapeName())
        self.currentState = AddShapeState(self.model, prototype)

    def onMouseDown(self, event):
        shift_down = bool(event.state & 0x01)
        ctrl_down = bool(event.state & 0x04)
        self.currentState.mouseDown(Point(event.x, event.y), shift_down, ctrl_down)
        self.refreshCanvas()

    def refreshCanvas(self):
        self.canvas.delete("all")
        for obj in self.model.objects:
            obj.render(self.renderer)
