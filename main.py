from transaction import Transaction
from blockchain import Blockchain
from wallet import Wallet

def main():
    islambek = Wallet()
    viktor = Wallet()
    batyrkhan = Wallet()
    seraphim = Wallet()
    senders = [islambek, viktor, batyrkhan, seraphim]
    print(f"Wallet public key: {islambek.public_key}")

    blockchain = Blockchain({
        islambek.public_key: 1000,
        viktor.public_key: 1000,
        batyrkhan.public_key: 1000,
        seraphim.public_key: 1000,
    })
    
    txs = [
        Transaction(islambek.public_key, viktor.public_key, 10),
        Transaction(islambek.public_key, seraphim.public_key, 100),
        Transaction(islambek.public_key, viktor.public_key, 10),
        Transaction(islambek.public_key, batyrkhan.public_key, 10),
        Transaction(seraphim.public_key, islambek.public_key, 10),
        Transaction(viktor.public_key, islambek.public_key,  10), 
        Transaction(batyrkhan.public_key, islambek.public_key,  10),
        Transaction(islambek.public_key, seraphim.public_key, 10),
        Transaction(batyrkhan.public_key, viktor.public_key,  10),
        Transaction(seraphim.public_key, viktor.public_key, 10),
    ]

    
    # Add transaction to the pool
    for tx in txs:
        for sender in senders:
            if sender.public_key == tx.sender: 
                tx.sign(sender.private_key)
                blockchain.add_transaction(tx)
    
    tx = Transaction(seraphim.public_key, viktor.public_key, 10)
    tx.sign(seraphim.private_key)
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