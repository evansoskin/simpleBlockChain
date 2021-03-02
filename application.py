from helpers import getCurrentDateTime
from Block import Block
from BlockChain import BlockChain
from Transaction import Transaction
from ecdsa import SigningKey, VerifyingKey, SECP256k1

# Main
def main():

    # create private key
    myKey = SigningKey.from_string(b'\x02=\x0c\xab\x89mC\x87v\xc7\x8e7u\x93\t\xc4+\xc3 _\x80bs;\xa5\x9d/\x9bE\x9b\x8b\xcf', curve=SECP256k1)
    # get public key from private key
    # c5a345488032ccd848b14b12503f57fae5b11c083daded9ecf70a966f4c744b2d4f234779a047c826af8277b719db508
    myWalletAddress = myKey.verifying_key

    # 7330f1fedf3d74d37a5728e67083da04adff3a84ba88a107c91bc37d7d17221250dc7178f26e10f589dc3156674ed8f8
    toWalletAddress = VerifyingKey.from_string(b"\x12\xd5gn\xfd\xe1\xb0c\x8cX=n\xa1\x131Mp\xb4\xeaz[M4N\x18\xf6\x8bL\xcb\xcbhU\r\xd6]\xe1b\x16;\xb6!'N\x87\xdc*\xf6w\x1b\x92#\x0b\x84\xb6\x86\xeb\xed1\x1d\x87\x1e\xef\xc3\xfd", curve=SECP256k1)

    BC = BlockChain()
    print("BlockChain created")

    trans1 = Transaction(myWalletAddress, toWalletAddress, 10)
    trans1.signTransaction(myKey)
    BC.addTransaction(trans1)


    print("start miner")
    BC.minePendingTransactions(myWalletAddress)
    print("My balance:")
    #BC.printBlockTransactions()
    print(BC.getAddressBalance(myWalletAddress))
    #print(BC.getAddressBalance("address2"))
    #print(BC.getAddressBalance("miner"))
    #BC.minePendingTransactions("miner")
    #print(BC.getAddressBalance("miner"))
    print(BC.isChainValid())

main()