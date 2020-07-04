from operator import mul, add
from functools import reduce


# get from https://github.com/t0theheart/matrices-multiplier but remove threading and logging

def multiply_matrices(matrix_1, matrix_2):
    result_matrix = [None for _ in matrix_2]
    verticals_from_matrix_2 = get_verticals_from_matrix(matrix_2)

    for x in range(len(result_matrix)):
        put_line_in_result(result_matrix, matrix_1, verticals_from_matrix_2, x)

    return result_matrix


def put_line_in_result(result_matrix, matrix_1, verticals_from_matrix_2, x):
    result_matrix[x] = calculate_line(matrix_1, verticals_from_matrix_2, x)


def calculate_line(matrix_1, verticals_from_matrix_2, x):
    return [multiply_lists(matrix_1[x], verticals_from_matrix_2[y]) for y in range(len(verticals_from_matrix_2))]


def multiply_lists(x, y):
    return reduce(add, map(mul, x, y))


def get_verticals_from_matrix(matrix):
    return list(map(lambda *elements: list(elements), *matrix))
