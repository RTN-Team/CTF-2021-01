lambdastic
==========

**Points:** 700 (696 after dynamic scoring)

**Flag:** RTN{1n_Th3_N4m3_0f_m4p_f1lt3r_and_f0ld_Amen}

This looks very scary when viewed in a decompiler like dnSpy, but really isn't. I promise.

There are various ways of solving this. This writeup will tackle it fully statically. ILSpy has a much better decompiler engine than dnSpy, so be sure to use it while following along.

The application implements three different monadic types: Taste, Spice and Fruit. Let's go over them one by one so that we can demystify what the huge expression is that is used to initialize the `Recipe` field.

## Taste

The `Taste` monad is perhaps the easiest of the three to recognize what it really is. Looking into the `SafeDiv` method, we see that it returns an instance of `Sweet`, with the dividend if the provided factor is not 0, and `Bitter` otherwise. This is also known as the `Maybe` or `Option` monad, where `Sweet` is `Just` or `Some`, and indicates a successful computation of the result. Conversely, `Bitter` maps to `None`, indicating no result.

## Spice

`Spice` is a little bit harder to recognize. One of the biggest hints for this one is the `Inputs` field, where we can see a bunch of calls to the `Cocoa` constructor, ending with one call to `Vanilla`. `Cocoa` defines two properties, `Seed` and `Branch`. We see that `Seed` contains an arbitrary value of type `T`, and `Branch`references another`Spice<T>`. This is a construct for linked lists, where `Seed` is the head of the list, and `Branch` is known as the tail and contains the remainder of the list. `Vanilla` indicates the empty list.

`Spice` also  overloads the `|` operator. With the knowledge gained from the previous paragraph , we can regonize that this operator is recursively iterating over the input list, and decrements a counter every time. When this counter reaches 0, the element is returned. In other words, this operator is an element accessor taking an integer index.

## Fruit

`Fruit` is the most involved monadic type, but is perhaps somewhat similar to the `Spice` monad. It is also a recursively defined type; Each `StrawBerry` element has a `Spice<Fruit>`(=`List<Fruit>`) property called `Arguments`, and a `Func<Spice<T>, Taste<T>>`(=`Func<List<T>, Maybe<T>>`) called `Function`. Furthermore, it defines an `Evaluate` method. Digging further a little into this reveals that this is an implementation of expression tree, where the `Evaluate` method takes a list of 2-tuples which represents a mapping of variables to raw values. This is used by the `Banana` implementation of the `Fruit` monad.

## Tying everything together

Now we get to the interpretation of the `Recipe` field. Using the information from above, we can infer that the `Recipe` stores a list of 3 mathematical expressions, which are added together in the `Main` method using a `Fold` operation.

```
f(x) = x^2 / dont + (fear*x) / the + monad / 250000000
```

Looking into `Inputs`, which contains the list of variable values, we can see that it contains the following values:

```
dont  = 1000000000
fear  = -161210479
the   = 250000000
monad = 25988818539409441

```

The verification algorithm evaluates the expression using the monadic bindings and the input interpreted as a hexstring. The result is compared to `0`. Therefore, the solution is to figure out solve `f(x) = 0`. Basic high-school algebra reveals that `x = 322420958`, which is `1337c0de` in hex. This will decrypt the flag
.
