import struct


def structE(data, adr):
    uint64, = struct.unpack("<Q", data[adr:adr+8])
    n, = struct.unpack("<h", data[adr+8:adr+10])
    adrArr, = struct.unpack("<h", data[adr+10:adr+12])
    uint64Arr = []
    for i in range(n):
        a, = struct.unpack("<Q", data[adrArr+(i*8):adrArr+(i*8)+8])
        uint64Arr.append(a)
    uint8, = struct.unpack("<B", data[adr+12:adr+13])
    return {'E1': uint64, 'E2': uint64Arr, 'E3': uint8}


def structD(data, adr):
    uint32, = struct.unpack("<I", data[adr:adr+4])
    int32_1, = struct.unpack("<i", data[adr+4:adr+8])
    int32_2, = struct.unpack("<i", data[adr+8:adr+12])
    return {'D1': uint32, 'D2': int32_1, 'D3': int32_2}


def structC(data, adr):
    strD = []
    strD.append(structD(data, adr))
    strD.append(structD(data, adr+12))
    strD.append(structD(data, adr+24))
    intArr = []
    for i in range(0, 5):
        a, = struct.unpack("<b", data[adr+36+i:adr+37+i])
        intArr.append(a)
    int8, = struct.unpack("<b", data[adr+41:adr+42])
    strE_adr, = struct.unpack("<h", data[adr+42:adr+44])
    strE = structE(data, strE_adr)
    int32, = struct.unpack("<i", data[adr+44:adr+48])
    int64, = struct.unpack("<q", data[adr+48:adr+56])
    float, = struct.unpack("<f", data[adr+56:adr+60])
    return {'C1': strD, 'C2': intArr,
            'C3': int8, 'C4': strE, 'C5': int32,
            'C6': int64, 'C7': float}


def structB(data, adr):
    float, = struct.unpack("<f", data[adr:adr+4])
    double, = struct.unpack("<d", data[adr+4:adr+12])
    uint32, = struct.unpack("<I", data[adr+12:adr+16])
    int32, = struct.unpack("<i", data[adr+16:adr+20])
    return {'B1': float, 'B2': double, 'B3': uint32, 'B4': int32}


def structA(data):
    strB_addr, = struct.unpack("<h", data[4:6])
    strB = structB(data, strB_addr)
    char_ = struct.unpack('<' + str(2) + 'c', data[6:8])
    charArr = ''
    for i in range(0, 2, 1):
        charArr += chr(char_[i][0])
    strC_addr, = struct.unpack("<h", data[8:10])
    strC = structC(data, strC_addr)
    return {'A1': strB, 'A2': charArr, 'A3': strC}


def main(bytesSequence):
    return structA(bytesSequence)



print(main(b'\xc2CMS\n\x00tjC\x00\x85\xeb\xce\xbc0\xc4\xf4C\xa9\x88\xbb?\x87tc?\x97%'
 b'\x95\xcd@<\xc1t#\x9f\x0c\x08\x89d8IV\xa1\xa1\xdb\x0b;\xaebQ\xe3{\xe0\xd2\x08'
 b'\xde5\xc5\x01g\x1f\x03\x00\x1e\x00\x9f\x02U\xc0q\x1a\xebv\xb3\x15'
 b'\xbe\xbe\xe1x\xcd\x86q\xd1\x12\x03U\x06\x88SA\xd3e\xbf\x03\xf3\xdb\x1dB\xdf'
 b'N\x98A7\xd6\x82\xd6\xe1&6\x00\xdd\xff\xe4\x05i\xf2\x82\xca\xf3\x95UX\xa4'
 b'\xac\x1e?'))

# H - uint16 2
# h - int16 2
# I - uint32 4
# i - int32 4
# b - int8 1
# B - uint8 1
# q - int64 8
# Q - uint64 8
# f - float 4