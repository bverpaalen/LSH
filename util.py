from timeit import default_timer as timer
import sys


def get_parameters():
    if len(sys.argv) < 3:
        print("Please provide both parameters: seed and file location of user_movie.npy, for example:")
        print(">> python main.py <seed> <file_location>")
        sys.exit()

    seed = sys.argv[1]
    file_location = sys.argv[2]

    if seed.isdigit():
        seed = int(seed)
    else:
        print("Seed must be an integer.")
        sys.exit()

    if not file_location.rpartition('/')[-1] == "user_movie.npy":
        print("Please provide the right file location to user_movie.npy.")
        sys.exit()

    return seed, file_location

def print_time(start, print_prefix=""):
    end = timer()
    elapsed = end - start
    seconds = round(elapsed, 2)
    minutes = round(elapsed / 60, 2)
    print(print_prefix + "Elapsed time: " + str(seconds) + "s | " + str(minutes) + "m.")
