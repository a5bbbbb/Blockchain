from transaction import Transaction
from blockchain import Blockchain
from wallet import Wallet

def main():
    wallet = Wallet()
    print(f"Wallet public key: {wallet.public_key}")

    blockchain = Blockchain({
        wallet.public_key: 1000,
        "Viktor": 100, 
        "Batyrkhan": 50,
    })
    
    txs = [
        Transaction("Viktor", "Batyrkhan", 30),
        Transaction("Batyrkhan", "Viktor", 10),
        Transaction(wallet.public_key, "Dilyara", 10),
        Transaction(wallet.public_key, "Sanzhar", 13),
        Transaction(wallet.public_key, "Seraphim", 100), # 5
        Transaction(wallet.public_key, "Nurdaulet", 10),
        Transaction(wallet.public_key, "Viktor", 10),
        Transaction(wallet.public_key, "Batyrkhan", 10),
        Transaction("Viktor", "Sanzhar", 10),
        Transaction(wallet.public_key, "Daulet", 10), # 10
        Transaction("Sanzhar", wallet.public_key, 10),
        Transaction("Dilyara", "Seraphim", 10),
    ]

    
    # Add transaction to the pool
    for tx in txs:
        tx.sign(wallet.private_key)
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