import unittest
from matrices_command.receiver import Receiver
from matrices_command.invoker import Invoker
from matrices_command.commands import SumCommand, TransportCommand


class TestUndo(unittest.TestCase):

    def test_undo_one_command(self):
        matrices = {
            'matrix_1': [[3, 9, -5], [-3, 8, 8], [-8, -2, 6]],
            'matrix_2': [[10, -7, 5], [-2, -8, -8], [-1, -10, -8]]
        }
        expected_data = matrices
        r = Receiver()
        i = Invoker()
        r.set_result(matrices)
        c = SumCommand(r)
        i.execute(c)
        i.undo()
        self.assertEqual(r.get_result(), expected_data)

    def test_undo_two_commands(self):
        matrices = {
            'matrix_1': [[3, 9, -5], [-3, 8, 8], [-8, -2, 6]],
            'matrix_2': [[10, -7, 5], [-2, -8, -8], [-1, -10, -8]]
        }
        expected_data = matrices
        r = Receiver()
        i = Invoker()
        r.set_result(matrices)
        c1 = SumCommand(r)
        c2 = TransportCommand(r)
        i.execute(c1)
        i.execute(c2)
        i.undo()
        i.undo()
        self.assertEqual(r.get_result(), expected_data)
