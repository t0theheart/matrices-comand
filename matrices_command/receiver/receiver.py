from .abc import ReceiverABC
from ._multiply_matrices import multiply_matrices, get_verticals_from_matrix
import json


class Receiver(ReceiverABC):
    def __init__(self):
        self._result = dict()

    def get_result(self):
        return self._result

    def read(self, read_from: str):
        with open(read_from, 'r') as f:
            self._result = json.load(f)

    def write(self, write_to: str):
        with open(write_to, 'w') as f:
            json.dump(self._result, fp=f)

    def delete(self):
        self._result = {}

    def sum(self):
        matrix_1, matrix_2 = self._result.values()
        self._result = {'sum': [
            [
                matrix_1[line][elem] + matrix_2[line][elem] for elem in range(len(matrix_1[0]))
            ] for line in range(len(matrix_1))
        ]}

    def multiply(self):
        matrix_1, matrix_2 = self._result.values()
        self._result = {'multiply': multiply_matrices(matrix_1, matrix_2)}

    def transport(self):
        self._result = {'transport': [get_verticals_from_matrix(m) for m in self._result.values()]}
