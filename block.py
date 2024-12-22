from sha256 import sha256 as hash
from merkleTree import MerkleTree
from datetime import datetime 

class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = str(datetime.now())
        self.merkle_root = MerkleTree(transactions).merkle_root
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = (
                self.merkle_root +
                str(self.previous_hash) +
                self.timestamp
        )
        return hash(block_data)