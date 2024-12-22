class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = None

    def sign_transaction(self, private_key):
        if self.sender == "SYSTEM":  # System transaction, no sign required
            return
        data = f"{self.sender}{self.receiver}{self.amount}"
        self.signature = hash(data.encode('utf-8') + private_key.encode('utf-8')).hexdigest() 

    def is_valid(self):
        if self.sender == "SYSTEM":
            return True  # System transactions always validate
        if not self.signature:
            return False  # Sign should be correctly
        data = f"{self.sender}{self.receiver}{self.amount}"
        return self.signature == hash(data.encode('utf-8') + self.sender.encode('utf-8')).hexdigest()