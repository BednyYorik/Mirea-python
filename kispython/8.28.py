import re


def main(input):
    seq = re.findall(r'[==>, ==> ][\s]?(\w*);', input)
    data_str = list(re.findall(r'\(([0-9- .\n]*)\)', input))
    data = []
    for i in range(len(data_str)):
        data.append(re.findall(r'(-?\d+)', data_str[i]))
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    dictionary = dict(zip(seq, data))
    return(dictionary)
