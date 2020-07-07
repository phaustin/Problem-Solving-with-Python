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

## Defining Variables

+++

Before we can construct symbolic math expressions or symbolic math equations with SymPy, first we need to create symbolic math variables, also called symbolic math _symbols_.

To define symbolic math variables with SymPy,  first import the ```symbols()``` function from the SymPy module:

```{code-cell} ipython3
from sympy import symbols
```

Symbolic math symbols are declared using SymPy's ```symbols()``` function. Pass a string surrounded by quotes to the ```symbols()``` function as an input argument. The the output of the ```symbols()``` function is assigned to a SymPy symbols object (not a string, no quotes).

```{code-cell} ipython3
x = symbols('x')
y = symbols('y')
```

SymPy's ```symbols()``` function can define multiple symbols in the same line of code. Note the input arguments passed to the ```symbols()``` function is a string, entries separated by a space (no comma) and surrounded by quotes. The output of the ```symbols()``` function are SymPy symbol objects. Commas separate these output objects (no quotation marks).

```{code-cell} ipython3
x, y = symbols('x y')
```
