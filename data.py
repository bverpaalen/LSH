import numpy as np

def load(filename):
    data = np.load(filename)
    sample = data[:1000]
    return sample

def transform_to_matrix(data):

    user = -1
    matrix = []
    for i in data:
        if i[0] == user:
            matrix[user].append(i[1])
        else:
            user = i[0]
            matrix.append([i[0]])

    return matrix