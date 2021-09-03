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

## Equations

+++

You can define equations in Python using SymPy and symbolic math variables. _Equations_ in SymPy are different than _expressions_. An expression does not have equality. An expression is a collection of symbols and operators, but expressions are not equal to anything. Equations have equality. An equation can be thought of as an expression equal to something else.

A code section that defines the equation $4x + 2 = 0$ is below. Note all equations defined in SymPy are assumed to equal zero.

```{code-cell} ipython3
from sympy import symbols, Eq

x = symbols('x')

eq1 = Eq(4*x + 2)
```

If you want to define the equation $2y - x = 5$, which is not equal to zero, you just have to subtract the right hand side of the equation from the left hand side of the equation first.

$$2y - x = 5$$

$$2y - x -5 = 0$$

```{code-cell} ipython3
x, y = symbols('x y')

eq2 = Eq(2*y - x - 5)
```

Alternatively, an equation can be defined with a left hand side and a right hand side passed as separate arguments.

```{code-cell} ipython3
x, y = symbols('x y')

eq2 = Eq(2*y - x, 5)
```

### Substitutions in Equations

Symbols and expressions can be substituted into equations. In the code section below, the variable $z$ is substituted in for the variable $x$ ($z$ replaces $x$).

```{code-cell} ipython3
x, y, z = symbols('x y z')

eq2 = Eq(2*y - x - 5)
eq3 = eq2.subs(x,z)
eq3
```

```{code-cell} ipython3

```
