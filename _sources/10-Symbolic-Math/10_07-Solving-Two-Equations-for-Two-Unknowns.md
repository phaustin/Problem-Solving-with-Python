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

## Solving Two Equations for Two Unknows

+++

Solving two equations for two unknown can be accomplished using SymPy. Consider the following set of two equations with two variables:

$$ x + y - 5 = 0 $$

$$ x - y + 3 = 0 $$

To solve this system of two equations for the two unknowns, $x$ and $y$, first import the SymPy package. From the SymPy package, the functions ```symbols```, ```Eq``` and ```solve``` are needed.

```{code-cell} ipython3
from sympy import symbols, Eq, solve
```

Next, create two SymPy symbols objects, $x$ and $y$. As shown in a previous section, the string passed as an input argument to the ```symbols()``` function, ```'x y'```, does not have any commas. The outputs of the ```symbols()``` function are the two symbol objects ```x``` and ```y```. These outputs must be separated by a comma and are not surrounded by quotes.

```{code-cell} ipython3
x, y = symbols('x y')
```

Now define the two equations as SymPy equation objects.

```{code-cell} ipython3
eq1 = Eq(x + y - 5)
eq2 = Eq(x - y + 3)
```

We can use SymPy's ```solve()``` function to compute the value of $x$ and $y$. The first argument passed to the ```solve()``` function is a tuple of the two equations ```(eq1, eq2)```. The second argument passed to the ```solve()``` function is a tuple of the variables we want to solve for ```(x, y)```.

```{code-cell} ipython3
solve((eq1,eq2), (x, y))
```

The solution is in the form of a Python dictionary. The dictionary keys are the variables and the dictionary values are the numerical solutions. 

We can access the solution out of the solution dictionary using regular dictionary indexing.

```{code-cell} ipython3
sol_dict = solve((eq1,eq2), (x, y))
print(f'x = {sol_dict[x]}')
print(f'y = {sol_dict[y]}')
```

### Solve a statics problem with SymPy

+++

Consider the following engineering statics problem which can be solved with symbolic math and SymPy.

#### GIVEN:

A weight of 22 lbs is hung from a ring. The ring is supported by two cords. The first cord, cord CE, is 30 degrees above the horizontal and to the right. The second cord, cord BD, is 45 degrees to the left and above the horizontal. 

$w$ = 22 lb

$T_{CE}$ @ +30 degrees CCW relative to +x-axis

$T_{BD}$ @ +45 degress CW relative to -x-axis

#### FIND:

The magnitude of $T_{CE}$ and $T_{BD}$ 

+++

#### SOLUTION:

To solve for the magnitude of $T_{CE}$ and $T_{BD}$, we need to solve to two equations for two unknowns.

To accomplish this with Python, first import NumPy and SymPy.  The SymPy functions ```symbols```, ```Eq``` and ```solve``` are needed. We will also use NumPy's trig functions to solve this problem.

```{code-cell} ipython3
import numpy as np
from sympy import symbols, Eq, solve
```

Next, define the symbolic math variables. Multiple symbolic math variables can be defined at the same time. Remember the argument names (on the right-hand side of the assignment operator ```=```) need to be enclosed in quotes``` '  ' ``` and separated by spaces, no commas. The object names (on the left-hand side of the assignment operator ```=```) are separated with commas, no quotes.

```{code-cell} ipython3
Tce, Tbd = symbols('Tce Tbd')
```

Two equations based on the sum of the forces need to be defined. 

Assuming the ring is in static equilibrium:

$$ \Sigma \vec{F} = 0 $$

$$ \Sigma F_{x} = 0 $$

$$ \Sigma F_{y} = 0 $$

The three forces opperating on the ring are defined as:

$$ {T_{ce}} = tension \ in \ cable \ CE \ $$

$$ \vec{T_{ce}} = T_{ce} cos(30)\hat{i} + T_{ce} sin(30)\hat{j} $$

$$ {T_{bd}} = tension \ in \ cable \ BD $$

$$ \vec{T_{bd}} = - T_{bd} cos(45)\hat{i} + T_{bd} sin(45)\hat{j} $$

$$ \vec{w} = 0 \hat{i} - 22 \hat{j} $$

Taking $\Sigma F_{x} = 0$ (sum of the $\hat{i}$ terms):

$$ T_{ce} cos(30) - T_{bd} cos(45) + 0 = 0 $$

Taking $\Sigma F_{y} = 0$ (sum of the $\hat{j}$ terms):

$$ T_{ce} sin(30) + T_{bd} sin(45) - 22 = 0 $$

+++

The first equation, based on the sum of the forces in the x-direction (the $\hat{i}$ terms) is:

$$ T_{ce} cos(30) - T_{bd} cos(45) + 0 = 0 $$

This equation can be represented as a SymPy equation object. Note the right-hand side of the equation is ```0```. SymPy equation objects are instantiated with expressions equal to zero. If the expression was not equal to zero, simply subtract both sides by the term on the right-hand side of the equals sign and use the resulting expression (equal to zero) to create the SymPy equation object.

A detail in the code section below is that NumPy's ```np.cos()``` function accepts an angle in radians, so we need to convert our angles from degrees to radians using NumPy's ```np.radians()``` function.

```{code-cell} ipython3
eq1=Eq(Tce * np.cos(np.radians(30)) - Tbd * np.cos(np.radians(45)))
print(eq1)
```

The second equation, based on the sum of the forces in the y-direction is:

$$ T_{ce} sin(30) + T_{bd} sin(45) - 22 = 0 $$

Define this equation as a SymPy equation object as well:

```{code-cell} ipython3
eq2=Eq(Tce * np.sin(np.radians(30)) + Tbd * np.sin(np.radians(45))-22)
print(eq2)
```

Now solve the two equations for $T_{ce}$ and $T_{bd}$ with SymPy's ```solve()``` function. The first argument passed to the ```solve()``` function is a tuple of equations to solve, the second argument passed to the ```solve()``` function is a tuple of the variables to solve for.

```{code-cell} ipython3
solve((eq1,eq2),(Tce, Tbd))
```

The solution is saved in a Python dictionary. The dictionary keys are the variable names ```Tbd``` and ```Tce``` and the dictionary values are the numerical solutions. 

The numerical solutions can be pulled out of the dictionary using regular Python dictionary access. Note ```Tce``` and ```Tbd``` are SymPy symbols objects, not strings.

```{code-cell} ipython3
sol_dict = solve((eq1,eq2),(Tce, Tbd))
print(f'Tce = {sol_dict[Tce]}')
print(f'Tce = {sol_dict[Tbd]}')
```

The same problem can be solved again, but with $w$ kept as a variable.

```{code-cell} ipython3
w, Tce, Tbd = symbols('w, Tab, Tac')

eq1=Eq(Tce * np.cos(np.radians(30)) - Tbd * np.cos(np.radians(45)))
eq2=Eq(Tce * np.sin(np.radians(30)) + Tbd * np.sin(np.radians(45))-w)

solve((eq1,eq2),(Tce,Tbd))
```

The result is a solution is in terms of the variable $w$. 

```{code-cell} ipython3

```
