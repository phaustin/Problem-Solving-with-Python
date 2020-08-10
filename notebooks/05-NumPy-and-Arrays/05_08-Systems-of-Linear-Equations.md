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

## Systems of Linear Equations

+++

Systems of linear equations can be solved with arrays and NumPy.

+++

A system of linear equations is shown below:

$$ 8x + 3y -2z = 9 $$

$$ -4x + 7y + 5z = 15 $$

$$ 3x + 4y - 12z = 35 $$

+++

NumPy's ```np.linalg.solve()``` function can be used to solve this system of equations for the variables $x$, $y$ and $z$. 

The steps to solve the system of linear equations with ```np.linalg.solve()``` are below:

 * Create NumPy array ```A``` as a 3 by 3 array of the coefficients
 * Create a NumPy array ```b``` as the right-hand side of the equations
 * Solve for the values of $x$, $y$ and $z$ using ```np.linalg.solve(A, b)```. 
 
The resulting array has three entries. One entry for each variable. 

```{code-cell} ipython3
import numpy as np

A = np.array([[8, 3, -2], [-4, 7, 5], [3, 4, -12]])
b = np.array([9, 15, 35])
x = np.linalg.solve(A, b)
x
```

We can plug the valuse of $x$, $y$ and $z$ back into one of the equations to check the answer. 

$x$ is the first entry of the array, $y$ is the second entry of the array, and $z$ is the third entry of the array.

$x$ = ```x[0]```

$y$ = ```x[1]```

$z$ = ```x[2]```

When these values are plugged into the equation from above:

$$ 8x + 3y -2z = 9 $$

The answer should be ```9.0```.

```{code-cell} ipython3
8*x[0] + 3*x[1] - 2*x[2]
```

```{code-cell} ipython3

```
