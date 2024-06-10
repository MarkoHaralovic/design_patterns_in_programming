import tkinter as tk
from tkinter import filedialog
from TkRendererImpl import TkRendererImpl
from IdleState import IdleState
from Point import Point
from tkinter import Button
from AddShapeState import AddShapeState
from SelectShapeState import SelectShapeState
from EraserState import EraserState
from SVGRendererImpl import SVGRendererImpl

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

        self.setup_eraser_button() 
        self.setup_selection_button()
        self.setup_svg_export_button()
        
        self.canvas.bind("<Button-1>", self.onMouseDown)
        
        self.canvas.focus_set()
        self.canvas.bind("<KeyPress>", self.onKeyPress)
        
    def setAddShapeState(self, prototype):
        print("Switching to AddShapeState with prototype:", prototype.getShapeName())
        self.currentState = AddShapeState(self.model, prototype)
    
    def onKeyPress(self, event):
        self.currentState.keyPressed(event.keycode)
        self.refreshCanvas()
    
    def setup_eraser_button(self):
        eraser_button = Button(self.button_frame, text="Eraser", command=self.activate_eraser_state)
        eraser_button.pack(side="left")
        
    def setup_selection_button(self):
        select_button = Button(self.button_frame, text="Select", command=self.activate_select_state)
        select_button.pack(side="left") 
    
    def setup_svg_export_button(self):
        svg_export_button = tk.Button(self.button_frame, text="SVG Export", command=self.export_svg)
        svg_export_button.pack(side="left")
        
    def export_svg(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG files", "*.svg")])
        if file_path:
            renderer = SVGRendererImpl(file_path)
            for obj in self.model.objects:
                obj.render(renderer)
            renderer.close()
            print(f"Exported to {file_path}")
            
    def activate_select_state(self):
        print("Switching to SelectShapeState")
        self.currentState = SelectShapeState(self.model)
        
    def activate_eraser_state(self):
        self.currentState = EraserState(self.model)
        print("Switched to EraserState")
        
    def onMouseDown(self, event):
        shift_down = bool(event.state & 0x01)
        ctrl_down = bool(event.state & 0x04)
        self.currentState.mouseDown(Point(event.x, event.y), shift_down, ctrl_down)
        self.refreshCanvas()

    def refreshCanvas(self):
        self.canvas.delete("all")
        for obj in self.model.objects:
            obj.render(self.renderer)
        if hasattr(self.currentState, 'afterDraw'):
            self.currentState.afterDraw(self.renderer)
