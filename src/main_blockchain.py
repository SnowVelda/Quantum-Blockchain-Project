import hashlib
import json
from time import time
import oqs

# --- Transaction Class ---
class Transaction:
    def __init__(self, from_address, to_address, amount):
        self.from_address = from_address
        self.to_address = to_address
        self.amount = amount
        self.timestamp = time()
        self.signature = None

    def calculate_hash(self):
        """Creates a SHA-256 hash of the transaction."""
        tx_string = json.dumps({
            "from": self.from_address,
            "to": self.to_address,
            "amount": self.amount,
            "timestamp": self.timestamp
        }, sort_keys=True).encode()
        return hashlib.sha256(tx_string).hexdigest()

    def sign_transaction(self, signing_key):
        """Sign transaction with the private key (sk) of the sender."""
        if self.from_address is None:
            raise ValueError("Cannot sign transactions from a genesis block.")
        
        tx_hash = self.calculate_hash()
        with oqs.Signature("Dilithium2") as sig:
            self.signature = sig.sign(tx_hash.encode(), signing_key)

    def is_valid(self):
        """Validate the transaction signature."""
        if self.from_address is None: # Genesis transactions are valid by default
            return True
        if not self.signature:
            raise ValueError("Transaction is not signed.")

        pk_bytes = bytes.fromhex(self.from_address)
        tx_hash = self.calculate_hash()
        with oqs.Signature("Dilithium2") as sig:
            return sig.verify(tx_hash.encode(), self.signature, pk_bytes)

# --- Block Class ---
class Block:
    def __init__(self, timestamp, transactions, previous_hash=''):
        self.timestamp = timestamp
        self.transactions = [tx.__dict__ for tx in transactions]
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculates the hash of the block."""
        block_string = str(self.timestamp) + json.dumps(self.transactions, sort_keys=True) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """Simple Proof of Work algorithm."""
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block Mined: {self.hash}")

# --- Blockchain Class ---
class QuantumBlockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_transactions = []
        self.mining_reward = 100

    def create_genesis_block(self):
        """Creates the very first block in the chain."""
        return Block(time(), [Transaction(None, "genesis_address", 0)], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        """Mines pending transactions and adds a new block to the chain."""
        reward_tx = Transaction(None, mining_reward_address, self.mining_reward)
        self.pending_transactions.append(reward_tx)

        new_block = Block(time(), self.pending_transactions, self.get_latest_block().hash)
        new_block.mine_block(self.difficulty)

        print("Block successfully mined!")
        self.chain.append(new_block)
        self.pending_transactions = []

    def add_transaction(self, transaction):
        """Adds a new transaction to the list of pending transactions."""
        if not transaction.from_address or not transaction.to_address:
            raise ValueError("Transaction must include a from and to address.")
        if not transaction.is_valid():
            raise ValueError("Cannot add an invalid transaction to the chain.")
        self.pending_transactions.append(transaction)

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

# --- Main Execution ---
if __name__ == '__main__':
    # 1. Create wallets with quantum-resistant keypairs using liboqs
    print("Generating quantum-resistant wallets...")
    with oqs.Signature("Dilithium2") as sig:
        # Wallet 1
        pk1 = sig.generate_keypair()
        sk1 = sig.export_secret_key()
        # Wallet 2
        pk2 = sig.generate_keypair()
        sk2 = sig.export_secret_key()

    wallet1_address = pk1.hex() # Public key is the wallet address
    wallet2_address = pk2.hex()
    print(f"Wallet 1 Address: {wallet1_address[:15]}...")
    print(f"Wallet 2 Address: {wallet2_address[:15]}...")

    # 2. Create a new blockchain instance
    qbc = QuantumBlockchain()

    # 3. Create and sign a transaction
    print("\nCreating a transaction from Wallet 1 to Wallet 2...")
    tx1 = Transaction(wallet1_address, wallet2_address, 10)
    tx1.sign_transaction(sk1) # Sign with Wallet 1's private key
    qbc.add_transaction(tx1)
    print("Transaction signed and added to pending transactions.")

    # 4. Mine the block
    print("\nMining pending transactions... (This will take a moment)")
    # The miner (Wallet 1 in this case) gets a reward
    qbc.mine_pending_transactions(mining_reward_address=wallet1_address)

    # 5. Verify the blockchain's integrity
    print(f"\nIs the blockchain valid? {qbc.is_chain_valid()}")

    # 6. Print the blockchain content
    print("\n--- Blockchain Content ---")
    for i, block in enumerate(qbc.chain):
        print(f"Block {i}:")
        print(f"  Hash: {block.hash}")
        print(f"  Previous Hash: {block.previous_hash}")
        print("  Transactions:")
        for tx in block.transactions:
            print(f"    - From: {tx['from_address'][:10] if tx['from_address'] else 'MINING_REWARD'}... To: {tx['to_address'][:10]}... Amount: {tx['amount']}")