espresso
========

**Points:** 500 (496 after dynamic scoring)

**Flag:** RTN{j4v4_pr1m1t1v3_c4ch1ng_1s_d4ng3r0u5}

This is an evil challenge. Addresses in this writeup assume the linux compiled binary.

First thing that can be noticed is that the application creates an instance of the JVM (`FUN_0010143D`). The verification procedure (`FUN_001017ee`) loads an embedded class file into the JVM and calls the main procedure of it, with as argument the input string + a hardcoded string. This class file can be extracted using e.g. binwalk, or using any other disassembler like Ghidra or IDA.

```bash
binwalk -D="." espresso.linux
```

Decompiling the embedded class file reveals that it is a very elaborate way to test whether the two inputs are equal, with some small changes to the input text.

```java
package cc.rtn_team;

public class Espresso {
    private static Boolean brewCoffee(Byte by, Short s, Boolean bl) {
        byte by2 = by;
        if (bl.booleanValue()) {
            by2 = (byte)(by2 + 1);
        }
        return by2 == s;
    }

    public static void main(String[] stringArray) {
        if (stringArray == null || stringArray.length <= 1 || stringArray[0] == null || stringArray[1] == null || stringArray[0].length() != stringArray[1].length()) {
            System.exit(1);
            return;
        }
        for (int i = 0; i < stringArray[0].length(); ++i) {
            if (!Espresso.brewCoffee((byte)stringArray[0].charAt(i), (short)stringArray[1].charAt(i), i % 2 == 0).booleanValue()) continue;
            System.exit(1 + i);
            return;
        }
    }
}

```

There is something wrong with this code. Passing on the hardcoded string as input does not result in the correct message. Furthermore, from normal analysis, it looks like any string except for the hardcoded string should work (notice the ! before the if statement in the main for loop).

The evilness of this challenge comes from the fact that this challenge exploits the fact that the JVM caches instances of primitive values. In Java, you can represent bytes either by using the primitive `byte` type, or using the `java.lang.Byte`class. Naturally, objects of classes are much more memory intensive than primitives. Therefore, to avoid a lot of duplicated `Byte` instances of the same value on the heap, the JVM maintains a cache of instances of `Byte`instead. The`Byte.valueOf(byte)`method uses this cache rather than creating new instances every time. If you manage to change the internal values stored in these `Byte` object instances, a call such as`Byte.valueOf(1)`might result in a`Byte`object that does not contain the value`1` at all. This is exactly what the native loader does. Prior to actually calling this Java code, the native loader hacks into the JVM just before loading and running the embedded class file. `FUN_001016a4` and `FUN_00101478` patch the values of the cached`java/lang/Byte`and`java/lang/Boolean`, resulting in the fact that the compared values do not match with what is stored in the bytecode, effectively slightly changing the behaviour of the implemented verification code. These functions are somewhat hidden to the reverser, as strings in these functions are encrypted, and calls to the JVM interface are virtual, and therefore hidden behind a vtable instead of referenced by imports directories of the binary.

A simple python script can be made to reverse the substitutions that are made (example can be found in `make.py`)
