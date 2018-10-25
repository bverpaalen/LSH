import numpy as np
import scipy.sparse as sparse


def load(filename, skip=0, take=-1):
    data = np.load(filename)
    if not take == -1:
        return data[skip * take:(skip + 1) * take]

    return data


def transform_to_dense_matrix(data):
    user = -1
    matrix = []
    for i in data:
        if i[0] == user:
            matrix[user].append(i[1])
        else:
            user = i[0]
            matrix.append([i[1]])

    return matrix


def transform_to_sparse_matrix(data, partial=False):
    users = data[:, 0]
    movies = data[:, 1]

    matrix = None
    if not partial:
        matrix = sparse.coo_matrix((np.ones(len(data)).astype(int), (movies, users))).toarray()
    else:
        matrix = sparse.csc_matrix((np.ones(len(data)).astype(int), (movies, users)))

    return matrix


def slice_sparse(matrix, _from, to):
    return matrix[:, _from:to].toarray()


def save_pair(pair):
    file = open("results.txt", "a")
    file.write("{0}, {1}\n".format(pair[0], pair[1]))
    file.close()
