import unittest
from matrices_command.receiver import Receiver
from matrices_command.invoker import Invoker
from matrices_command.commands import MultiplyCommand


class TestMultiplyCommand(unittest.TestCase):

    def test_multiply_case_1(self):
        matrices = {
            'matrix_1': [[3, 9, -5], [-3, 8, 8], [-8, -2, 6]],
            'matrix_2': [[10, -7, 5], [-2, -8, -8], [-1, -10, -8]]
        }
        expected_data = {'multiply': [[17, -43, -17], [-54, -123, -143], [-82, 12, -72]]}
        r = Receiver()
        i = Invoker()
        r.set_result(matrices)
        c = MultiplyCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)

    def test_multiply_case_2(self):
        matrices = {
            'matrix_1': [[-68, -93, -61], [-2, 81, -65], [62, -76, -20]],
            'matrix_2': [[38, -61, 57], [52, -27, 81], [32, 48, 69]]
        }
        expected_data = {'multiply': [[-9372, 3731, -15618], [2056, -5185, 1962], [-2236, -2690, -4002]]}
        r = Receiver()
        i = Invoker()
        r.set_result(matrices)
        c = MultiplyCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)

    def test_multiply_case_3(self):
        matrices = {
            'matrix_1': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            'matrix_2': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        }
        expected_data = {'multiply': [[0, 0, 0], [0, 0, 0], [0, 0, 0]]}
        r = Receiver()
        i = Invoker()
        r.set_result(matrices)
        c = MultiplyCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)
