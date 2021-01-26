radish
======

**Points:** 300 (288 after dynamic scoring)

**Flag:** RTN{r4d1x_m4l0rum_3st_cup1d1t4s}

The key is to recognize the algorithm that is implemented is encoding the input as base32. This can be recognized by either trying different inputs/outputs, and/or recognizing the `=` (0x61 in hex) characters that are appended at the end of a lot of strings. Also the message refers to radish (radix) being a good Base for smoothies.

The solution is to simply reverse the base32 encoding on the hardcoded data using e.g. CyberChef.
