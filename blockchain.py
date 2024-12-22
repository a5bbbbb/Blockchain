from block import Block
from transaction import Transaction
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = [] 
        self.reward = 50  
        self.balances = {};
    def create_genesis_block(self):
        return Block(0, ["Genesis Block"], "0")
    def get_latest_block(self):
        return self.chain[-1]
    def add_transaction(self, transaction):
        if not transaction.is_valid():
            raise ValueError("Transaction is not valid")
        if self.balances.get(transaction.sender, 0) < transaction.amount:
            raise ValueError("Not enough funds")
        self.pending_transactions.append(transaction)
    def mine_block(self, miner_address):
        # Add reward for miners
        reward_transaction = Transaction("SYSTEM", miner_address, self.reward)
        self.pending_transactions.append(reward_transaction)
        # Creating new block
        block = Block(len(self.chain), [str(tx.__dict__) for tx in self.pending_transactions],
        self.get_latest_block().hash)
        block.mine_block(self.difficulty)
        self.chain.append(block)
        # Update balance
        for tx in self.pending_transactions:
            if tx.sender != "SYSTEM":
                self.balances[tx.sender] -= tx.amount
                self.balances[tx.receiver] = self.balances.get(tx.receiver, 0) + tx.amount
        self.pending_transactions = []

    def add_block(self, transactions):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            # Checking hash of current block
            if current_block.hash != current_block.calculate_hash():
                return False
            # Checking connection to previous block
            if current_block.previous_hash != previous_block.hash:
                return False
        return True