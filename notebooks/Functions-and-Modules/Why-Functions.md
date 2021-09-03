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

## Why Functions?

+++

Functions are an essential part of most programming languages. Functions are reusable pieces of code that can be called using a function's name. Functions can be called anywhere in a Python program, including calling functions within other functions. 

Functions provide a couple of benefits:

 * Functions allow the same piece of code to run multiple times

 * Functions break long programs up into smaller components
 
 * Functions can be shared and used by other programmers
 
Every function has a _function name_. The function name is used when the function is _called_ in a program. Calling a function means running a function.

Functions can receive input from the program. The input provided to a function is called _input arguments_ or just _arguments_. Arguments are the code passed to a function as input. 

Functions can produce output. We say a function _returns_ output to the program. The output of a function can be assigned to a variable for use in a program. 

Below is an example calling Python's ```pow()``` a function:

```{code-cell} ipython3
out = pow(3,2)
```

In the function call above, the function name is ```pow```. ```pow``` is the power function. The ```pow``` function raises a number to a power. The input arguments are the numbers ```3``` and ```2```. The function output is assigned to the variable ```out```.  In this example, the function returns the value ```9``` (3 raised to the 2 power, $3^2 = 9$).

```{code-cell} ipython3

```
