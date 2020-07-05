from .abc import CommandABC


class SumCommand(CommandABC):
    def execute(self):
        self._receiver.sum()

    def undo(self):
        self._receiver.set_result(self._current_state)
