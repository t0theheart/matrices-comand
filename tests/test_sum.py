import unittest
from matrices_command.receiver import Receiver
from matrices_command.invoker import Invoker
from matrices_command.commands import SumCommand


class TestSumCommand(unittest.TestCase):

    def test_sum_case_1(self):
        matrices = {
            'matrix_1': [[3, 9, -5], [-3, 8, 8], [-8, -2, 6]],
            'matrix_2': [[10, -7, 5], [-2, -8, -8], [-1, -10, -8]]
        }
        expected_data = {'sum': [[13, 2, 0], [-5, 0, 0], [-9, -12, -2]]}
        r = Receiver()
        i = Invoker()
        r.set_result(matrices)
        c = SumCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)

    def test_sum_case_2(self):
        matrices = {
            'matrix_1': [[-68, -93, -61], [-2, 81, -65], [62, -76, -20]],
            'matrix_2': [[38, -61, 57], [52, -27, 81], [32, 48, 69]]
        }
        expected_data = {'sum': [[-30, -154, -4], [50, 54, 16], [94, -28, 49]]}
        r = Receiver()
        i = Invoker()
        r.set_result(matrices)
        c = SumCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)

    def test_sum_case_3(self):
        matrices = {
            'matrix_1': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            'matrix_2': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        }
        expected_data = {'sum': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]}
        r = Receiver()
        i = Invoker()
        r.set_result(matrices)
        c = SumCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)
