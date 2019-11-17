from functools import reduce


def summation(num):
    return reduce(lambda a,b: a+b, list(range(num+1)))
