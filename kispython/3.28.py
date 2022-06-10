from math import log


def main(m, p, b, a):

    f1 = 0

    for k in range(1, m+1):
        f1 = f1 + 6*(p-89*(k**3)) + (98*(k**3) - 0.03 - p)**4

    f2 = 0

    for c in range(1, m+1):
        for j in range(1, a+1):
            for i in range(1, b+1):
                f2 = f2 + (log(i) + (((16*(c**3)) + 76)**5) + (15*((j)**3)))

    return f1 - f2
