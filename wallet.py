import json
from transaction import Transaction
from rsa import RSA
import os


class Wallet:
    def __init__(self):
        self.rsa = RSA()
        self.private_key, self.public_key = self.rsa.generate_keys()
        self.database_file = os.path.join(os.getcwd(), "transactions.txt")

    def create_transaction(self, receiver, amount):
        transaction = Transaction(self.public_key, receiver, amount)
        transaction.sign(self.private_key)
        self.save_transaction(transaction)
        print(f"Transaction created and saved: {transaction}")

    def save_transaction(self, transaction):
        with open(self.database_file, "a") as db:  # "a" for data to the file
            db.write(json.dumps({
                "sender": transaction.sender,
                "receiver": transaction.receiver,
                "amount": transaction.amount,
                "signature": transaction._signature
            }) + "\n")

    def get_transactions(self):
        transactions = []
        try:
            with open(self.database_file, "r") as db:
                for line in db:
                    tx_data = json.loads(line.strip())
                    transaction = Transaction(
                        tx_data["sender"], tx_data["receiver"], tx_data["amount"]
                    )
                    transaction._signature = tx_data["_signature"]
                    transactions.append(transaction)
        except FileNotFoundError:
            print("No transactions database found.")
        return transactions
