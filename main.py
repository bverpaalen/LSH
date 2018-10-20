import pandas as pd
import scipy.sparse as sciparse
import data

import numpy as np


def experimenteer(filename):
    movie_data = data.load(filename)
    matrix = data.transform_to_matrix(movie_data)

    distinctMovies = np.unique(movie_data[:, 1])
    np.random.seed(100)
    np.random.shuffle(distinctMovies)

    distinctMovies2 = distinctMovies.copy()
    np.random.shuffle(distinctMovies2)
    distinctMovies3 = distinctMovies.copy()
    np.random.shuffle(distinctMovies3)

    matrix1 = np.zeros((len(distinctMovies), len(matrix)))
    matrix2 = np.zeros((len(distinctMovies), len(matrix)))
    matrix3 = np.zeros((len(distinctMovies), len(matrix)))
    matrix4 = np.array([np.zeros(3) for i in range(len(matrix))])
    for i, movie in enumerate(distinctMovies):
        for j, userMovies in enumerate(matrix):
            if matrix4[j][0] == 0 and distinctMovies[i] in userMovies:
                matrix4[j][0] = i + 1
            if matrix4[j][1] == 0 and distinctMovies2[i] in userMovies:
                matrix4[j][1] = i + 1
            if matrix4[j][2] == 0 and distinctMovies3[i] in userMovies:
                matrix4[j][2] = i + 1

    print(matrix4)

    '''' _, keys_as_int = np.unique(y[:, 0], return_inverse=True)
 n_keys = max(keys_as_int)
 indices = [[] for i in range(n_keys + 1)]
 for i, k in enumerate(keys_as_int):
     indices[k].append(y[i][1])
 indices = [np.array(elt) for elt in indices]

  #g = Groupby(s)
n = np.unique(s[:, 0])
print(len(n))
z = np.array([list(y[y[:, 0] == i, 1]) for i in n])
sparse_matrix=sciparse.coo_matrix((y['data'],(y['row'],y['col'])),shape=y['shape'])
print(sparse_matrix[0])'''


experimenteer("user_movie.npy")
#sparse_matrix = sciparse.load_npz("user_movie.npy")

#print(sparse_matrix[0])
#dt = pd.read_csv("user_movie.npy", engine="python")

#print(dt.iloc[0])