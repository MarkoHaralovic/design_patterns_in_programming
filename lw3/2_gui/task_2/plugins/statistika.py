import tkinter as tk
from plugins.plugin_interface import Plugin 

class Statistika(Plugin):
    def get_name(self):
        return "Statistika"
    
    def get_description(self):
        return "Counts lines, words, and characters in the document"
    
    def execute(self, model, undo_manager, clipboard_stack):
        text = "\n".join(model.get_text())
        lines = len(model.get_text())
        words = len(text.split())
        chars = len(text)

        message = f"Lines: {lines}\nWords: {words}\nCharacters: {chars}"
        tk.messagebox.showinfo("Document Statistics", message)
