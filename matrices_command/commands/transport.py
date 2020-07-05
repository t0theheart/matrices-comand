from .abc import CommandABC


class TransportCommand(CommandABC):
    def execute(self):
        self._receiver.transport()

    def undo(self):
        self._receiver.set_result(self._current_state)
