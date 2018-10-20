import numpy as np

def generate_permutations(distinct_movies, number, seed = 100):
    np.random.seed(seed)
    permutations = []
    for i in range(number):
        permutation = distinct_movies.copy()
        np.random.shuffle(permutation)
        permutations.append(permutation)

    return permutations