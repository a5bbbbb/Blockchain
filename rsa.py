import random

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime():
    while True:
        num = random.randint(100, 200)
        if is_prime(num):
            return num

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def generate_keys():
    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = mod_inverse(e, phi)
    
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

def encrypt(plain_text, public_key):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in plain_text]
    return cipher_text

def decrypt(cipher_text, private_key):
    d, n = private_key
    plain_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return plain_text

public_key, private_key = generate_keys()
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")

message = "Hello!"
print(f"Original Message: {message}")

cipher_text = encrypt(message, public_key)
print(f"Cipher Text: {cipher_text}")

decrypted_message = decrypt(cipher_text, private_key)
print(f"Decrypted Message: {decrypted_message}")
