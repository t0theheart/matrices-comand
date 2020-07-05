from .abc import CommandABC


class DeleteCommand(CommandABC):
    def execute(self):
        self._receiver.delete()

    def undo(self):
        self._receiver.set_result(self._current_state)
