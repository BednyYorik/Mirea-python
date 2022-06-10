a, b, c, d, e, f = range(6)

N = [
    {'flag': True, 'index': 2, 'SVG': b, 'PIKE': c},  # a
    {'flag': True, 'index': 0, 'YACC': d, 'CSS': e, 'SAS': f},  # b
    {'flag': False, 'index': 1, 1977: 8, 2012: 9},  # c
    {'flag': False, 'index': 3, 2017: 0, 1977: 1, 2000: 2},  # d
    {'flag': False, 'index': 1, 1977: 3, 2012: 4},  # e
    {'flag': False, 'index': 3, 2017: 5, 1977: 6, 2000: 7}  # f
]


def main(input):
    rez = 0
    for i in range(4):
        if (N[rez].get('flag')):
            index = N[rez].get('index')
            rez = N[rez].get(input[index])
        else:
            index = N[rez].get('index')
            rez = N[rez].get(input[index])
            break
    return rez
