import numpy as np
import mmh3 as mmh3
import similarity as sim
import util
import data


def apply(signature_matrix, user_movies_matrix, bands, rows, start_time):
    nr_buckets = 0
    nr_found = [0]
    for band in range(bands):
        print("\t\t\t| Band number: " + str(band + 1) + " |")
        print("\t\t\t ---------------\n")
        buckets = {}
        for user, movies_signature in enumerate(signature_matrix):
            band_column = movies_signature[band * rows: (band + 1) * rows]

            group = ''
            for signature_value in band_column:
                group = group + "," + str(signature_value)

            if group in buckets:
                buckets[group].append(user)
            else:
                buckets[group] = [user]

        for bucket in buckets:
            if len(buckets[bucket]) > 1:
                nr_buckets = nr_buckets + 1
                verify_partial_candidates(buckets[bucket], user_movies_matrix, nr_buckets, nr_found, start_time)
        print("\t*************************************\n")

    return nr_found[0], nr_buckets


def verify_partial_candidates(candidate_group, user_movies_matrix, bucket_nr, nr_found, start_time):
    for cnr1, candidate1 in enumerate(candidate_group):
        for cnr2 in range(cnr1 + 1, len(candidate_group)):
            candidate2 = list(candidate_group)[cnr2]
            jsim = sim.jaccard(user_movies_matrix[candidate1], user_movies_matrix[candidate2])
            if jsim >= 0.50:
                pair = sorted((candidate1, candidate2))
                data.save_pair(pair)
                print("\tFound similar pair: " + str(pair))
                print("\tSimilarity: " + str(
                    sim.jaccard(user_movies_matrix[candidate1], user_movies_matrix[candidate2])))
                print("\tBucket number: " + str(bucket_nr))
                print("\tNumber of candidates in the bucket: " + str(len(candidate_group)))
                nr_found[0] = nr_found[0] + 1
                print("\tFound until now: " + str(nr_found[0]))
                util.print_time(start_time, "\t")
                print()


def verify_candidates(candidates, user_movies_matrix, start_time):
    print("\nVerifying candidates...")
    count = 0

    print("Number of buckets in total: " + str(len(candidates)))
    for cnr, candidate_group in enumerate(candidates):
        # print("Number of candidates in bucket " + str(cnr) + ": " + str(len(candidate_group)))
        for cnr1, candidate1 in enumerate(candidate_group):
            for cnr2 in range(cnr1 + 1, len(candidate_group)):
                candidate2 = list(candidate_group)[cnr2]
                jsim = sim.jaccard(user_movies_matrix[candidate1], user_movies_matrix[candidate2])
                if jsim >= 0.50:
                    print("Number of candidates in bucket " + str(cnr) + ": " + str(len(candidate_group)))
                    count = count + 1
                    print((candidate1, candidate2))
                    print("Similarity: " + str(
                        sim.jaccard(user_movies_matrix[candidate1], user_movies_matrix[candidate2])))
                    print("Found until now: " + str(count))
                    util.print_time(start_time)
                    print()
        # print()

    print(count)


def apply2(user_movies_matrix, bands=5, rows=10):
    permutations = []
    for r in range(100):
        permutation = []
        for u in user_movies_matrix:
            permutation.append(u[r])
        permutations.append(permutation)

    signature_matrix = np.array([np.zeros(100).astype(int) for i in range(len(user_movies_matrix))])
    for permutation in permutations:
        for i, user_movies in enumerate(user_movies_matrix):
            if permutation[i] in user_movies:
                signature_matrix[i][0]

    for b in range(1, bands + 1):
        buckets = {}
        for user_id, user_movies in enumerate(user_movies_matrix):
            row_signature = ''
            for r in range(1, rows + 1):
                min_hash = min([mmh3.hash(movie, seed=b * r) for movie in user_movies])
                row_signature = row_signature + str(min_hash)

            if row_signature in buckets:
                buckets[row_signature].append(user_id)
            else:
                buckets[row_signature] = [user_id]

        for bucket in buckets:
            candidate_group = buckets[bucket]
            if len(candidate_group) > 1:
                for cnr1, candidate1 in enumerate(candidate_group):
                    for cnr2 in range(cnr1 + 1, len(candidate_group)):
                        candidate2 = candidate_group[cnr2]
                        print((candidate1, candidate2))
                        print(sim.jaccard(user_movies_matrix[candidate1], user_movies_matrix[candidate2]))


def generate_shingles(user_movies_matrix, k=10, shingle=None):
    user_movies_shingles = []
    for u, user in enumerate(user_movies_matrix):
        shingles = []
        for i in range(0, len(user), k):
            shingle = ''
            for movie in user[i:i + k]:
                shingle = shingle + str(movie)
            shingles.append(int(shingle))
        # user_movies_matrix[u] = shingles
        user_movies_shingles.append(shingles)
    return user_movies_shingles
