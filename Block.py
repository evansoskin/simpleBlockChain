from hashlib import sha256
from Transaction import Transaction


# Block Class
class Block:
    def __init__(self, timestamp, transactions, previousHash = ''):
        self.timestamp = timestamp
        self.transactions = transactions
        self.previousHash = previousHash
        self.hash = ''
        self.nonce = 0

    def calculateHash(self):
        return sha256((self.previousHash + self.timestamp + str(self.transactions) + str(self.nonce)).encode("utf-8")).hexdigest()

    def mineBlock(self, difficulty):
        difficulty_str = "0" * difficulty
        while self.hash[0 : difficulty] != difficulty_str:
            self.nonce += 1
            self.hash = self.calculateHash()

    def hasValidTransactions(self):
        for trans in self.transactions:
            if not trans.isValid():
                return False
        return True