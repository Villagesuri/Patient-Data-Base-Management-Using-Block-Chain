import hashlib
import json
from time import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        # Create the genesis block with arbitrary proof and previous hash
        self.create_block(proof=100, previous_hash='1')

    def create_block(self, proof, previous_hash):
        """
        Create a new block and add it to the chain
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'data': self.current_data,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.current_data = []  # Clear current data
        self.chain.append(block)
        return block

    def get_last_block(self):
        """
        Return the last block in the chain
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        """
        Simple Proof of Work Algorithm
        """
        proof = 0
        while not self.valid_proof(previous_proof, proof):
            proof += 1
        return proof

    @staticmethod
    def valid_proof(previous_proof, proof):
        """
        Check if hash(previous_proof + proof) starts with 4 zeros
        """
        guess = f'{previous_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a block
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def add_patient_data(self, patient_id, name, age, diagnosis):
        """
        Add new patient data to the list of data
        """
        self.current_data.append({
            'patient_id': patient_id,
            'name': name,
            'age': age,
            'diagnosis': diagnosis
        })
        return self.get_last_block()['index'] + 1

    def is_chain_valid(self):
        """
        Check if the blockchain is valid
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Verify hash linkage
            if current['previous_hash'] != self.hash(previous):
                return False

            # Verify proof of work
            if not self.valid_proof(previous['proof'], current['proof']):
                return False

        return True


# Usage Example
if __name__ == "__main__":
    blockchain = Blockchain()

    # Add some patient data
    print("Adding patient data...")
    blockchain.add_patient_data("P001", "Surya", 30, "Fever")
    blockchain.add_patient_data("P002", "Suresh", 40, "Common cold")

    # Mine a new block to add patient data to the blockchain
    last_proof = blockchain.get_last_block()['proof']
    proof = blockchain.proof_of_work(last_proof)
    previous_hash = blockchain.hash(blockchain.get_last_block())
    block = blockchain.create_block(proof, previous_hash)

    print(f"\nNew Block Mined: {json.dumps(block, indent=4)}")

    # Validate the blockchain
    print("\nIs Blockchain valid?", blockchain.is_chain_valid())

    # Print the entire blockchain
    print("\nFull Blockchain:")
    for blk in blockchain.chain:
        print(json.dumps(blk, indent=4))
