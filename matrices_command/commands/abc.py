from abc import ABC, abstractmethod
from matrices_command.receiver import ReceiverABC


class CommandABC(ABC):
    def __init__(self, receiver: ReceiverABC):
        self._receiver = receiver
        self._current_state = receiver.get_result()

    @abstractmethod
    def execute(self): pass

    @abstractmethod
    def undo(self): pass
