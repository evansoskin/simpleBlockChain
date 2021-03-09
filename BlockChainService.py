from Blockchain import Blockchain
from ecdsa import SigningKey, SECP256k1

class BlockchainService:
    blockchainInstance = Blockchain()
    walletKeys = {}

    def __init__(self):
        self.blockchainInstance.difficulty = 2
        self.blockchainInstance.minePendingTransactions("myWalletAddress")
        
        self.generateWalletKeys()

    def generateWalletKeys(self):
        sk = SigningKey.generate(curve=SECP256k1)
        pk = sk.verifying_key

        self.walletKeys["publicKey"] = pk.to_string().hex()
        self.walletKeys["privateKey"] = sk.to_string().hex()

    def getBlocks(self):
        return self.blockchainInstance.chain

    def getBlockByHash(self, hashOfBlock):
        for block in self.blockchainInstance.chain:
            if block.hash == hashOfBlock:
                return self.blockchainInstance.chain['block']
        return None