import unittest
from matrices_command.receiver import Receiver
from matrices_command.invoker import Invoker
from matrices_command.commands import DeleteCommand


class TestDeleteCommand(unittest.TestCase):

    def test_delete(self):
        matrices = {
            'matrix_1': [[3, 9, -5], [-3, 8, 8], [-8, -2, 6]],
            'matrix_2': [[10, -7, 5], [-2, -8, -8], [-1, -10, -8]]
        }
        expected_data = {}
        r = Receiver()
        i = Invoker()
        r.set_result(matrices)
        c = DeleteCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)
