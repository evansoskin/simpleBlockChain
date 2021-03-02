# Public/Private Key info
# https://pypi.org/project/ecdsa/
from ecdsa import SigningKey, VerifyingKey, SECP256k1
from hashlib import sha256

# create private key
sk = SigningKey.generate(curve=SECP256k1) # uses NIST192p
print("sk str: ",sk.to_string().hex())

# create public key
pk = sk.verifying_key
print("pk str: ", pk.to_string().hex())

# data to sign
msg = "Message to Hash"
msgHash = sha256(msg.encode("utf-8")).hexdigest()
msgByte = bytearray.fromhex(msgHash)

# sign data with private key
signature = sk.sign(msgByte)
print(signature.hex())

# verify signature with public key
print(pk.verify(signature, msgByte))
