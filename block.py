from sha256 import sha256 as hash
from merkleTree import MerkleTree

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = "2024-12-21"
        self.nonce = 0
        self.merkle_root = MerkleTree(transactions).merkle_root
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        block_data = (
                str(self.index) +
                self.merkle_root +
                self.previous_hash +
                self.timestamp +
                str(self.nonce)
        )
        return hash(block_data)
    def mine_block(self, difficulty):
        while not self.hash.startswith('0' * difficulty):
            self.nonce += 1
            self.hash = self.calculate_hash()