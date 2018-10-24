import data
import min_hashing as mh
import similarity as sim
import hashlib
import LSH
from timeit import default_timer as timer
import sys
import gc

import numpy as np

''''dat = np.array([[0,1],[0,2],[1,2],[1,3]])
users = dat[:,0]
movies = dat[:,1]
a=[[1,2,3],
[3,4,5]]

from scipy import sparse
matrix = sparse.coo_matrix((np.ones(len(dat)), (movies, users)))
print(matrix.toarray())

for r in matrix.toarray():
    for c in r:
        print(c)

d = matrix.data'''''
#for r in matrix.row:

#for user, movie, occurence in zip(matrix.row, matrix.col, d):




def similar_users(signature_matrix):
    similar_users = []
    for base_user, signature1 in enumerate(signature_matrix):
        b = []
        for to_compare_user in range(base_user + 1, len(signature_matrix)):
            # print(str(base_user) + " " + str(to_compare_user))
            signature2 = signature_matrix[to_compare_user]

            similarity = sim.jaccard_sig(signature1, signature2)

            if similarity > 0.3:
                similar_users.append((base_user, to_compare_user))
            b.append(similarity)
            # print(round(intersection / len(signature1), 2))
            # print()'''''
        print(b)
    print(similar_users)


def experimenteer(filename, k=64, b=8, r=8, seed=123):
    start = timer()

    movie_data = data.load(filename, 0,60000000)

    user_movies_sparse_matrix = data.transform_to_sparse_matrix(movie_data)

    distinct_movies = np.unique(movie_data[:, 1])
    nr_users = user_movies_sparse_matrix.shape[1]
    nr_movies = len(distinct_movies)
    np.random.seed(seed)
    signature_matrix = mh.generate_signature(user_movies_sparse_matrix,k,nr_users,nr_movies)

    ''''signature_matrix = np.array([[-1] * k for i in range(nr_users)])

    for permutation_nr in range(k):
        permutation = list(range(0, nr_movies))
        np.random.shuffle(permutation)

        for user in range(nr_users):
            user_movies = user_movies_sparse_matrix[:,user]
            for index in permutation:
                if user_movies[index] == 1:
                    signature_matrix[user][permutation_nr] = index + 1
                    break'''
    # free memory
    del user_movies_sparse_matrix
    gc.collect()

    user_movies_matrix = data.transform_to_matrix(movie_data)
    print(len(user_movies_matrix))

    candidates = LSH.apply(signature_matrix,b,r)
    end = timer()
    print(end-start)

    ''''for user in range(user_movies_sparse_matrix.shape[1]):
        movies = user_movies_sparse_matrix[:,user]
        first_movie = (movies != 0).argmax(axis=0)
        signature_matrix[user][permutation_nr] = permutation[first_movie] + 1'''''


    '''for i, sig in enumerate(signature_matrix):
    for j in range(i+1, len(signature_matrix)):
        sig2 = signature_matrix[j]
        simi = sim.jaccard_sig(sig, sig2)
        if simi > 0.0:
            print((i,j))
            print(simi)
            print(sim.jaccard(user_movies_matrix[i], user_movies_matrix[j]))
            print()


s='''''
    ''''for movie_nr in permutation:
        row = user_movies_sparse_matrix[movie_nr]
        for user, column in enumerate(row):
            if column == 1:
                print()'''''


    ''''distinct_movies = np.unique(movie_data[:, 1])
    permutations = mh.generate_permutations(distinct_movies, 100)
    signature_matrix = np.array([[len(distinct_movies)+1]*100 for i in range(len(user_movies_sparse_matrix))])
    for movie_index, movie in enumerate(distinct_movies):
        for user_id in range(user_movies_sparse_matrix.shape[1]):
            if user_movies_sparse_matrix[:,user_id][movie_index] == 1:
                for pnr, permutation in enumerate(permutations):
                    if permutation[movie_index] < signature_matrix[user_id][pnr]:
                        signature_matrix[user_id][pnr] = movie_index + 1'''''


    #user_movies_matrix = data.transform_to_matrix(movie_data)
    #sim.jaccard(user_movies_matrix[0], user_movies_matrix[1])


    #user_movies_matrix = user_movies_matrix[413:]


    #print(sim.jaccard(user_movies_matrix[413], user_movies_matrix[4345]))

    #a = []
    #for i in range(1, 20):
        #a.append(sim.jaccard(user_movies_matrix[0], user_movies_matrix[i]))

    #print(a)
    ''''print(sim.jaccard(user_movies_matrix[1], user_movies_matrix[41]))
    print(sim.jaccard(user_movies_matrix[1], user_movies_matrix[86]))
    print(sim.jaccard(user_movies_matrix[1], user_movies_matrix[90]))
    print(sim.jaccard(user_movies_matrix[5], user_movies_matrix[39]))
    print(sim.jaccard(user_movies_matrix[12], user_movies_matrix[14]))
    print(sim.jaccard(user_movies_matrix[21], user_movies_matrix[146]))'''

    #signature_matrix = mh.generate_signature(user_movies_matrix)


    #print(len(user_movies_matrix))

    #shingles = LSH.generate_shingles(user_movies_matrix)

    ''''start = timer()
    distinct_movies = np.unique(movie_data[:, 1])
    end = timer()
    print(end - start)

    start = timer()
    permutations = mh.generate_permutations(distinct_movies, 100)
    end = timer()
    print(end - start)'''

    #candidates = LSH.apply(permutations)

    ''''start = timer()
    signature_matrix = np.array([np.zeros(100).astype(int) for i in range(len(user_movies_matrix))])
    for movie_index, movie in enumerate(distinct_movies):
        for user_id, userMovies in enumerate(user_movies_matrix):
            if any(l == 0 for l in signature_matrix[user_id]):
                for pnr, permutation in enumerate(permutations):
                    if signature_matrix[user_id][pnr] == 0 and permutation[movie_index] in userMovies:
                        signature_matrix[user_id][pnr] = movie_index + 1
    end = timer()
    print(end - start)'''

    #signature_matrix = mh.generate_signature(user_movies_matrix)
    #candidates = LSH.apply(signature_matrix)
    #candidates = LSH.apply2(user_movies_matrix)
    #print(signature_matrix)
    #similar_users(signature_matrix)

    count = 0
    
    print("Number of buckets: " + str(len(candidates)))
    #print(candidates[16686-1][0])
    #print(len(candidates[16686-1][1]))
    #return
    for cnr, (group_name, candidate_group) in enumerate(candidates):
        print("Number of candidates in bucket " + str(cnr) + ": " + str(len(candidate_group)))
        for cnr1, candidate1 in enumerate(candidate_group):
            for cnr2 in range(cnr1 + 1, len(candidate_group)):
                candidate2 = candidate_group[cnr2]
                jsim = sim.jaccard(user_movies_matrix[candidate1], user_movies_matrix[candidate2])
                if jsim > 0.49:
                    count = count + 1
                    print((candidate1, candidate2))
                    print(sim.jaccard(user_movies_matrix[candidate1], user_movies_matrix[candidate2]))
                    print(count)
                    print()
        #print()

    print(count)

    #similar_users(signature_matrix)


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


start = timer()
experimenteer("user_movie.npy")
end = timer()
print(end - start)
#sparse_matrix = sciparse.load_npz("user_movie.npy")

#print(sparse_matrix[0])
#dt = pd.read_csv("user_movie.npy", engine="python")

#print(dt.iloc[0])