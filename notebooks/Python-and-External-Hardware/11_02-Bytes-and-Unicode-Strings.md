---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.9'
    jupytext_version: 1.5.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

## Bytes and Unicode Strings

+++

Before using PySerial to communicate with external hardware over the serial interface, it is import to understand the difference between _bytes_ and _unicode strings_ in Python. 

The distinction between bytes and Unicode strings is important because strings in Python are _Unicode_ by default. However, external hardware like Arduino's, oscilloscopes and voltmeters transmit characters as _bytes_.

+++

### Unicode Strings

+++

In Python, the syntax to define a new string is:

```{code-cell} ipython3
ustring = 'A unicode string'
```

Use Python's built-in ```type()``` function to determine the data type of the ```ustring``` variable:

```{code-cell} ipython3
print(type(ustring))
```

When the Python interpreter declares the variable ```ustring``` is of ```<class 'str'>```, it indicates ```ustring``` is a _Unicode string_.

**In Python 3, all strings are _Unicode strings_ by defaut**.

_Unicode strings_ are useful because there are many letters and letter-like characters that are not part of the set of letters, numbers, and symbols on a regular computer keyboard.  For example in Spanish, the accent character is used over certain vowels. Letters with accents cannot be represented by the letters on a standard English keyboard.  However, letters with accents are part of a set of letters, numbers, and symbols in _unicode strings_.

+++

### Byte Strings

Another way that characters such as letters, numbers, and punctuation can be stored is as _bytes_. A _byte_ is a unit of computer information that has a fixed width (one byte long). Because of this fixed width, one _byte_ only has a small number of unique combinations. This limits _byte strings_ to only the letters, numbers and punctuation marks on a computer keyboard (plus a couple extra). This limited set of characters is called the ASCII (pronounced _ask-ee two_) character set. A table of ASCII character codes is in the appendix. For instance, the ASCII character code ```49``` corresponds to the number one ```1```.

**Machines speak bytes.**

However, external hardware such as Arduinos, oscilloscopes, and voltmeters speak _byte strings_ by default. Almost all machines speak _byte strings_ by default, including the servers that bring Netflix to your laptop.

+++

To define a _byte string_ in Python, the letter ```b``` is placed before the quotation marks ```b'  '``` when a string is created.

```{code-cell} ipython3
bstring = b'bstring'
```

We can view the data type of the ```bstring``` variable using the ```type()``` function.

```{code-cell} ipython3
print(type(bstring))
```

### Convert between Unicode strings and byte strings

+++

In order for a Python program to communicate with external hardware, it needs to be able to convert between _Unicode strings_ and _byte strings_. This conversion is completed with the ```.encode()``` and ```.decode()``` methods. 

The ```.encode()``` method "encodes" a Unicode string into a byte string.

```<byte string> = <unicode string>.encode()```

The ```.decode()``` method "decodes" a byte string into a unicode string.

```<unicode string> = <byte string>.decode```

**Remember: Machines speak bytes, Python strings are Unicode by default.** 

A Python script must decode what machines transmit before further processing. Python defaults to Unicode (and machines do not), so within a script's Python code, remember to _encode_  Unicode strings so machines can understand them.

```{code-cell} ipython3
ustring = 'A unicode string'
new_bstring = ustring.encode()
type(new_bstring)
```

```{code-cell} ipython3
bstring = b'bstring'
new_ustring = bstring.decode()
type(new_ustring)
```

When a command from a Python program (a Unicode string) is sent to a piece of external hardware (that reads bytes):

The ```.encode()``` method is applied to the Unicode string (to convert the Unicode string to a byte string) before the command is sent to the piece of external hardware.

When a chunk of data comes in from a piece of external hardware (a byte string) and is read by a Python script (which speaks Unicode by the default):

The ```.decode()``` method is applied to the byte string (to convert the byte string to a Unicode string) before it is processed further by Python program.

```{code-cell} ipython3

```
