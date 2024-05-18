#!/usr/bin/python

from TextEditorModel import TextEditorModel
from tkinter import Canvas, Frame, BOTH, font, Tk, Menu, Button, Label, SUNKEN, messagebox
from LocationRange import LocationRange
import os
import importlib.util
from plugins.plugin_interface import Plugin 

class TextEditor(Frame):
   def __init__(self, text_editor_model: TextEditorModel):
      super().__init__()
      self.canvas = Canvas(self)
      self._TextEditorModel = text_editor_model
      self.text_font = font.Font(family='Courier', size=12) 
      self.plugins = []
      self.initUI()
      self._TextEditorModel.registerCursorObserver(self)
      self._TextEditorModel.registerTextObserver(self)
      self._TextEditorModel.undo_manager.registerObserver(self)
      self.load_plugins()
      
   def updateCursorLocation(self, loc):
      self.draw_cursor()  
      self.update_status_bar()
      
   def updateText(self):
      self.redraw()   
      self.update_status_bar()  
        
   def initUI(self):
      self.master.title("Text Editor")
      self.canvas.pack(fill=BOTH, expand=1)
      self.canvas.bind('<Motion>', self.mouse_move)
      self.canvas.bind('<Button-1>', self.mouse_click)
      self.bind_all('<Key>', self.key_press)
      
      self.initMenu()
      self.initToolbar()
      self.initStatusBar()
      self.draw_text()
      self.draw_cursor()
      
   def initMenu(self):
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)
        
        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_program)
        
        edit_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo_action)
        edit_menu.add_command(label="Redo", command=self.redo_action)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_command(label="Paste and Take", command=self.paste_and_take_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="Delete selection", command=self.delete_selection)
        edit_menu.add_command(label="Clear document", command=self.clear_document)
        
        move_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Move", menu=move_menu)
        move_menu.add_command(label="Cursor to document start", command=self.cursor_to_start)
        move_menu.add_command(label="Cursor to document end", command=self.cursor_to_end)
        
        plugins_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Plugins", menu=plugins_menu)
        self.plugins_menu = plugins_menu

   def initToolbar(self):
        toolbar = Frame(self.master, bd=1, relief='raised')
        undo_button = Button(toolbar, text="Undo", command=self.undo_action)
        redo_button = Button(toolbar, text="Redo", command=self.redo_action)
        cut_button = Button(toolbar, text="Cut", command=self.cut_text)
        copy_button = Button(toolbar, text="Copy", command=self.copy_text)
        paste_button = Button(toolbar, text="Paste", command=self.paste_text)
        
        undo_button.pack(side="left")
        redo_button.pack(side="left")
        cut_button.pack(side="left")
        copy_button.pack(side="left")
        paste_button.pack(side="left")
        
        toolbar.pack(side="top", fill="x")
        
   def initStatusBar(self):
        self.status_bar = Label(self.master, text="Line: 1, Column: 1 | Lines: 1", bd=1, relief=SUNKEN, anchor='w')
        self.status_bar.pack(side="bottom", fill="x")
        
   def update_status_bar(self):
        line = self._TextEditorModel.cursorLocation.line + 1
        column = self._TextEditorModel.cursorLocation.column + 1
        num_lines = len(self._TextEditorModel.lines)
        status_text = f"Line: {line}, Column: {column} | Lines: {num_lines}"
        self.status_bar.config(text=status_text)
        
   def load_plugins(self):
        plugin_folder = 'plugins'
        for filename in os.listdir(plugin_folder):
            if filename.endswith('.py'):
                plugin_path = os.path.join(plugin_folder, filename)
                spec = importlib.util.spec_from_file_location(filename[:-3], plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for attr in dir(module):
                    plugin_class = getattr(module, attr)
                    if isinstance(plugin_class, type) and issubclass(plugin_class, Plugin) and plugin_class is not Plugin:
                        plugin_instance = plugin_class()
                        self.plugins.append(plugin_instance)
                        self.plugins_menu.add_command(label=plugin_instance.get_name(), command=lambda p=plugin_instance: p.execute(self._TextEditorModel, self._TextEditorModel.undo_manager, self._TextEditorModel.clipboard))
   
   def open_file(self):
        pass
    
   def save_file(self):
        pass
    
   def exit_program(self):
        self.master.quit()  
   
   def undo_action(self):
        self._TextEditorModel.undo_manager.undo()
        self.updateUndoRedoStatus()
        
   def redo_action(self):
        self._TextEditorModel.undo_manager.redo()
        self.updateUndoRedoStatus()
    
   def cut_text(self):
        if self._TextEditorModel.getSelectionRange().start != self._TextEditorModel.getSelectionRange().end:
            selected_text = self._TextEditorModel.getSelectedText()
            self._TextEditorModel.clipboard.push(selected_text)
            self._TextEditorModel.deleteRange(self._TextEditorModel.getSelectionRange())
            self.updateUndoRedoStatus()
            
   def copy_text(self):
        if self._TextEditorModel.getSelectionRange().start != self._TextEditorModel.getSelectionRange().end:
            selected_text = self._TextEditorModel.getSelectedText()
            self._TextEditorModel.clipboard.push(selected_text)
    
   def paste_text(self):
        text = self._TextEditorModel.clipboard.peek()
        if text:
            self._TextEditorModel.insert_string(text)
            self.updateUndoRedoStatus()
    
   def paste_and_take_text(self):
        text = self._TextEditorModel.clipboard.pop()
        if text:
            self._TextEditorModel.insert_string(text)
            self.updateUndoRedoStatus() 
            
   def delete_selection(self):
        self._TextEditorModel.deleteRange(self._TextEditorModel.getSelectionRange())
    
   def clear_document(self):
        self._TextEditorModel.lines = [""]
        self._TextEditorModel.updateCursorLocation(0, 0)
        self._TextEditorModel.clear_selection()
        self._TextEditorModel.notifyTextObservers()
    
   def cursor_to_start(self):
        self._TextEditorModel.updateCursorLocation(0, 0)
    
   def cursor_to_end(self):
        last_line = len(self._TextEditorModel.lines) - 1
        last_col = len(self._TextEditorModel.lines[last_line])
        self._TextEditorModel.updateCursorLocation(last_line, last_col) 
              
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