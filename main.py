from transaction import Transaction
from blockchain import Blockchain
blockchain = Blockchain()
# Add transactions# blockchain.add_block(["Victor sent 10 coins to Batyrkhan", "Batyrkhan sent Victor 5 coins"])
# blockchain.add_block(["Victor sent Islambek 3 coins"])
def main():
    print("Blockchain validate?", blockchain.validate_chain())
    blockchain.balances["Victor"] = 100
    blockchain.balances["Batyrkhan"] = 50
    tx1 = Transaction("Victor", "Batyrkhan", 30)
    tx1.sign_transaction("Victor")
    tx2 = Transaction("Batyrkhan", "Victor", 10)
    tx2.sign_transaction("Batyrkhan")
    # Add transaction to the pool
    blockchain.add_transaction(tx1)
    blockchain.add_transaction(tx2)
    # Mining block
    blockchain.mine_block("Miner1")
    print("Balances:", blockchain.balances)
    # Print blocks
    for block in blockchain.chain:
        print(f"Block {block.index}")
        print(f"Hash: {block.hash}")
        print(f"Previous hash: {block.previous_hash}")
        print(f"Root of Merkle tree: {block.merkle_root}")
        print(f"Transaction: {block.transactions}")
        print("----")
if __name__ == "__main__":    main()