

def main(x):
    A = x & 0b11111111111
    B = (x >> 11) & 0b11111111111
    C = (x >> 22) & 0b111111111
    return B | (C << 10) | (A << 19)   

print(main(0xb697f497))