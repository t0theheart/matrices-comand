import unittest
from matrices_command.receiver import Receiver
from matrices_command.invoker import Invoker
from matrices_command.commands import TransportCommand


class TestTransportCommand(unittest.TestCase):

    def test_transport_matrix_3_x_3(self):
        input_data = {'data': [
            [5, 8, -4],
            [6, 9, -5],
            [4, 7, -3]
        ]}
        expected_data = {'transport': [
            [5, 6, 4],
            [8, 9, 7],
            [-4, -5, -3]
        ]}
        r = Receiver()
        i = Invoker()
        r.set_result(input_data)
        c = TransportCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)

    def test_transport_matrix_3_x_2(self):
        input_data = {'data': [
            [5, 8],
            [6, 9],
            [4, 7]
        ]}
        expected_data = {'transport': [
            [5, 6, 4],
            [8, 9, 7]
        ]}
        r = Receiver()
        i = Invoker()
        r.set_result(input_data)
        c = TransportCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)

    def test_transport_matrix_2_x_3(self):
        input_data = {'data': [
            [5, 8, -4],
            [6, 9, -5],
        ]}
        expected_data = {'transport': [
            [5, 6],
            [8, 9],
            [-4, -5]
        ]}
        r = Receiver()
        i = Invoker()
        r.set_result(input_data)
        c = TransportCommand(r)
        i.execute(c)
        self.assertEqual(r.get_result(), expected_data)
