ALPHABET = b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

compressed_flag = bytes.fromhex("9acf32c0b21091af2dcf8107f7e4473744d5d12df99a2f31f8b2dc91af3134d5ec3e5df8413d4900")

output = bytearray()

i = 0
val = 0
for x in range((len(compressed_flag)-1) * 8):
    bit_index = x % 8
    byte_index = x // 8

    bit = (compressed_flag[byte_index] >> bit_index) & 1
    val |= bit << i

    i += 1
    if i == 6:
        output.append(ALPHABET[val])
        val = 0
        i = 0

print(f"RTN{{{output.decode()}}}")