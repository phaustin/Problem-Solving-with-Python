---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.10'
    jupytext_version: 1.5.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

## Expressions and Substitutions

+++

Symbolic math variables can be combined into symbolic math expressions. Once in an expression, symbolic math variables can be exchanged with substituion.

+++

### Expressions

A symbolic math expression is a combination of symbolic math variables with numbers and mathematical operators such as ```+```, ```-```, ```/``` and ```*```. The standard Python rules for calculating numbers apply in SymPy symbolic math expressions.

After the symbols ```x``` and ```y``` are created, a symbolic math expression using ```x``` and ```y``` can be defined.

```{code-cell} ipython3
from sympy import symbols

x, y = symbols('x y')
expr = 2*x + y
```

### Substitution

+++

Use SymPy's ```.subs()``` method to insert a numerical value into a symbolic math expression. The first argument of the ```.subs()``` method is the mathematical symbol and the second argument is the numerical value. In the expression below:

$$ 2x + y $$

If we substitute:

$$ x = 2 $$

The resulting expression is:

$$ 2(2) + y $$
$$ 4 + y $$

We can code the substitution above using SymPy's ```.subs()``` method as shown below.

```{code-cell} ipython3
expr.subs(x, 2)
```

The ```.subs()``` method does not replace variables in place, ```.subs()``` only completes a one-time substitution. If ```expr``` is called after the ```.subs()``` method is applied, the original ```expr``` expression is returned.

```{code-cell} ipython3
expr
```

To make the substitution permanent, a new expression object needs to be assigned to the output of the ```.subs()``` method.

```{code-cell} ipython3
expr = 2*x + y
expr2 = expr.subs(x, 2)
expr2
```

SymPy variables can also be substituted into SymPy expressions. In the code section below, the symbol $z$ is substituted for the symbol $x$ ($z$ replaces $x$).

```{code-cell} ipython3
x, y, z = symbols('x y z')
expr = 2*x + y
expr2 = expr.subs(x, z)
expr2
```

Expressions can also be substituted into other expressions. Consider the following:

$$ y + 2x^2 + z^{-3} $$

substitute in 

$$ y = 2x $$

results in

$$ 2x + 2x^2 + z^{-3} $$

```{code-cell} ipython3
x, y, z = symbols('x y z')
expr = y + 2*x**2 + z**(-3)
expr2 = expr.subs(y, 2*x)
expr2
```

A practical example involving symbolic math variables, expressions and substitutions can include a complex expression and several replacements.

$$ n_0e^{-Q_v/RT} $$

$$ n_0 = 3.48 \times 10^{-6} $$

$$ Q_v = 12,700 $$

$$ R = 8.31 $$

$$ T = 1000 + 273 $$

We can create four symbolic math variables and combine the variables into an expression with the code below.

```{code-cell} ipython3
from sympy import symbols, exp
n0, Qv, R, T = symbols('n0 Qv R T')
expr = n0*exp(-Qv/(R*T))
```

Multiple SymPy ```subs()``` methods can be chained together to substitute multiple variables in one line of code.

```{code-cell} ipython3
expr.subs(n0, 3.48e-6).subs(Qv,12700).subs(R, 8031).subs(T, 1000+273)
```

To evaluate an expression as a floating point number, use SymPy's ```.evalf()``` method.

```{code-cell} ipython3
expr2 = expr.subs(n0, 3.48e-6).subs(Qv,12700).subs(R, 8031).subs(T, 1000+273)
```

```{code-cell} ipython3
expr2.evalf()
```

You can control the number of digits the ```.evalf()``` method outputs by passing a number as an argument.

```{code-cell} ipython3
expr2.evalf(4)
```

### Summary

+++

The SymPy functions and methods used in this section are summarized in the table below.

| SymPy function or method | Description | Example |
| --- | --- | --- |
| ```symbols()``` | create symbolic math variables | ```x, y = symbols('x y')``` |
| ```.subs()``` | substitute a value into a symbolic math expression | ```expr.subs(x,2)``` |
| ```.evalf()``` | evaluate a symbolic math expression as a floating point number | ```expr.evalf()``` |
