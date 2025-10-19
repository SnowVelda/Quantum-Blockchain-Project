import hashlib
import random

class Chapter3:
    def __init__(self):
        self.name = "The Blockchain of Trust"
        self.year = 2042
        self.story = "After escaping the quantum entanglement, Echo Prime guides you to a memory from 2042. This was a time when I was trying to rebuild my life, but the world was skeptical. Trust was a currency, and mine was devalued. Chronos is corrupting the historical blockchain, trying to erase my contributions and perpetuate the narrative of my past. You must validate the integrity of the blockchain."
        self.puzzle_description = "You need to verify the integrity of a simulated blockchain. Find the correct nonce to mine a block or identify corrupted blocks."

    def create_block(self, index, timestamp, data, previous_hash, nonce=0):
        block_string = f"{index}{timestamp}{data}{previous_hash}{nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, index, timestamp, data, previous_hash, difficulty=4):
        nonce = 0
        while True:
            current_hash = self.create_block(index, timestamp, data, previous_hash, nonce)
            if current_hash.startswith('0' * difficulty):
                return nonce, current_hash
            nonce += 1

    def play_chapter(self, game):
        print(self.story)
        print(self.puzzle_description)

        # Simulate a simple blockchain
        blockchain = []
        previous_hash = "0"
        
        # Create genesis block
        nonce, block_hash = self.mine_block(0, "2042-01-01", "Genesis Block", previous_hash)
        blockchain.append({"index": 0, "timestamp": "2042-01-01", "data": "Genesis Block", "previous_hash": previous_hash, "nonce": nonce, "hash": block_hash})
        previous_hash = block_hash

        # Add a few more blocks
        for i in range(1, 4):
            data = f"Transaction {i}"
            nonce, block_hash = self.mine_block(i, f"2042-01-0{i+1}", data, previous_hash)
            blockchain.append({"index": i, "timestamp": f"2042-01-0{i+1}", "data": data, "previous_hash": previous_hash, "nonce": nonce, "hash": block_hash})
            previous_hash = block_hash

        # Introduce a random corruption
        corrupted_block_index = random.randint(1, len(blockchain) - 1)
        original_data = blockchain[corrupted_block_index]["data"]
        blockchain[corrupted_block_index]["data"] = "CORRUPTED DATA"
        print(f"\nChronos has corrupted Block {corrupted_block_index}!")

        print("\nBlockchain State:")
        for block in blockchain:
            print(f"Block {block['index']}: Hash={block['hash']}, Data={block['data']}")

        print("\nYour task is to identify the corrupted block and fix it by re-mining it with the original data.")
        
        while True:
            action = input("Enter the index of the block you want to verify/fix (or 'quit'): ").lower().strip()
            if action == 'quit':
                print("You failed to validate the blockchain. Chronos wins this round.")
                break
            try:
                block_index = int(action)
                if 0 <= block_index < len(blockchain):
                    block = blockchain[block_index]
                    calculated_hash = self.create_block(block["index"], block["timestamp"], block["data"], block["previous_hash"], block["nonce"])
                    
                    if calculated_hash == block["hash"]:
                        print(f"Block {block_index} is valid.")
                        if block_index == corrupted_block_index and block["data"] == original_data: # Check if fixed
                            print("You have successfully fixed the corrupted block!")
                            game.player_data["year"] = 2043 # Advance time
                            print("A memory of trust restored: your contributions are validated!")
                            break
                    else:
                        print(f"Block {block_index} is corrupted! Its hash does not match its content.")
                        fix_choice = input("Do you want to fix this block with the original data? (yes/no): ").lower().strip()
                        if fix_choice == 'yes':
                            blockchain[block_index]["data"] = original_data
                            new_nonce, new_hash = self.mine_block(block["index"], block["timestamp"], original_data, block["previous_hash"])
                            blockchain[block_index]["nonce"] = new_nonce
                            blockchain[block_index]["hash"] = new_hash
                            print(f"Block {block_index} has been re-mined and fixed.")
                            # Re-verify the entire chain from this point to ensure integrity
                            is_chain_valid = True
                            for i in range(block_index, len(blockchain)):
                                current_b = blockchain[i]
                                prev_b = blockchain[i-1] if i > 0 else None
                                if self.create_block(current_b["index"], current_b["timestamp"], current_b["data"], current_b["previous_hash"], current_b["nonce"]) != current_b["hash"]:
                                    is_chain_valid = False
                                    break
                                if prev_b and current_b["previous_hash"] != prev_b["hash"]:
                                    is_chain_valid = False
                                    break
                            if is_chain_valid:
                                print("The entire blockchain is now valid!")
                                game.player_data["year"] = 2043 # Advance time
                                print("A memory of trust restored: your contributions are validated!")
                                break
                            else:
                                print("Fixing this block caused further issues down the chain. Keep trying!")
                        else:
                            print("Block not fixed.")
                else:
                    print("Invalid block index.")
            except ValueError:
                print("Invalid input. Please enter a number or 'quit'.")

        print("\nChapter 3 complete.")
