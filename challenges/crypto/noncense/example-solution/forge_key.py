# Event: RTN CTF 2020
# Author: 766F6964 (https://github.com/766F6964)
# Challenge: Noncense
# Description: Solves the challenge by forging a private key using two vulnerable signatures + documents of vgtables

import os
import pathlib
from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Util.asn1 import DerSequence

document_path = os.path.dirname(os.path.realpath(__file__))


def load_signature(filename):
    sig_bytes = pathlib.Path(filename).read_bytes() 
    seq_der = DerSequence()
    sig_params = seq_der.decode(sig_bytes)
    r = sig_params[0]
    s = sig_params[1]
    return r, s 

def calculate_inverse(x, n):
  return pow(x, n-2, n)

def calculate_egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = calculate_egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def calculate_modinv(a, m):
    g, x, y = calculate_egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# 1. Load public key of vgtables
f = open(document_path + "/vgtables.pub",'rt')
pub_key = ECC.import_key(f.read())

# 2. Load two of the vulnerable signatures and get their params (r and s)
r1, s1 = load_signature("document02.sig")
r2, s2 = load_signature("document04.sig")

# 3. Load the digest of the message the sigs are for (the actual documents)
z1 = int(SHA256.new(pathlib.Path(document_path + "/document02.pdf").read_bytes()).hexdigest(), 16)
z2 = int(SHA256.new(pathlib.Path(document_path + "/document04.pdf").read_bytes()).hexdigest(), 16)

# 4. Extract curve order from pub key
p = int(pub_key._curve.order)

# 5. Make sure r1 == r2, otherwise the attack doesnt work
if (r1 != r2):
    print("Attack not possible!")
    exit()
else:
    print("Attack is possible ...")

# 6. Compute nonce k
k = (z1 - z2) * calculate_inverse(s1 - s2, p) % p
print("Calculated nonce:", hex(k))

# 7. Compute private key d
d = ((((s1 * k) % p) - z1) * calculate_modinv(r1, p)) % p
print("Calculated private key:", d)

# 8. Forge ssh private key using computed value d
priv_key = ECC.construct(curve='P-256', d=d, point_x=pub_key.pointQ.x, point_y=pub_key.pointQ.y)

f = open(document_path + "/key_file.pem", "wt")
f.write(priv_key.export_key(format='PEM'))
f.close()
print("Created forged private key !!")