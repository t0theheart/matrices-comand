from .abc import CommandABC
from matrices_command.receiver import ReceiverABC
import os


class WriteCommand(CommandABC):
    def __init__(self, receiver: ReceiverABC, write_to: str):
        super().__init__(receiver)
        self._write_to = write_to

    def execute(self):
        self._receiver.write(self._write_to)

    def undo(self):
        self._receiver.set_result(self._current_state)
        os.remove(f'{self._write_to}')
