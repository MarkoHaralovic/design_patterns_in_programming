class EditAction:
    def execute_do(self):
        raise NotImplementedError("Subclasses should implement this!")

    def execute_undo(self):
        raise NotImplementedError("Subclasses should implement this!")
