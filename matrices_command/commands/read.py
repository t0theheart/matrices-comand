from .abc import CommandABC
from matrices_command.receiver import ReceiverABC


class ReadCommand(CommandABC):
    def __init__(self, receiver: ReceiverABC, read_from: str):
        super().__init__(receiver)
        self._read_from = read_from

    def execute(self):
        self._receiver.read(self._read_from)

    def undo(self):
        self._receiver.set_result(self._current_state)
