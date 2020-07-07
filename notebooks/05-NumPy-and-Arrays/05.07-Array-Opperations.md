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

## Array Operations

+++

Mathematical operations can be completed using NumPy arrays. 

+++

### Scalar Addition

Scalars can be added and subtracted from arrays and arrays can be added and subtracted from each other:

```{code-cell} ipython3
import numpy as np

a = np.array([1, 2, 3])
b = a + 2
print(b)
```

```{code-cell} ipython3
a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
c = a + b
print(c)
```

### Scalar Multiplication

NumPy arrays can be multiplied and divided by scalar integers and floats:

```{code-cell} ipython3
a = np.array([1,2,3])
b = 3*a
print(b)
```

```{code-cell} ipython3
a = np.array([10,20,30])
b = a/2
print(b)
```

### Array Multiplication

NumPy array can be multiplied by each other using matrix multiplication. These matrix multiplication methods include element-wise multiplication, the dot product, and the cross product.

+++

#### Element-wise Multiplication

The standard multiplication sign in Python ```*``` produces element-wise multiplication on NumPy arrays.

```{code-cell} ipython3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a * b
```

#### Dot Product

```{code-cell} ipython3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.dot(a,b)
```

#### Cross Product

```{code-cell} ipython3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.cross(a, b)
```

### Exponents and Logarithms

+++

#### np.exp()

NumPy's ```np.exp()``` function produces element-wise $e^x$ exponentiation.

```{code-cell} ipython3
a = np.array([1, 2, 3])
np.exp(a)
```

#### Logarithms

NumPy has three logarithmic functions.

 * ```np.log()``` - natural logarithm (log base $e$)
 * ```np.log2()``` - logarithm base 2
 * ```np.log10()``` - logarithm base 10
 

```{code-cell} ipython3
np.log(np.e)
```

```{code-cell} ipython3
np.log2(16)
```

```{code-cell} ipython3
np.log10(1000)
```

### Trigonometry

NumPy also contains all of the standard trigonometry functions which operate on arrays. 

 * ```np.sin()``` - sin
 * ```np.cos()``` - cosine
 * ```np.tan()``` - tangent
 * ```np.asin()``` - arc sine
 * ```np.acos()``` - arc cosine
 * ```np.atan()``` - arc tangent
 * ```np.hypot()``` - given sides of a triangle, returns hypotenuse

```{code-cell} ipython3
import numpy as np
np.set_printoptions(4)

a = np.array([0, np.pi/4, np.pi/3, np.pi/2])
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(f"Sides 3 and 4, hypotenuse {np.hypot(3,4)}")
```

NumPy contains functions to convert arrays of angles between degrees and radians.

* ```deg2rad()``` - convert from degrees to radians
* ```rad2deg()``` - convert from radians to degrees

```{code-cell} ipython3
a = np.array([np.pi,2*np.pi])
np.rad2deg(a)
```

```{code-cell} ipython3
a = np.array([0,90, 180, 270])
np.deg2rad(a)
```

```{code-cell} ipython3

```
