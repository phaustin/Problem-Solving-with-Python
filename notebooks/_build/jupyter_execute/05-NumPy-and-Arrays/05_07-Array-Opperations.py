## Array Operations

Mathematical operations can be completed using NumPy arrays.

### Scalar Addition

Scalars can be added and subtracted from arrays and arrays can be added and subtracted from each other:

import numpy as np

a = np.array([1, 2, 3])
b = a + 2
print(b)

a = np.array([1, 2, 3])
b = np.array([2, 4, 6])
c = a + b
print(c)

### Scalar Multiplication

NumPy arrays can be multiplied and divided by scalar integers and floats:

a = np.array([1,2,3])
b = 3*a
print(b)

a = np.array([10,20,30])
b = a/2
print(b)

### Array Multiplication

NumPy array can be multiplied by each other using matrix multiplication. These matrix multiplication methods include element-wise multiplication, the dot product, and the cross product.

#### Element-wise Multiplication

The standard multiplication sign in Python ```*``` produces element-wise multiplication on NumPy arrays.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a * b

#### Dot Product

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.dot(a,b)

#### Cross Product

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.cross(a, b)

### Exponents and Logarithms

#### np.exp()

NumPy's ```np.exp()``` function produces element-wise $e^x$ exponentiation.

a = np.array([1, 2, 3])
np.exp(a)

#### Logarithms

NumPy has three logarithmic functions.

 * ```np.log()``` - natural logarithm (log base $e$)
 * ```np.log2()``` - logarithm base 2
 * ```np.log10()``` - logarithm base 10

np.log(np.e)

np.log2(16)

np.log10(1000)

### Trigonometry

NumPy also contains all of the standard trigonometry functions which operate on arrays. 

 * ```np.sin()``` - sin
 * ```np.cos()``` - cosine
 * ```np.tan()``` - tangent
 * ```np.asin()``` - arc sine
 * ```np.acos()``` - arc cosine
 * ```np.atan()``` - arc tangent
 * ```np.hypot()``` - given sides of a triangle, returns hypotenuse

import numpy as np
np.set_printoptions(4)

a = np.array([0, np.pi/4, np.pi/3, np.pi/2])
print(np.sin(a))
print(np.cos(a))
print(np.tan(a))
print(f"Sides 3 and 4, hypotenuse {np.hypot(3,4)}")

NumPy contains functions to convert arrays of angles between degrees and radians.

* ```deg2rad()``` - convert from degrees to radians
* ```rad2deg()``` - convert from radians to degrees

a = np.array([np.pi,2*np.pi])
np.rad2deg(a)

a = np.array([0,90, 180, 270])
np.deg2rad(a)

