from .abc import InvokerABC


class Invoker(InvokerABC):
    def __init__(self):
        self._commands = []

    def execute(self, command):
        self._commands.append(command)
        self._commands[-1].execute()

    def undo(self):
        self._commands[-1].undo()
        self._commands.pop(-1)
