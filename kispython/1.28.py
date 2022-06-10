from math import *


def main(y, z):

    f = y**2 - (exp(z)/30) - \
        sqrt((((z**2)/7) + z**3)**5 + ((27*(z**2))+(25*(y**3)))/13)
    return f
