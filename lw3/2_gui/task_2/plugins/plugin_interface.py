class Plugin:
    def get_name(self):
        raise NotImplementedError
    
    def get_description(self):
        raise NotImplementedError
    
    def execute(self, model, undo_manager, clipboard_stack):
        raise NotImplementedError
