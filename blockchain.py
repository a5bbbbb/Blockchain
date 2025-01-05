from block import Block
from transaction import Transaction


class Blockchain:
    def __init__(self, balances):
        '''
        To create a blockchain object it is needed to provide a dictionary balances with no more 
        than 10 entries with keys denoting addresses and values specifying the amount.
        The balances will be hardcoded into the genesis block as transactions from the SYSTEM address.
        '''
        self._pending_transactions = []
        self._balances = balances
        transactions = [str(Transaction("SYSTEM", address, amount)) for (address, amount) in balances.items()]
        self._chain = [self._create_genesis_block(transactions)]
    
    def _create_genesis_block(self, transactions):
        return Block(transactions, None)
    
    def _get_latest_block(self):
        return self._chain[-1]
    
    def add_transaction(self, transaction):
        if self._balances.get(transaction.sender, 0) < transaction.amount:
            raise ValueError(
                f"Not enough funds: " +
                f"the {transaction.sender} address has a balance of {self._balances.get(transaction.sender, 0)} " +
                f"and cannot send {transaction.amount}."
                            )
        self._pending_transactions.append(transaction)

        if(len(self._pending_transactions) == 10):
            print("10 pending transactions, calling mine_block()")
            self.mine_block()
    
    def mine_block(self):
        if(len(self._pending_transactions) == 0):
            raise BufferError("No transactions pending")
        transactions_for_block = self._pending_transactions[:10]
        self._pending_transactions = self._pending_transactions[10:]

        block = Block(
            [str(tx) for tx in transactions_for_block], 
            self._get_latest_block().hash
        )

        self._chain.append(block)

        # Update balance
        for tx in transactions_for_block:
            self._balances[tx.receiver] = self._balances.get(tx.receiver, 0) + tx.amount
            if tx.sender != "SYSTEM":
                self._balances[tx.sender] -= tx.amount

    def load_transactions(self, wallet):
        # Loading transactions from database
        transactions = wallet.get_transactions()
        for transaction in transactions:
            try:
                if transaction.verify():
                    self.add_transaction(transaction)
                    print(f"Transaction added: {transaction}")
                else:
                    print(f"Invalid transaction skipped: {transaction}")
            except ValueError as e:
                print(f"Transaction verification failed: {e}")
    
    def validate_blockchain(self):
        print("Checking blockchain with peer nodes.")
        for i in range(1, len(self._chain)):
            current_block = self._chain[i]
            previous_block = self._chain[i - 1]
            # Checking hash of current block
            if current_block.hash != current_block.calculate_hash():
                return False
            # Checking connection to previous block
            if current_block.previous_hash != previous_block.calculate_hash():
                return False
        return True
    