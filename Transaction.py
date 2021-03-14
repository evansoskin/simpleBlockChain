from hashlib import sha256
from helpers import getCurrentDateTime
from ecdsa import SigningKey, SECP256k1


# Transaction Class
class Transaction:
    def __init__(self, fromAddress = None, toAddress = None, amount = 0):
        self.fromAddress = fromAddress
        self.toAddress = toAddress
        self.amount = amount
        self.timestamp = getCurrentDateTime()
        self.signature = None

    def printTransaction(self):
        if self.fromAddress == None and self.toAddress != None:
            print("{ fromAddress: " + "\n  toAddress: " + self.toAddress + "\n  amount: " + str(self.amount) + "\n}")
        elif self.fromAddress != None and self.toAddress == None:
            print("{ fromAddress: " + self.fromAddress + "\n  toAddress: " + "\n  amount: " + str(self.amount) + "\n}")
        elif self.fromAddress == None and self.toAddress == None:
            print("{ fromAddress: " + "\n  toAddress: " + "\n  amount: " + str(self.amount) + "\n}")
        else:
            print("{ fromAddress: " + self.fromAddress + "\n  toAddress: " + self.toAddress + "\n  amount: " + str(self.amount) + "\n}")

    def calculateHash(self):
        return sha256(self.fromAddress.to_string() + self.toAddress.to_string() + bytearray(str(self.amount), "utf-8") + bytearray(self.timestamp, "utf-8")).hexdigest()

    def signTransaction(self, signingKey):

        if  signingKey.verifying_key != self.fromAddress:
            print("You cannot sign transactions for other wallets")
            exit()

        hashTrans = bytearray.fromhex(self.calculateHash())
        sig = signingKey.sign(hashTrans)
        self.signature = sig.hex()

    def isValid(self):
        # Check if fromAddress is None (miningBlock reward)
        if self.fromAddress == None:
            return True
        # check if signature is valid
        if not self.signature or self.signature == None:
            print("no signature")
            exit()

        return self.fromAddress.verify(bytearray.fromhex(self.signature), bytearray.fromhex(self.calculateHash()))
