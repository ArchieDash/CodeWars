from collections import Counter


def find_uniq (array):
    for key, value in Counter(array).items():
        if value == 1:
            return key
