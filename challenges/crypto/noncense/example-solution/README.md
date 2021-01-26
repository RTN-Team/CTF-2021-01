# Noncense

**Points:** 800 (

**Flag:** RTN{h0W_mUcH_m0r3_n0nS3ns3_d0_Y0u_w4Nt}

# Overview

This challenge tests the users skill in analyzing and breaking weak cryptography implementations.
At the start of the challenge, the user is given a bunch of ECDSA signatures and pdf documents that they can verify against, as well as two public SSH keys.
The documents hint the user that a crypto weakness is present, and that the goal is to log into the SSH server to get hold of a secret document (the flag).

## Analysis

When the user analyzes the given signatures' parameters, he will realize, that some signatures have the same values for either r.
This is an indicator that during the generation of the signatures, the nonce is not a random, but a static value.
This can be abused to recover the private value d, and allows to forge a private ssh key to log into the server.
This weakness was exploited in the wild, and used to jailbreak the PlayStation 3.

## Scripts

`generate.py`: Generates keypairs + vulnerable signatures
`forge_key.py`: Generates a private SSH key from the signatures and the documents (This is the example solution)

## Tools

The following tools can be helpful when solving this challenge:

- dumpasn1
- pycryptodome
- https://keytool.online/
