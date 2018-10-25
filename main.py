import data
import min_hashing as mh
import similarity as sim
import hashlib
import LSH

import numpy as np

bands = 20
rows = 7

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


def experimenteer(filename):
    movie_data = data.load(filename,10000000)
    user_movies_matrix = data.transform_to_matrix(movie_data)
    distinct_movies = np.unique(movie_data[:, 1])
    #user_movies_matrix = user_movies_matrix[413:]


#    print(sim.jaccard(user_movies_matrix[413], user_movies_matrix[4345]))

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

    ''''distinct_movies = np.unique(movie_data[:, 1])
    permutations = mh.generate_permutations(distinct_movies, 100)

    signature_matrix = np.array([np.zeros(100).astype(int) for i in range(len(user_movies_matrix))])
    for movie_index, movie in enumerate(distinct_movies):
        for user_id, userMovies in enumerate(user_movies_matrix):
            if any(l == 0 for l in signature_matrix[user_id]):
                for pnr, permutation in enumerate(permutations):
                    if signature_matrix[user_id][pnr] == 0 and permutation[movie_index] in userMovies:
                        signature_matrix[user_id][pnr] = movie_index + 1'''''

    start = timer()
    permutations = mh.generate_permutations(distinct_movies,bands * rows)
    print("Permutations: "+str(timer()-start))

    start = timer()
    signature_matrix = mh.permutations_to_matrix(user_movies_matrix,permutations)
    print("Permutation matrix: "+str(timer()-start))

    start = timer()
    candidates = LSH.apply2(signature_matrix,bands,rows)
    print("LSH time: "+str(timer()-start))
    #print(signature_matrix)
    #similar_users(signature_matrix)
    print("Candidates len: "+str(len(candidates)))

    bestCandidates = []

    for candidate_group in candidates:
        print("Bucket size: "+str(len(candidate_group)))
        for cnr1, candidate1 in enumerate(candidate_group):
            for cnr2 in range(cnr1 + 1, len(candidate_group)):
                candidate2 = candidate_group[cnr2]
                jaccardSim = sim.jaccard(user_movies_matrix[candidate1], user_movies_matrix[candidate2])
                if jaccardSim >= 0.5:
                    print((candidate1,candidate2))
                    print(jaccardSim)
                    bestCandidates.append((candidate1,candidate2))
    for candidates in bestCandidates:
        candidate1 = candidates[0]
        candidate2 = candidates[1]
        print(candidate1,candidate2)
        print(sim.jaccard(user_movies_matrix[candidate1],user_movies_matrix[candidate2]))
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

from timeit import default_timer as timer
start = timer()
experimenteer("user_movie.npy")
end = timer()
print(end - start)
#sparse_matrix = sciparse.load_npz("user_movie.npy")

#print(sparse_matrix[0])
#dt = pd.read_csv("user_movie.npy", engine="python")

#print(dt.iloc[0])