dragons
=======

**Points:** 150 (100 after dynamic scoring)

**Flag:** RTN{3ND_0F_F1L3_1S_0F73N_1GN0R3D}

If we run `strings` on the PNG file, we can quickly recognize that there is a hidden string stored at the end of the file. This string contains a hint to the affine cipher with key=7, followed up by a ciphertext. The string can be decrypted using CyberChef.
