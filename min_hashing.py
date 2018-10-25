import numpy as np
import mmh3 as mmh3
import data


def generate_empty_signature(k, nr_users):
    signature_matrix = np.array([[-1] * k for i in range(nr_users)])
    return signature_matrix


def generate_signature(user_movies_sparse_matrix, k, nr_users, nr_movies, seed):
    np.random.seed(seed)
    signature_matrix = generate_empty_signature(k, nr_users)

    for permutation_nr in range(k):
        permutation = list(range(0, nr_movies))
        np.random.shuffle(permutation)

        for user in range(nr_users):
            user_movies = user_movies_sparse_matrix[:, user]
            for index in permutation:
                if user_movies[index] == 1:
                    signature_matrix[user][permutation_nr] = index + 1
                    break

    return signature_matrix


###############################################################
# For alternative approaches; not used in the current approach
###############################################################

def generate_permutations(distinct_movies, number, seed):
    """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    distinct_movies : list
        List of all unique movies
    number : int
        Number of permutations to create
    seed : int
        Number of permutations to create

    Returns
    -------
    2D list
        All generated permutations, where every permutation is a 1D list

    """
    np.random.seed(seed)
    permutations = []
    for i in range(number):
        permutation = distinct_movies.copy()
        np.random.shuffle(permutation)
        permutations.append(permutation)

    return permutations


def generate_hash_signature(user_movies_matrix, k, seed):
    signature_matrix = [[] for i in range(len(user_movies_matrix))]
    np.random.seed(seed)

    for user_id, user_movies in enumerate(user_movies_matrix):
        for i in range(k):
            min_hash = min([mmh3.hash(movie, seed=i) for movie in user_movies])
            signature_matrix[user_id].append(min_hash)

    return signature_matrix


def build_signature_in_parts(k, nr_users, nr_movies, user_movies_sparse_matrix, seed):
    signature_matrix = generate_empty_signature(k, nr_users)
    for i in range(4):
        _from = int(i * (nr_users / 4))
        to = int((i + 1) * (nr_users / 4))

        partial_matrix = data.slice_sparse(user_movies_sparse_matrix, _from, to)
        generate_partial_signature(partial_matrix, k, nr_movies, _from, signature_matrix, seed)

    return signature_matrix


def generate_partial_signature(partial_user_movies_sparse_matrix, k, nr_movies, prev_nr_users, signature_matrix, seed):
    np.random.seed(seed)
    for permutation_nr in range(k):
        permutation = list(range(0, nr_movies))
        np.random.shuffle(permutation)

        current_nr_users = partial_user_movies_sparse_matrix.shape[1]
        for curr_user_nr in range(current_nr_users):
            user = curr_user_nr + prev_nr_users
            user_movies = partial_user_movies_sparse_matrix[:, curr_user_nr]
            for index in permutation:
                if user_movies[index] == 1:
                    signature_matrix[user][permutation_nr] = index + 1
                    break
    return signature_matrix
