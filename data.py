import numpy as np
import scipy.sparse as sparse


def load(filename, skip=0, take=None):
    data = np.load(filename)
    if not take is None:
        return data[skip*take:(skip+1)*take]

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

def transform_to_sparse_matrix(data):
    users = data[:, 0]
    movies = data[:, 1]

    matrix = sparse.coo_matrix((np.ones(len(data)).astype(int), (movies, users))).toarray()
    #print(matrix)
    return matrix
