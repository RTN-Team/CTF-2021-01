reverseme
=========

**Points:** 200 (150 after dynamic scoring)

**Flag:** RTN{1tty_B1tty_B1t_sh1ft5}

The algorithm implemented is reversing each bit of every byte in the input, and then reverses the result as well, effectively just reversing the entire bitstream. To get to the flag, you simply have to call the same function again, but on the hardcoded bitstream that is compared with.
