import numpy as np
import mmh3 as mmh3
import sys


def generate_permutations(distinct_movies, number, seed=100):
    np.random.seed(seed)
    permutations = []
    for i in range(number):
        permutation = distinct_movies.copy()
        np.random.shuffle(permutation)
        permutations.append(permutation)

    return permutations


def generate_signature(user_movies_matrix):
    signature_matrix = [[] for i in range(len(user_movies_matrix))]
    #signature_matrix = np.array([np.zeros(100).astype(int) for i in range(len(user_movies_matrix))])

    for user_id, user_movies in enumerate(user_movies_matrix):
        np.random.seed(123)
        for i in range(50):
            ''''permutation = user_movies.copy()
            np.random.shuffle(permutation)
            for movie_index, user_movie in enumerate(user_movies):
                if signature_matrix[user_id][i] == 0 and permutation[movie_index] == user_movies[movie_index]:
                    signature_matrix[user_id][i] = movie_index + 1
                    break'''
            min_hash = sys.maxsize
            for user_movie in user_movies:
                hash = mmh3.hash(user_movie, seed=np.random.randint(2**16))
                if hash < min_hash:
                    min_hash = hash
            signature_matrix[user_id].append(min_hash)

    return signature_matrix
