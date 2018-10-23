import numpy as np


def apply(signature_matrix, bands=7, rows=15):

    candidates = []
    for band in range(bands):
        buckets = {}
        for user, movies_signature in enumerate(signature_matrix):
            band_column = movies_signature[band * rows: (band + 1) * rows]
            group = ''
            for signature_value in band_column:
                group = group + str(signature_value)

            if group in buckets:
                buckets[group].append(user)
            else:
                buckets[group] = [user]

        for bucket in buckets:
            if len(buckets[bucket]) > 1:
                candidates.append(buckets[bucket])
                print(buckets[bucket])
    return candidates

def generate_shingles(user_movies_matrix, k=10, shingle=None):
    user_movies_shingles = []
    for u, user in enumerate(user_movies_matrix):
        shingles = []
        for i in range(0, len(user), k):
            shingle = ''
            for movie in user[i:i + k]:
                shingle = shingle + str(movie)
            shingles.append(int(shingle))
        #user_movies_matrix[u] = shingles
        user_movies_shingles.append(shingles)
    return user_movies_shingles