import pandas as pd
import scipy.sparse as sciparse
import data
import min_hashing as mh
import similarity as sim

import numpy as np


def experimenteer(filename):

    movie_data = data.load(filename, 10000)
    matrix = data.transform_to_matrix(movie_data)
    print(len(matrix))

    distinct_movies = np.unique(movie_data[:, 1])
    permutations = mh.generate_permutations(distinct_movies, 100)

    signature_matrix = np.array([np.zeros(100) for i in range(len(matrix))])
    for movie_index, movie in enumerate(distinct_movies):
        for user_id, userMovies in enumerate(matrix):
            if any(l == 0 for l in signature_matrix[user_id]):
                for pnr, permutation in enumerate(permutations):
                    if signature_matrix[user_id][pnr] == 0 and permutation[movie_index] in userMovies:
                        signature_matrix[user_id][pnr] = movie_index + 1

    #print(signature_matrix)

    similar_users = []
    for base_user, signature1 in enumerate(signature_matrix):
        for to_compare_user in range(base_user+1, len(signature_matrix)):
            #print(str(base_user) + " " + str(to_compare_user))
            signature2 = signature_matrix[to_compare_user]

            similarity = sim.jaccard(signature1, signature2)

            if similarity > 0.3:
                similar_users.append((base_user, to_compare_user))

            #print(round(intersection / len(signature1), 2))
            #print()
    print(similar_users)

    ''''first, second = similar_users[0]
    intersection = 0
    signature1 = matrix[first]
    print(signature1)
    signature2 = matrix[second]
    for i in signature1:
        if i in signature2:
            intersection = intersection + 1
    similarity = round(intersection / len(signature2), 2)
    print(similarity)'''

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

from timeit import default_timer as timer
start = timer()
experimenteer("user_movie.npy")
end = timer()
print(end - start)
#sparse_matrix = sciparse.load_npz("user_movie.npy")

#print(sparse_matrix[0])
#dt = pd.read_csv("user_movie.npy", engine="python")

#print(dt.iloc[0])