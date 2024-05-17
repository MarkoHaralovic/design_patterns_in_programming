from Location import Location
from LocationRange import LocationRange
from CursorObserver import CursorObserver
from TextObserver import TextObserver
from ClipboardStack import ClipboardStack
from UndoManager import UndoManager
from EditAction import EditAction

class InsertAction(EditAction):
    def __init__(self, model, location, text):
        self.model = model
        self.location = location
        self.text = text

    def execute_do(self):
        self.model._insert_text(self.location, self.text)

    def execute_undo(self):
        self.model._delete_range(LocationRange(self.location, self._get_end_location()))

    def _get_end_location(self):
        lines = self.text.split('\n')
        end_line = self.location.line + len(lines) - 1
        end_column = len(lines[-1]) if len(lines) > 1 else self.location.column + len(self.text)
        return Location(end_line, end_column)

class DeleteAction(EditAction):
    def __init__(self, model, start_location, end_location, deleted_text):
        self.model = model
        self.start_location = start_location
        self.end_location = end_location
        self.deleted_text = deleted_text

    def execute_do(self):
        self.model._delete_range(LocationRange(self.start_location, self.end_location))

    def execute_undo(self):
        self.model._insert_text(self.start_location, self.deleted_text)
        
class TextEditorModel:
   def __init__(self, text: str):
      super().__init__()
      self.lines = text.split('\n')
      self.selectionRange = LocationRange(Location(0, 0), Location(0, 0))
      self.cursorLocation = Location(0, 0)
      self.cursorObservers = []
      self.textObservers = []
      self.clipboard = ClipboardStack()
      self.undo_manager = UndoManager()
      
   def registerCursorObserver(self, observer: CursorObserver):
        if observer not in self.cursorObservers:
            self.cursorObservers.append(observer)

   def removeCursorObserver(self, observer: CursorObserver):
        self.cursorObservers.remove(observer)

   def notifyCursorObservers(self):
        for observer in self.cursorObservers:
            observer.updateCursorLocation(self.cursorLocation) 
   def registerTextObserver(self, observer: TextObserver):
        if observer not in self.textObservers:
            self.textObservers.append(observer)
   def removeTextObserver(self, observer: TextObserver):
        if observer in self.textObservers:
            self.textObservers.remove(observer)
   def notifyTextObservers(self):
        for observer in self.textObservers:
            observer.updateText()
                      
   def get_text(self):
      return self.lines
   
   def insert_text(self, text):
        if self.selectionRange.start != self.selectionRange.end:
            self.deleteRange(self.selectionRange)
        line, col = self.cursorLocation.line, self.cursorLocation.column
        insert_action = InsertAction(self, Location(line, col), text)
        self.undo_manager.push(insert_action)
        insert_action.execute_do()
        self.notifyTextObservers()
   # def insert_text(self, text):
   #      if self.selectionRange.start != self.selectionRange.end:
   #          self.deleteRange(self.selectionRange)
   #      line, col = self.cursorLocation.line, self.cursorLocation.column
   #      if text == '\r':  # Handling Return key as new line
   #          # Split current line into two at cursor position
   #          current_line = self.lines[line]
   #          first_part = current_line[:col]
   #          second_part = current_line[col:]
   #          self.lines[line] = first_part
   #          self.lines.insert(line + 1, second_part)
   #          # Move cursor to the start of the next line
   #          self.updateCursorLocation(line + 1, 0)
   #      else:
   #          current_line = self.lines[line]
   #          new_line = current_line[:col] + text + current_line[col:]
   #          self.lines[line] = new_line
   #          # Update cursor location after insert
   #          self.updateCursorLocation(line, col + len(text))
   #      self.notifyTextObservers()

   def delete_text(self):
      line, col = self.cursorLocation.line, self.cursorLocation.column
      if col > 0:
         current_line = self.lines[line]
         new_line = current_line[:col-1] + current_line[col:]
         self.lines[line] = new_line
         self.updateCursorLocation(line, col - 1)
      elif line > 0:
         prev_line_len = len(self.lines[line - 1])
         self.lines[line - 1] += self.lines[line]
         del self.lines[line]
         self.updateCursorLocation(line - 1, prev_line_len)
      self.notifyTextObservers()
   
   def forward_delete(self):
      line, col = self.cursorLocation.line, self.cursorLocation.column
      if col < len(self.lines[line]):
         current_line = self.lines[line]
         new_line = current_line[:col] + current_line[col+1:]
         self.lines[line] = new_line
      elif line + 1 < len(self.lines):
         # If at the end of a line, merge with the next line
         self.lines[line] += self.lines[line + 1]
         del self.lines[line + 1]
      self.notifyTextObservers()
      
   def updateCursorLocation(self, line: int, column: int):
      if line < 0:
         line = 0
      elif line >= len(self.lines):
         line = len(self.lines) - 1
      if column < 0:
         column = 0
      elif column > len(self.lines[line]):
         column = len(self.lines[line])

      self.cursorLocation = Location(line, column)
      self.notifyCursorObservers()

      
   def set_selection_range(self, start_location: Location, end_location: Location):
      self.selectionRange = LocationRange(start_location, end_location)
      self.notifyTextObservers()

   def clear_selection(self):
      self.selectionRange = LocationRange(self.cursorLocation, self.cursorLocation)
      self.notifyTextObservers()
      
   def move_cursor_left(self):
      if self.cursorLocation.column > 0:
         self.cursorLocation.column -= 1
      elif self.cursorLocation.line > 0:
            self.cursorLocation.line -= 1
            self.cursorLocation.column = len(self.lines[self.cursorLocation.line])
      self.notifyCursorObservers()
    
   def move_cursor_right(self):
        if self.cursorLocation.column < len(self.lines[self.cursorLocation.line]):
            self.cursorLocation.column += 1
        elif self.cursorLocation.line < len(self.lines) - 1:
            self.cursorLocation.line += 1
            self.cursorLocation.column = 0
        self.notifyCursorObservers()
        
   def move_cursor_up(self):
        if self.cursorLocation.line > 0:
            self.cursorLocation.line -= 1
            self.cursorLocation.column = min(self.cursorLocation.column, len(self.lines[self.cursorLocation.line]))
        self.notifyCursorObservers()
        
   def move_cursor_down(self):
        if self.cursorLocation.line < len(self.lines) - 1:
            self.cursorLocation.line += 1
            self.cursorLocation.column = min(self.cursorLocation.column, len(self.lines[self.cursorLocation.line]))
        self.notifyCursorObservers()
          
   def allLines(self):
      return iter(self.lines)
   
   def linesRange(self, index1, index2):
      return iter(self.lines[index1:index2])
   
   def deleteBefore(self):
        if self.cursorLocation.column > 0:
            self.cursorLocation.column -= 1
            self.delete_text()  
        elif self.cursorLocation.line > 0:
            self.cursorLocation.line -= 1
            self.cursorLocation.column = len(self.lines[self.cursorLocation.line])
            self.lines[self.cursorLocation.line] += self.lines[self.cursorLocation.line + 1]
            del self.lines[self.cursorLocation.line + 1]
        self.notifyTextObservers()
        
   # def deleteAfter(self):
   #      self.forward_delete()  # Assuming forward_delete handles single character deletion
   #      self.notifyTextObservers()
   def deleteAfter(self):
        line, col = self.cursorLocation.line, self.cursorLocation.column
        if col < len(self.lines[line]):
            current_line = self.lines[line]
            deleted_text = current_line[col]
            new_line = current_line[:col] + current_line[col + 1:]
            self.lines[line] = new_line
            delete_action = DeleteAction(self, Location(line, col), Location(line, col + 1), deleted_text)
            self.undo_manager.push(delete_action)
        elif line + 1 < len(self.lines):
            deleted_text = '\n'
            self.lines[line] += self.lines[line + 1]
            del self.lines[line + 1]
            delete_action = DeleteAction(self, Location(line, len(self.lines[line])), Location(line + 1, 0), deleted_text)
            self.undo_manager.push(delete_action)
        self.notifyTextObservers()
   
   def deleteRange(self, r: LocationRange):
      try:
            start = r.start
            end = r.end
            if start.line == end.line:
                  self.lines[start.line] = self.lines[start.line][:start.column] + self.lines[start.line][end.column:]
            else:
                  self.lines[start.line] = self.lines[start.line][:start.column] + self.lines[end.line][end.column:]
                  del self.lines[start.line + 1:end.line + 1]
            self.updateCursorLocation(start.line, start.column)
            self.clear_selection()
            self.notifyTextObservers()
      except Exception as e:
          return
   
   def getSelectionRange(self):
        return self.selectionRange

   def setSelectionRange(self, range: LocationRange):
      self.selectionRange = range
      self.notifyTextObservers()
   
   def clear_selection(self):
     self.selectionRange = LocationRange(self.cursorLocation, self.cursorLocation)
     self.notifyTextObservers()

   def insert_char(self, c):
      if self.selectionRange.start != self.selectionRange.end:
         self.deleteRange(self.selectionRange)
      line, col = self.cursorLocation.line, self.cursorLocation.column
      current_line = self.lines[line]
      new_line = current_line[:col] + c + current_line[col:]
      self.lines[line] = new_line
      self.updateCursorLocation(line, col + 1)
      self.notifyTextObservers()
   # def insert_char(self, c):
   #      self.insert_text(c)
        
   def insert_string(self, text):
      if self.selectionRange.start != self.selectionRange.end:
         self.deleteRange(self.selectionRange)
      lines_to_insert = text.split('\n')
      line, col = self.cursorLocation.line, self.cursorLocation.column
      current_line = self.lines[line]
      if len(lines_to_insert) == 1:
         new_line = current_line[:col] + lines_to_insert[0] + current_line[col:]
         self.lines[line] = new_line
         self.updateCursorLocation(line, col + len(lines_to_insert[0]))
      else:
         self.lines[line] = current_line[:col] + lines_to_insert[0]
         for i, insert_line in enumerate(lines_to_insert[1:], start=1):
               self.lines.insert(line + i, insert_line)
         self.lines[line + len(lines_to_insert) - 1] += current_line[col:]
         self.updateCursorLocation(line + len(lines_to_insert) - 1, len(lines_to_insert[-1]))
      self.notifyTextObservers()
   
   def getSelectedText(self):
        start = self.selectionRange.start
        end = self.selectionRange.end
        if start.line == end.line:
            return self.lines[start.line][start.column:end.column]
        else:
            selected_text = []
            selected_text.append(self.lines[start.line][start.column:])
            for i in range(start.line + 1, end.line):
                selected_text.append(self.lines[i])
            selected_text.append(self.lines[end.line][:end.column])
            return '\n'.join(selected_text)
         
   def _insert_text(self, location, text):
        line, col = location.line, location.column
        if text == '\r':  
            current_line = self.lines[line]
            first_part = current_line[:col]
            second_part = current_line[col:]
            self.lines[line] = first_part
            self.lines.insert(line + 1, second_part)
            self.updateCursorLocation(line + 1, 0)
        else:
            current_line = self.lines[line]
            new_line = current_line[:col] + text + current_line[col:]
            self.lines[line] = new_line
            self.updateCursorLocation(line, col + len(text))
        self.notifyTextObservers()
  
   def _delete_range(self, r: LocationRange):
        start = r.start
        end = r.end
        try:
           if start.line == end.line:
            self.lines[start.line] = self.lines[start.line][:start.column] + self.lines[start.line][end.column:]
           else:
                  self.lines[start.line] = self.lines[start.line][:start.column] + self.lines[end.line][end.column:]
                  del self.lines[start.line + 1:end.line + 1]
        except Exception as e:
           return
        self.updateCursorLocation(start.line, start.column)
        self.clear_selection()
        self.notifyTextObservers()
     
