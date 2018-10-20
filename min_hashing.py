import numpy as np
import hashlib

def generate_permutations(distinct_movies, number, seed = 100):
    np.random.seed(seed)
    permutations = []
    for i in range(number):
        permutation = distinct_movies.copy()
        np.random.shuffle(permutation)
        permutations.append(permutation)

    return permutations

def generate_signature(user_movies_matrix):
    signature_matrix = [[] for i in range(len(user_movies_matrix))]
    for user_id, user_movies in enumerate(user_movies_matrix):
        for hnr, hash_name in enumerate(hashlib.algorithms_guaranteed):
            hash_function = getattr(hashlib, hash_name)
            min_hash = hash_function(str(1000000).encode()).hexdigest()
            for user_movie in enumerate(user_movies):
                hash = hash_function(str(user_movie).encode()).hexdigest()
                if hash < min_hash:
                    min_hash = hash
            signature_matrix[user_id].append(min_hash)

    return signature_matrix