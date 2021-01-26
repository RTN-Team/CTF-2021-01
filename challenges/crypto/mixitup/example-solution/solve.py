
with open("image1.bmp", "rb") as f:
    image1 = f.read()

with open("image2.bmp", "rb") as f:
    image2 = f.read()

with open("output.bmp", "wb") as f:
    # Write BMP header
    f.write(image1[:54])

    # XOR pixel data.
    f.write(bytes([a^b for a, b in zip(image1[54:], image2[54:])]))
