import random
class RSA:
    @staticmethod
    def _is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def _generate_prime():
        while True:
            num = random.randint(1000, 1000000)
            if RSA._is_prime(num):
                return num

    @staticmethod
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def _mod_inverse( a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    def generate_keys(self):
        p = RSA._generate_prime()
        q = RSA._generate_prime()
        n = p * q
        phi = (p - 1) * (q - 1)
        
        e = random.randint(2, phi - 1)
        while RSA._gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
        
        d = RSA._mod_inverse(e, phi)
        
        public_key = (e, n)
        private_key = (d, n)
        
        return public_key, private_key

    def encrypt(self, plain_text, private_key):
        d, n = private_key
        cipher_text = [pow(ord(char), d, n) for char in plain_text]
        return cipher_text

    def decrypt(self, cipher_text, public_key):
        e, n = public_key
        plain_text = ''.join([chr(pow(char, e, n)) for char in cipher_text])
        return plain_text
    
if __name__ == "__main__":
    public_key, private_key = RSA.generate_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    message = "Hello!"
    print(f"Original Message: {message}")

    cipher_text = RSA.encrypt(message, private_key)
    print(f"Cipher Text: {cipher_text}")

    decrypted_message = RSA.decrypt(cipher_text, public_key)
    print(f"Decrypted Message: {decrypted_message}")
