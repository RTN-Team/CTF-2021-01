clavdivs
========

**Points:** 100 (50 after dynamic scoring)

**Flag:** RTN{4v3_Caes4r_M0r1tur1_T3_S4lutant}

The text AVE CLAVDIVS, or Avé Claudius (Caesar), is a reference to the Caesar shift cipher, where characters are shifted by 3 places in the alphabet. This challenge, however, does not use a shift of 3 letters, but it is easy to figure out the actual shift. By looping over all possible shift values and trying them as key, we can simply look at the one that results in a string that resembles a flag. See `solve.py` for an example solution.
