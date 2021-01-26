mixitup
=======

**Points:** 200 (150 after dynamic scoring)

**Flag:** `RTN{4dd_Str4b3rr13s_X0r_B4n4n4s}`

The hint message mentions the word `eXclusively`, which is a reference to XOR. If we XOR the pixel data together of both images (and skip the first 54 bytes that make up the bmp header), we get an image of a smoothie with the flag.
