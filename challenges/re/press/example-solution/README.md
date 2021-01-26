# press

**Points:** 350 (326 after dynamic scoring)

**Flag:** RTN{A_Smaller_Alph4b3t_r3qu1r3s_A_sm4ll3r_Am0un7_0f_b1ts}

Press is a relatively simple native RE challenge. This writeup assumes the linux binary.

The binary asks for an input, which is fed into a compression function as decompiled by Ghidra below:

```c
char * compress(char *input,size_t size,size_t *final_size)
{
    byte b;
    char *ptr;
    uint j;
    int i;
    int k;
  
    ptr = calloc(size,1);
    j = 0;
    i = 0;
    while (i < size) {
        b = b_index(input[i]);
        k = 0;
        while (k < 6) {
            ptr[j >> 3] = ptr[j >> 3] | (b >> (k & 0x1f) & 1U) << (j & 7);
            j += 1;
            k += 1;
        }
        i += 1;
    }
    *final_size = (j >> 3) + 1;
    return ptr;
}

uint b_index(char c)
{
    uint i;
  
    i = 0;
    while( true ) {
        if (0x3f < i) {
            return 0xffffffff;
        }
        if (c == "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"[i]) break;
        i += 1;
    }
    return i;
}
```

The key take-away from this is that it looks up the index for every character in a predefined alphabet (`b_index`), and then translates these numbers into a 6-bit number (the inner while loop). These bits are then stitched together without any zero bits in between, as would be the case with a normal 8-bit byte. The solution is to simply do the reverse (see `solve.py`).
