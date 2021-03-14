from Blockchain import Blockchain
from ecdsa import SigningKey, VerifyingKey, SECP256k1

class BlockchainService:
    blockchainInstance = Blockchain()
    walletKeys = {}

    def __init__(self):
        self.generateWalletKeys()
        self.blockchainInstance.difficulty = 2
        self.blockchainInstance.miningReward = 100
        self.blockchainInstance.minePendingTransactions(VerifyingKey.from_string( bytearray.fromhex( self.walletKeys["publicKey"] ), curve=SECP256k1 ) )

    def generateWalletKeys(self):
        sk = SigningKey.generate(curve=SECP256k1)
        pk = sk.verifying_key

        self.walletKeys["publicKey"] = pk.to_string().hex()
        self.walletKeys["privateKey"] = sk.to_string().hex()

    def getBlocks(self):
        return self.blockchainInstance.chain

    def getBlockByHash(self, hashOfBlock):
        for idx, block in enumerate(self.blockchainInstance.chain):
            if block.hash == hashOfBlock:
                return self.blockchainInstance.chain[idx]
        return None