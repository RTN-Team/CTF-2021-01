saturn
======

**Points:** 600 (596 after dynamic scoring)

**Flag:** RTN{4r3_y0u_SATisf13d}

This challenge contains lots of code, which might seem overwhelming at first. However, most of it is not relevant to solving the challenge. This writeup assumes the linux variant.

The application asks for a launch code of 22 letters,  which is then ran through a bunch of XOR formulae, and finally compared to a hardcoded string of bytes (`FUN_00102799`). To find the solution to these equations, you can use a SAT solver. `solve.py` provides a sample implementation for this  using z3.
