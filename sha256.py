
def sha256(obj) -> str:
    '''A method that returns the hash hex of the serialized object or string following sha256 algorithm. The object must have self.__str__() implemented.'''
    data = bytearray(str(obj),"ascii")
    H = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]

    K = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]

    length = len(data) * 8
    data.append(0x80)
    while (len(data) * 8 + 64) % 512 != 0:
        data.append(0x00)

    data += length.to_bytes(8, 'big')

    blocks = [] 
    for i in range(0, len(data), 64):
        blocks.append(data[i:i+64])


    for data_block in blocks:
        data_schedule = []
        for t in range(0, 64):
            if t <= 15:
                data_schedule.append(bytes(data_block[t*4:(t*4)+4]))
            else:
                term1 = _s1(int.from_bytes(data_schedule[t-2], 'big'))
                term2 = int.from_bytes(data_schedule[t-7], 'big')
                term3 = _s0(int.from_bytes(data_schedule[t-15], 'big'))
                term4 = int.from_bytes(data_schedule[t-16], 'big')
                schedule = ((term1 + term2 + term3 + term4) % 2**32).to_bytes(4, 'big')
                data_schedule.append(schedule)

        a = H[0]
        b = H[1]
        c = H[2]
        d = H[3]
        e = H[4]
        f = H[5]
        g = H[6]
        h = H[7]

        for t in range(64):
            t1 = ((h + _cs1(e) + _ch(e, f, g) + K[t] +
                   int.from_bytes(data_schedule[t], 'big')) % 2**32)

            t2 = (_cs0(a) + _maj(a, b, c)) % 2**32

            h = g
            g = f
            f = e
            e = (d + t1) % 2**32
            d = c
            c = b
            b = a
            a = (t1 + t2) % 2**32

        H[0] = (H[0] + a) % 2**32
        H[1] = (H[1] + b) % 2**32
        H[2] = (H[2] + c) % 2**32
        H[3] = (H[3] + d) % 2**32
        H[4] = (H[4] + e) % 2**32
        H[5] = (H[5] + f) % 2**32
        H[6] = (H[6] + g) % 2**32
        H[7] = (H[7] + h) % 2**32

    return ((H[0]).to_bytes(4, 'big') + (H[1]).to_bytes(4, 'big') +
            (H[2]).to_bytes(4, 'big') + (H[3]).to_bytes(4, 'big') +
            (H[4]).to_bytes(4, 'big') + (H[5]).to_bytes(4, 'big') +
            (H[6]).to_bytes(4, 'big') + (H[7]).to_bytes(4, 'big')).hex()

def _s0(num):
    num = (
    _rotate_r(num, 7)^
    _rotate_r(num, 18)^
    (num >> 3)
    )
    return num

def _s1(num):
    num = (
    _rotate_r(num, 17)^
    _rotate_r(num, 19)^
    (num >> 10)
    )
    return num

def _cs0(num):
    num = (
    _rotate_r(num, 2)^
    _rotate_r(num, 13)^
    _rotate_r(num, 22)
    )
    return num

def _cs1(num):
    num = (
    _rotate_r(num, 6)^
    _rotate_r(num, 11)^
    _rotate_r(num, 25)
    )
    return num

def _ch(x , y , z):
    return (x & y) ^ (~x & z)

def _maj(x , y , z):
    return (x & y) ^ (x & z) ^ (y & z)

def _rotate_r(n , sh , s  = 32):
    return (n>>sh) | (n<<s - sh)



