import numpy as np


def load(filename, take=None):
    data = np.load(filename)
    if take is not None:
        return data[:take]

    return data


def transform_to_matrix(data):
    user = -1
    matrix = []
    for i in data:
        if i[0] == user:
            matrix[user].append(i[1])
        else:
            user = i[0]
            matrix.append([i[1]])

    return matrix
