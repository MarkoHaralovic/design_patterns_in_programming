from Renderer import Renderer
import tkinter as tk

class TkRendererImpl(Renderer):
   def __init__(self, canvas: tk.Canvas):
        self.canvas = canvas
        
   def draw_line(self, s, e):
      self.canvas.create_line(s.x, s.y, e.x, e.y, fill="blue")
      print(f"Drawing line from {s} to {e}")
      
   def fill_polygon(self, points):
      point_list = [(p.x, p.y) for p in points]
      self.canvas.create_polygon(point_list, fill="blue", outline="red")
      print(f"Filling polygon with points: {points}")
        
   def draw_oval(self, bounding_box):
        self.canvas.create_oval(bounding_box[0], bounding_box[1], bounding_box[2], bounding_box[3], fill="blue", outline="red")
        print(f"Drawing oval with bounding box: {bounding_box}")