#!/usr/bin/python

from TextEditorModel import TextEditorModel
from tkinter import Canvas, Frame, BOTH, font
from LocationRange import LocationRange

class TextEditor(Frame):
   def __init__(self, text_editor_model: TextEditorModel):
      super().__init__()
      self.canvas = Canvas(self)
      self._TextEditorModel = text_editor_model
      self.text_font = font.Font(family='Courier', size=12) 
      self.initUI()
      self._TextEditorModel.registerCursorObserver(self)
      self._TextEditorModel.registerTextObserver(self)
      self._TextEditorModel.undo_manager.registerObserver(self)
      
   def updateCursorLocation(self, loc):
        self.draw_cursor()  
         
   def updateText(self):
        self.redraw()     
        
   def initUI(self):
      self.master.title("Text Editor")
      self.canvas.pack(fill=BOTH, expand=1)
      self.canvas.bind('<Motion>', self.mouse_move)
      self.canvas.bind('<Button-1>', self.mouse_click)
      self.bind_all('<Key>', self.key_press)
      self.draw_text()
      self.draw_cursor()

   def draw_text(self):
        self.canvas.delete("text")
        y_offset = 10
        line_height = self.text_font.metrics('linespace')
        selection_range = self._TextEditorModel.getSelectionRange()
        start, end = selection_range.start, selection_range.end

        for i, line in enumerate(self._TextEditorModel.allLines()):
            if start.line <= i <= end.line:
                start_col = start.column if i == start.line else 0
                end_col = end.column if i == end.line else len(line)

                self.canvas.create_rectangle(
                    10 + self.text_font.measure(' ' * start_col), 
                    y_offset + i * line_height, 
                    10 + self.text_font.measure(' ' * end_col), 
                    y_offset + (i + 1) * line_height,
                    fill="lightblue", tags="text"
                )
            self.canvas.create_text(10, y_offset + i * line_height, anchor='nw', text=line, tags="text", font=self.text_font)

   def draw_cursor(self):
        self.canvas.delete("cursor")
        line_height = self.text_font.metrics('linespace')
        x = 10 + self._TextEditorModel.cursorLocation.column * self.text_font.measure(' ')
        y = 10 + self._TextEditorModel.cursorLocation.line * line_height
        self.cursor = self.canvas.create_line(x, y, x, y + line_height, fill="black", tags="cursor")

   def mouse_move(self, event):
      self._TextEditorModel.updateCursorLocation(event.y // self.text_font.metrics('linespace'),
                                                   (event.x - 10) // self.text_font.measure(' '))
      print(f"Mouse move: {event.x}, {event.y}")

   def mouse_click(self, event):
      line = event.y // self.text_font.metrics('linespace')
      x_offset = 10  
      col = (event.x - x_offset) // self.text_font.measure(' ')
      
      if line >= len(self._TextEditorModel.lines):
         line = len(self._TextEditorModel.lines) - 1
      if line < 0: 
         line = 0
      if col > len(self._TextEditorModel.lines[line]):
         col = len(self._TextEditorModel.lines[line])
      if col < 0:  
         col = 0

      self._TextEditorModel.updateCursorLocation(line, col)
      self._TextEditorModel.clear_selection()
      self.redraw()
      print(f"Mouse click: Line: {line}, Col: {col}")

   def key_press(self, event):
    print(f"Key press: {str(event.char)}")
    print(f"Key code: {str(event.keycode)}")
    print(f"Key symbol : {str(event.keysym)}")
    print(event)
    ctrl = (event.state & 0x4) != 0
    alt = (event.state & 0x8) != 0 or (event.state & 0x80) != 0
    shift = (event.state & 0x1) != 0

    selection_range = self._TextEditorModel.getSelectionRange()
    if ctrl and event.keysym.lower() == "c":
            if selection_range.start != selection_range.end:
                selected_text = self._TextEditorModel.getSelectedText()
                self._TextEditorModel.clipboard.push(selected_text)
    elif ctrl and event.keysym.lower() == "x":
            if selection_range.start != selection_range.end:
                selected_text = self._TextEditorModel.getSelectedText()
                self._TextEditorModel.clipboard.push(selected_text)
                self._TextEditorModel.deleteRange(selection_range)
    elif ctrl and event.keysym.lower() == "v":
            if shift:
                text = self._TextEditorModel.clipboard.pop()
            else:
                text = self._TextEditorModel.clipboard.peek()
            if text:
                self._TextEditorModel.insert_string(text)
    elif ctrl and event.keysym.lower() == "z":
        self._TextEditorModel.undo_manager.undo()
    elif ctrl and event.keysym.lower() == "y":
        self._TextEditorModel.undo_manager.redo()
    elif event.keysym == "BackSpace":
        if selection_range.start != selection_range.end:
            self._TextEditorModel.deleteRange(selection_range)
        else:
            self._TextEditorModel.deleteBefore()
    elif event.keysym == "Delete":
        if selection_range.start != selection_range.end:
            self._TextEditorModel.deleteRange(selection_range)
        else:
            self._TextEditorModel.deleteAfter()
    elif event.keysym == "Return":
        self._TextEditorModel.insert_text('\r')
    elif event.char and event.keysym not in ["BackSpace", "Delete", "Return"]:
        self._TextEditorModel.insert_char(event.char)
    elif event.keysym in ["Left", "Right", "Up", "Down"]:
        move_method = getattr(self._TextEditorModel, 'move_cursor_' + event.keysym.lower())
        move_method()
        if shift:
            self._TextEditorModel.setSelectionRange(
                LocationRange(self._TextEditorModel.getSelectionRange().start, self._TextEditorModel.cursorLocation)
            )
    elif event.keysym == "Escape":
        pass  # destroy
    elif event.char:
            self._TextEditorModel.insert_char(event.char)

    self.redraw()
   def updateUndoRedoStatus(self):
        pass
      
   def redraw(self):
        self.draw_text()
        self.draw_cursor()