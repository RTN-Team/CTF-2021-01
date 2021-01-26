
def decode_flag(value, alphabet):
    # Construct inverse alphabet.
    map_inv = [0]*len(alphabet)
    for i in range(len(alphabet)):
        map_inv[alphabet[i]] = i

    # Apply.
    result = bytearray()
    for i in range(len(value)):
        c = value[i]
        if i % 2 == 1:
            c -= 1
        cc = map_inv[c]
        result.append(cc)

    return result


encoded_flag = b"UwHEpXTXskOHiHFHT9s:W:nHhQsH_tJXhQ8Pa8wm"
alphabet = bytes.fromhex("000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c432e2f614741385777597533633a3b3c3d3e3f40324d2d7b4b74314e7a6445624248726778556b765271346636795b5c5d5e7360304c394a6f58506e6d70537d6968656a564f5f46375435515a49447c6c7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff")

print(decode_flag(encoded_flag, alphabet).decode("utf-8"))