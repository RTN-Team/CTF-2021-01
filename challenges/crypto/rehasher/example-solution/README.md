rehasher
========

**Points:** 450 (450 after dynamic scoring)

The key is to recognize the cipher is a Feistel cipher. Feistel ciphers have the property that decryption is the same as encryption, but with the input key reversed, regardless of what "inner encryption function" is used on each block (in this case the SHA256 hash). To get the flag, simply reverse the "public" key and use it to decrypt the ciphertext.
