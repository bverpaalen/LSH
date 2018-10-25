import data
import min_hashing as mh
import LSH
from timeit import default_timer as timer
import util
import sys
import gc


def run(file_location, seed, k=128, b=16, r=8, partial=False, skip=0, take=-1):
    start_time = timer()

    print("==============================================")
    print("               PREPROCESSING")
    print("==============================================")

    movie_data = None
    user_movies_sparse_matrix = None

    if not partial:
        print("\nRunning sequential...")
        print("\nLoading data and generating matrix...")
        user_movies_sparse_matrix = data.transform_to_sparse_matrix(data.load(file_location, skip, take), partial)
    else:
        print("\nRunning partial...")
        print("\nLoading data...")
        movie_data = data.load(file_location, skip, take)
        print("Generating matrix...")
        user_movies_sparse_matrix = data.transform_to_sparse_matrix(movie_data, partial)

    matrix_shape = user_movies_sparse_matrix.shape
    print("Shape: " + str(matrix_shape[1]) + " users | " + str(matrix_shape[0]) + " movies.")
    nr_movies = matrix_shape[0]
    nr_users = matrix_shape[1]
    util.print_time(start_time)

    print()
    print("==============================================")
    print("                Min Hashing")
    print("==============================================")
    print("\nGenerating signature matrix...")
    print("Length: " + str(k))
    if not partial:
        signature_matrix = mh.generate_signature(user_movies_sparse_matrix, k, nr_users, nr_movies, seed)
    else:
        signature_matrix = mh.build_signature_in_parts(k, nr_users, nr_movies, user_movies_sparse_matrix, seed)

    util.print_time(start_time)

    print()
    print("==============================================")
    print("                    LSH")
    print("==============================================")

    print("\nNumber of bands: " + str(b))
    print("Number of rows per band: " + str(r))
    print()

    # free memory
    del user_movies_sparse_matrix
    gc.collect()

    if movie_data is None:
        movie_data = data.load(file_location, skip, take)

    user_movies_matrix = data.transform_to_dense_matrix(movie_data)
    nr_found, nr_buckets = LSH.apply(signature_matrix, user_movies_matrix, b, r, start_time)

    print_report(nr_found, nr_buckets, start_time, matrix_shape, k, b, r, seed)


def print_report(nr_found, nr_buckets, start_time, matrix_shape, k, b, r, seed):
    print("______________________________________________\n")

    print("Final Report")
    print("------------\n")
    print("Found pairs in total: " + str(nr_found))
    print("Number of buckets in total: " + str(nr_buckets))
    util.print_time(start_time)
    print()
    print("For:")
    print('Users: {1} | Movies: {0}'.format(str(matrix_shape[0]), str(matrix_shape[1])))
    print()
    print("With parameters:")
    print('Sig. Length: {0} | Bands: {1} | Rows: {2} | Seed: {3}'.format(k, b, r, seed))


seed, file_location = util.get_parameters()

run(file_location, seed)
