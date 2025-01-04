from transaction import Transaction
from blockchain import Blockchain


def main():
    blockchain = Blockchain({
        "Viktor": 100, 
        "Batyrkhan": 50,
        "Islambek": 1000
    })
    
    txs = [
        Transaction("Viktor", "Batyrkhan", 30),
        Transaction("Batyrkhan", "Viktor", 10),
        Transaction("Islambek", "Dilyara", 10),
        Transaction("Islambek", "Sanzhar", 13),
        Transaction("Islambek", "Seraphim", 100), # 5
        Transaction("Islambek", "Nurdaulet", 10),
        Transaction("Islambek", "Viktor", 10),
        Transaction("Islambek", "Batyrkhan", 10),
        Transaction("Viktor", "Sanzhar", 10),
        Transaction("Islambek", "Daulet", 10), # 10
        Transaction("Sanzhar", "Islambek", 10),
        Transaction("Dilyara", "Seraphim", 10),
    ]

    
    # Add transaction to the pool
    for tx in txs:
        blockchain.add_transaction(tx)
    
    # Mining block
    blockchain.mine_block()
    
    print("Balances:", blockchain._balances)

    print(f"Validate_blockchain: {blockchain.validate_blockchain()}")
    
    # Print blocks
    i = 0
    for block in blockchain._chain:
        print(f"Block {i}")
        print(f"Hash: {block.hash}")
        print(f"Previous hash: {block.previous_hash}")
        print(f"Root of Merkle tree: {block.merkle_root}")
        print(f"Transactions: {block.transactions}")
        print("----")
        i+=1

if __name__ == "__main__":    
    main()