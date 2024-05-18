from plugins.plugin_interface import Plugin

class VelikoSlovo(Plugin):
    def get_name(self):
        return "Veliko Slovo"
    
    def get_description(self):
        return "Capitalizes the first letter of each word in the document"
    
    def execute(self, model, undo_manager, clipboard_stack):
        new_lines = []
        for line in model.get_text():
            new_line = ' '.join(word.capitalize() for word in line.split())
            new_lines.append(new_line)
        model.lines = new_lines
        model.notifyTextObservers()
