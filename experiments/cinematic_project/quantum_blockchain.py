import hashlib
import time
from quantum_core import QuantumEmotionalState

class Block:
    def __init__(self, timestamp, data, previous_hash, emotional_state):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.emotional_state = emotional_state
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculates the hash of the block, incorporating the emotional state."""
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.emotional_state)
        return hashlib.sha256(hash_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Creates the first block in the chain."""
        return Block(time.time(), "1610ab34ef41ff5fdb6649feb4295e2b28985f06c62ad5bdfb5a1a46659f3cb7", "0", {})

    def get_latest_block(self):
        """Returns the most recent block in the chain."""
        return self.chain[-1]

    def add_block(self, new_block):
        """Adds a new block to the chain."""
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Determines if the blockchain is valid."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
