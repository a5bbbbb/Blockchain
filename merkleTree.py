from sha256 import sha256 as hash

class MerkleTree:
    def __init__(self, transactions):
        self.transactions = transactions
        self.merkle_root = self.build_merkle_tree()

    def build_merkle_tree(self):
        # Creating a list of hashes for transactions
        current_level = [hash(tx) for tx in self.transactions]

        # Reduce the level until only the root remains.
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                # If the number of nodes is odd, the last one is duplicated.
                if i + 1 < len(current_level):
                    combined = current_level[i] + current_level[i + 1]
                else:
                    combined = current_level[i] + current_level[i]
                next_level.append(hash(combined))
            current_level = next_level

        # Returning tree root
        return current_level[0] if current_level else None
