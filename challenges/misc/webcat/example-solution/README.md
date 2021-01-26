webcat
======

**Points:** 600 (582 after dynamic scoring)

**Flag:** RTN{R4ther_hav3_a_C4t_th4t_M30w5}

The link refers to a website showing an ascii image of a cat, and a message that it is not impressed by the browser that was used to access the page.

The takeaway from this is that you should not use a webbrowser at all, but start a direct connection using e.g. netcat (hence the name webcat). If you do that, and start off my sending "hello" (as the note suggets) instead of a normal HTTP request (GET, POST or anything like that), you'll be greeted by a message that webcat is interested now, a random hex string and that it is waiting for your reply.

The key insight here is that this string is in fact x86 code consisting of simple additions/subtractions/etc. and ending with a single `cmp`. This can be inferred by from the note that states that webcat speaks "letni" (= "Intel" reversed), or from the general structure of the bytes that are send back (e.g. even though it is randomized, it has a reoccurring pattern/structure). The solution is therefore to respond with the answer that the x86 code computes. Do this a few times and webcat gives you the flag eventually. See `solve.py` for an example implementation.
