from math import *


def f(n):
    if (n == 0):
        f = -0.18
    elif (n == 1):
        f = -0.17
    else:
        f = ceil(1 - main(n-1) - main(n-2)**3) + 1
    return f


def main(n):
    return f(n)
