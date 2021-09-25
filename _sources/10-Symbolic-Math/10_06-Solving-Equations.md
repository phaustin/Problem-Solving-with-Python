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

## Solving Equations

+++

SymPy's ```solve()``` function can be used to solve equations and expressions that contain symbolic math variables.

+++

### Equations with one solution

A simple equation that contains one variable like $x-4-2 = 0$ can be solved using the SymPy's  ```solve()``` function. When only one value is part of the solution, the solution is in the form of a list.

The code section below demonstrates SymPy's ```solve()``` function when an expression is defined with symbolic math variables.

```{code-cell} ipython3
from sympy import symbols, solve

x = symbols('x')
expr = x-4-2

sol = solve(expr)

sol
```

To pull the value out of the solution list ```sol```, regular list indexing can be used.

```{code-cell} ipython3
num = sol[0]

num
```

The code section below demonstrates SymPy's solve() function when an equation is defined with symbolic math variables. 

```{code-cell} ipython3
from sympy import symbols, Eq, solve

y = symbols('y')
eq1 = Eq(y + 3 + 8)

sol = solve(eq1)
sol
```

### Equations with two solutions

Quadratic equations, like $x^2 - 5x + 6 = 0$, have two solutions. SymPy's ```solve()``` function can be used to solve an equation with two solutions. When an equation has two solutions, SymPy's ```solve()``` function outputs a list. The elements in the list are the two solutions.

The code section below shows how an equation with two solutions is solved with SymPy's ```solve()``` function.

```{code-cell} ipython3
from sympy import symbols, Eq, solve

y = symbols('x')
eq1 = Eq(x**2 -5*x + 6)

sol = solve(eq1)
sol
```

If you specify the keyword argument ```dict=True``` to SymPy's ```solve()``` function, the output is still a list, but inside the list is a dictionary that shows which variable was solved for.

```{code-cell} ipython3
from sympy import symbols, Eq, solve

y = symbols('x')
eq1 = Eq(x**2 -5*x + 6)

sol = solve(eq1, dict=True)
sol
```

```{code-cell} ipython3
sol[0]
```

```{code-cell} ipython3
sol[1]
```

```{code-cell} ipython3

```
