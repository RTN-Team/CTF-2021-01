from smoothiecrypt import encrypt

ciphertext = bytes.fromhex("15e1c8c4bd2fcb12838d3f48e8fc567adf4fac1c36648eb270ad899a717dfadfccd9b49fc32a726711dd1d7faab7ed81")
public_key = bytes.fromhex("537472347762337272795f536d303074686933535f42337374")
private_key = public_key[::-1]

print(encrypt(ciphertext, private_key).decode("utf-8"))
