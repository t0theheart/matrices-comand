from .abc import CommandABC


class MultiplyCommand(CommandABC):
    def execute(self):
        self._receiver.multiply()

    def undo(self):
        self._receiver.set_result(self._current_state)
