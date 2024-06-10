import tkinter as tk 
from TkRendererImpl import TkRendererImpl
from IdleState import IdleState
from Point import Point

class GUI(tk.Frame):
   def __init__(self, master=None,objects=None):
      super().__init__(master)
      self.currentState = IdleState()
      self.master = master
      self.pack()
      self.objects = objects
      self.canvas = tk.Canvas(self, width=400, height=400)
      self.canvas.pack()
      self.renderer = TkRendererImpl(self.canvas)
            
      self.canvas.bind("<Button-1>", self.onMouseDown)
      self.canvas.bind("<B1-Motion>", self.onMouseDrag)
      self.canvas.bind("<ButtonRelease-1>", self.onMouseUp)
      self.master.bind("<KeyPress>", self.onKeyPress)
      
      self.draw_objects()
   
   def draw_objects(self):
        for obj in self.objects:
            obj.render(self.renderer)
            
   def clear_canvas(self):
        self.canvas.delete("all")     
               
   def setVisible(self,visible:bool) -> None:
      if visible:
         self.draw_objects()
      else:
         self.clear_canvas()
      
   def onMouseDown(self, event):
        shift_down = bool(event.state & 0x01)  
        ctrl_down = bool(event.state & 0x04) 
        self.currentState.mouseDown(Point(event.x, event.y), shift_down, ctrl_down)
        
   def onMouseDrag(self, event):
      self.currentState.mouseDragged(Point(event.x, event.y))

   def onMouseUp(self, event):
        shift_down = bool(event.state & 0x01) 
        ctrl_down = bool(event.state & 0x04)
        self.currentState.mouseUp(Point(event.x, event.y), shift_down, ctrl_down)
        
   def onKeyPress(self, event):
      if event.keysym == 'Escape':
         self.currentState.onLeaving()
         self.currentState = IdleState()
      else:
         self.currentState.keyPressed(event.keycode)
      