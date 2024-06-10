import tkinter as tk 
from TkRendererImpl import TkRendererImpl

class GUI(tk.Frame):
   def __init__(self, master=None,objects=None):
      super().__init__(master)
      self.master = master
      self.pack()
      self.objects = objects
      self.canvas = tk.Canvas(self, width=400, height=400)
      self.canvas.pack()
      self.renderer = TkRendererImpl(self.canvas)
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
      