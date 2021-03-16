from hashlib import sha256
from helpers import getCurrentDateTime
from ecdsa import SigningKey, VerifyingKey, SECP256k1


# Transaction Class
class Transaction:
    def __init__(self, fromAddress = None, toAddress = None, amount = 0):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.timestamp = getCurrentDateTime()
        self.signature = None

    def calculateHash(self):
        return sha256(bytearray.fromhex(self.fromAddress) + bytearray.fromhex(self.toAddress) + bytearray(str(self.amount), "utf-8") + bytearray(self.timestamp, "utf-8")).hexdigest()

    def signTransaction(self, signingKey):


        if  SigningKey.from_string(bytearray.fromhex(signingKey), curve=SECP256k1).verifying_key != VerifyingKey.from_string( bytearray.fromhex( self.fromAddress ), curve=SECP256k1 ):
            print("You cannot sign transactions for other wallets")
            exit()

        hashTrans = bytearray.fromhex(self.calculateHash())
        sig = SigningKey.from_string(bytearray.fromhex(signingKey), curve=SECP256k1).sign(hashTrans)
        self.signature = sig.hex()

    def isValid(self):
        # Check if fromAddress is None (miningBlock reward)
        if self.fromAddress == None:
            return True
        # check if signature is valid
        if not self.signature or self.signature == None:
            print("no signature")
            exit()

        return VerifyingKey.from_string( bytearray.fromhex( self.fromAddress ), curve=SECP256k1 ).verify(bytearray.fromhex(self.signature), bytearray.fromhex(self.calculateHash()))
