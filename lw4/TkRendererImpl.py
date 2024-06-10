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
      self.canvas.create_polygon(point_list, outline="red", fill="")
      print(f"Filling polygon with points: {points}")
        
   def draw_oval(self, bounding_box):
        self.canvas.create_oval(bounding_box[0], bounding_box[1], bounding_box[2], bounding_box[3], fill="blue", outline="red")
        print(f"Drawing oval with bounding box: {bounding_box}")
        
   def draw_point(self, point, size=3, color='red'):
        self.canvas.create_oval(point.x - size, point.y - size, point.x + size, point.y + size, fill=color, outline=color)
        print(f"Drawing point at ({point.x}, {point.y})")
        
   def draw_polyline(self, points):
    if len(points) > 1:
        for i in range(1, len(points)):
            self.canvas.create_line(points[i-1].x, points[i-1].y, points[i].x, points[i].y, fill="red")
