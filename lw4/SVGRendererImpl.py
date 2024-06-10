from Renderer import Renderer
import os

class SVGRendererImpl(Renderer):
    def __init__(self, file_name):
        self.file_name = file_name
        self.lines = []
        self.lines.append('<svg xmlns="http://www.w3.org/2000/svg" version="1.1">')

    def close(self):
        self.lines.append('</svg>')
        with open(self.file_name, 'w') as file:
            file.write('\n'.join(self.lines))

    def draw_line(self, s, e):
        line = f'<line x1="{s.x}" y1="{s.y}" x2="{e.x}" y2="{e.y}" stroke="blue" />'
        self.lines.append(line)

    def fill_polygon(self, points):
        point_str = ' '.join(f'{p.x},{p.y}' for p in points)
        polygon = f'<polygon points="{point_str}" style="stroke:red; fill:none;" />'
        self.lines.append(polygon)

    def draw_oval(self, bounding_box):
        cx = (bounding_box[0] + bounding_box[2]) / 2
        cy = (bounding_box[1] + bounding_box[3]) / 2
        rx = abs(bounding_box[2] - bounding_box[0]) / 2
        ry = abs(bounding_box[3] - bounding_box[1]) / 2
        oval = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" style="stroke:red; fill:blue;" />'
        self.lines.append(oval)

    def draw_point(self, point, size=3, color='red'):
        circle = f'<circle cx="{point.x}" cy="{point.y}" r="{size}" fill="{color}" />'
        self.lines.append(circle)
