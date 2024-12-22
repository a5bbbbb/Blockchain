class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = None

    def sign_transaction(self, private_key):
        if self.sender == "SYSTEM":  
            return
        data = f"{self.sender}{self.receiver}{self.amount}"
        self.signature = self.simple_hash(data + private_key)

    def is_valid(self):
        if self.sender == "SYSTEM":
            return True  
        if not self.signature:
            return False  
        data = f"{self.sender}{self.receiver}{self.amount}"
        return self.signature == self.simple_hash(data + self.sender)

    def simple_hash(self, data):
        hash_value = sum(bytearray(data, 'utf-8'))
        return str(hash_value)  
