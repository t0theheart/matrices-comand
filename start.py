from matrices_command.receiver import Receiver
from matrices_command.invoker import Invoker
from matrices_command.commands import *
from enum import Enum


class Commands(Enum):
    read = ReadCommand
    write = WriteCommand
    sum = SumCommand
    multiply = MultiplyCommand
    transport = TransportCommand
    delete = DeleteCommand
    undo = None


def main():
    """
        Example of using


        "Matrices command" started!
        Enter the command from list ['read', 'write', 'sum', 'multiply', 'transport', 'delete', 'undo']
        Commands "read" and "write" have second arg file path, examples:
        $ read examples/matrices.json
        $ write result.json
        Enter the command: read examples/matrices.json
        result: {'matrix_1': [[5, 8, -4], [6, 9, -5], [4, 7, -3]], 'matrix_2': [[3, 2, 5], [4, -1, 3], [9, 6, 5]]}
        Enter the command: sum
        result: {'sum': [[8, 10, 1], [10, 8, -2], [13, 13, 2]]}
        Enter the command: transport
        result: {'transport': [[8, 10, 13], [10, 8, 13], [1, -2, 2]]}
        Enter the command: undo
        result: {'sum': [[8, 10, 1], [10, 8, -2], [13, 13, 2]]}
        Enter the command: exit
        End.
    """
    print('"Matrices command" started!')
    receiver = Receiver()
    invoker = Invoker()
    print(f'Enter the command from list {[c.name for c in Commands]}')
    print('Commands "read" and "write" have second arg file path, examples:')
    print('$ read examples/matrices.json')
    print('$ write result.json')

    while True:
        inputs = input('Enter the command: ')
        if inputs == 'exit':
            print('End.')
            exit()
        elif inputs == 'undo':
            invoker.undo()
        else:
            args = inputs.split()
            command_cls = Commands[args[0]].value
            if len(args) == 1:
                command = command_cls(receiver)
                invoker.execute(command)
            elif len(args) == 2:
                arg = args[1]
                command = command_cls(receiver, arg)
                invoker.execute(command)

        print(f'result: {receiver.get_result()}')


if __name__ == '__main__':
    main()
