from matrices_command.receiver import Receiver
from matrices_command.invoker import Invoker
from matrices_command.commands import *


receiver = Receiver()
invoker = Invoker()

print(receiver.get_result())  # {}

read_command = ReadCommand(receiver, read_from='matrices.json')
invoker.execute(read_command)
print(receiver.get_result())  # {'matrix_1': [[5, 8, -4], [6, 9, -5], [4, 7, -3]], 'matrix_2': [[3, 2, 5], [4, -1, 3], [9, 6, 5]]}


sum_command = SumCommand(receiver)
invoker.execute(sum_command)
print(receiver.get_result())  # {'sum': [[8, 10, 1], [10, 8, -2], [13, 13, 2]]}


invoker.undo()
print(receiver.get_result())  # {'matrix_1': [[5, 8, -4], [6, 9, -5], [4, 7, -3]], 'matrix_2': [[3, 2, 5], [4, -1, 3], [9, 6, 5]]}


multiply_command = MultiplyCommand(receiver)
invoker.execute(multiply_command)
print(receiver.get_result())  # {'multiply': [[11, -22, 29], [9, -27, 32], [13, -17, 26]]}


transport_command = TransportCommand(receiver)
invoker.execute(transport_command)
print(receiver.get_result())  # {'transport': [[[11, 9, 13], [-22, -27, -17], [29, 32, 26]]]}


write_command = WriteCommand(receiver, write_to='result_1.json')
invoker.execute(write_command)


invoker.undo()  # undo write_command, delete file result_1.json
invoker.undo()  # undo transport_command
invoker.undo()  # undo multiply_command
print(receiver.get_result())  # {'matrix_1': [[5, 8, -4], [6, 9, -5], [4, 7, -3]], 'matrix_2': [[3, 2, 5], [4, -1, 3], [9, 6, 5]]}


delete_command = DeleteCommand(receiver)
invoker.execute(delete_command)
print(receiver.get_result())  # {}
