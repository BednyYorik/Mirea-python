from math import *


def main(y, z):

    f = 0
    n = len(y)
    for i in range(1, n+1):
        f += 38*(((z[ceil(i/4)-1])-(y[n+1-ceil(i/4)-1])**3)**3)
    return 65*f
