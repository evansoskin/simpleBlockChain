from helpers import getCurrentDateTime
from Block import Block
from Transaction import Transaction


# BlockChain Class
class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 2
        self.miningReward = 100
        self.pendingTransactions = []
        self.chain.append(self.createGenesisBlock())

    def createGenesisBlock(self):
        genesisTransactions = []
        genesisTransactions.append(Transaction(None, None, 0))
        genesisTransactions.append(Transaction(None, None, 0))
        gb = Block(getCurrentDateTime(), genesisTransactions)
        gb.mineBlock(self.difficulty)
        return gb

    def getLatestBlock(self):
        return self.chain[len(self.chain) - 1]

    def minePendingTransactions(self, miningRewardAddress):
        self.addTransaction(Transaction(None, miningRewardAddress, self.miningReward))
        newBlock = Block(getCurrentDateTime(), self.pendingTransactions[:])
        newBlock.mineBlock(self.difficulty)

        print("Block Successfully mined")
        self.chain.append(newBlock)

        self.pendingTransactions.clear()

    def addTransaction(self, transaction):
        # If there isn't a from or to address, error, None is ok
        if transaction.toAddress == None:
            print("no addresses given")
            exit()

        if not transaction.isValid():
            print("Cannot add invalid transaction to chain")
            exit()

        self.pendingTransactions.append(transaction)

    def getAddressBalance(self, address):
        balance = 0

        for block in self.chain:
            for trans in block.transactions:
                if trans.toAddress == None:
                    continue
                if trans.toAddress == address:
                    balance += trans.amount
                elif trans.fromAddress == address:
                    balance -= trans.amount
                else:
                    pass

        return balance

    def isChainValid(self):
        for block in range(len(self.chain)):
            if block == 0:
                continue
            currentBlock = self.chain[block]
            previousBlock = self.chain[block - 1]

            if currentBlock.hash != currentBlock.hash:
                return False
            if currentBlock.previousHash != previousBlock.hash:
                return False

            if not currentBlock.hasValidTransactions():
                return False

        return True

    """
    def printBlockTransactions(self):
        for block in self.chain:
            for trans in block.transactions:
                trans.printTransaction()
    """