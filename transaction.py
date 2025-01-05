from digitalsignature import DigitalSignature

class Transaction:
    digitalSignature = DigitalSignature()
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self._signature = []
    
    def __str__(self):
        return f"{self.sender}${self.receiver}${self.amount}"
    
    def sign(self, private_key):
        self._signature = Transaction.digitalSignature.sign(private_key, self.__str__())

    def verify(self):
        signature_content = Transaction.digitalSignature.verify(self.sender, self.__str__(), self._signature)
        if signature_content != self.__str__():
            raise ValueError(f"Verify transaction={self.__str__()} : Document is wrong")
        return True



