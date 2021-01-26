from Crypto.Protocol.SecretSharing import Shamir
from Crypto.Cipher import AES 
from Crypto.Util.Padding import unpad

ciphertext = bytes.fromhex("6eeb7683e9242ed56080e847c2f94cfc50634c29a3a50f14b31e7e3f97e34df0")

shares = [
    (1, bytes.fromhex("d8877abe8c795a869b1fe28ed9a328a4")),
    (2, bytes.fromhex("1a1c134fc5c474899ee9d573b8895388")),
    (3, bytes.fromhex("da143ab7a656e69a91b22414de846d0e")),
    (4, bytes.fromhex("e4c6d40f50bd5f37d5c2f5e356a0af94")),
    (5, bytes.fromhex("f344401d9a20a8ea1f08598434bfbf8e"))
]

key = Shamir.combine(shares, ssss=True)
print(f"Reconstructed key: {key.hex()} ({key})")

cipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(cipher.decrypt(ciphertext), len(key))
print("Decrypted text:", decrypted)