from abc import ABC, abstractmethod


class InvokerABC(ABC):
    @abstractmethod
    def execute(self, command): pass

    @abstractmethod
    def undo(self): pass
