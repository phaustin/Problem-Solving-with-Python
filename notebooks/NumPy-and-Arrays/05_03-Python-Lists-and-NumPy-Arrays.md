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

## Python Lists and NumPy Arrays

+++

NumPy is a Python package used for numerical calculations, working with arrays of homogeneous values, and scientific computing. This section introduces NumPy arrays then explains the difference between Python lists and NumPy arrays.

+++

### Python Lists

NumPy is used to construct homogeneous arrays and perform mathematical operations on arrays. A NumPy array is different from a Python list. The data types stored in a Python list can all be different.

```python
python_list = [ 1, -0.038, 'gear', True]
```

The Python list above contains four different data types: ```1``` is an integer, ```-0.038``` is a float, ```'gear'``` is a string, and ```'True'``` is a boolean.

The code below prints the data type of each value store in ```python_list```.

```{code-cell} ipython3
python_list = [1, -0.038, 'gear', True]
for item in python_list:
    print(type(item))
```

### NumPy Arrays

The values stored in a NumPy array must all share the same data type. Consider the NumPy array below:

```python
np.array([1.0, 3.1, 5e-04, 0.007])
```

All four values stored in the NumPy array above share the same data type: ```1.0```, ```3.1```, ```5e-04```, and ```0.007``` are all floats.

The code below prints the data type of each value stored in the NumPy array above.

```{code-cell} ipython3
import numpy as np

for value in np.array([1.0, 3.1, 5e-04, 0.007]):
    print(type(value))
```

If the same four elements stored in the previous Python list are stored in a NumPy array, NumPy forces all of the four items in the list to conform to the same data type. 

In the next code section, all four items are converted to type ```'<U32'```, which is a string data type in NumPy (the ```U``` refers Unicode strings; all strings in Python are Unicode by default).

```{code-cell} ipython3
np.array([1, -0.038, 'gear', True])
```

NumPy arrays can also be two-dimensional, three-dimensional, or up to n-dimensional. In practice, computer resources limit array size.  Remember that regardless of size, all elements in a NumPy array must be the same type.

+++

NumPy arrays are useful because mathematical operations can be run on an entire array simultaneously. If numbers are stored in a regular Python list and the list is multiplied by a scalar, the list extends and repeats- instead of multiplying each number in the list by the scalar.

The code below demonstrates list repetition using the multiplication operator, ```*```.

```{code-cell} ipython3
lst = [1, 2, 3, 4]
lst*2
```

To multiply each element in a Python list by the number ```2```, a loop can be used:

```{code-cell} ipython3
lst = [1, 2, 3, 4]
for i, item in enumerate(lst):
    lst[i] = lst[i]*2
lst
```

The method above is relatively cumbersome and is also quite _computationally expensive_. An operation that is computationally expensive is an operation that takes a lot of processing time or storage resources like RAM and CPU bandwidth.

Another way to complete the same operation in the loop above is to use a NumPy array.

+++

### Array Multiplication

An entire NumPy array can be multiplied by a scalar in one step. The scalar multiplication operation below produces an array with each element multiplied by the scalar ```2```.

```{code-cell} ipython3
nparray = np.array([1,2,3,4])
2*nparray
```

If we have a very long list of numbers, we can compare the amount of time it takes each of the two computation methods above, a list with a loop compared to array multiplication to complete the same operation. This comparison highlights an advantage of arrays compared to lists- speed.

+++

### Timing Arrays

Jupyter notebooks have a nice built-in method to time how long a line of code takes to execute. In a Jupyter notebook, when a line starts with ```%timeit``` followed by code, the kernel runs the line of code multiple times and outputs an average of the time spent to execute the line of code.

We can use ```%timit``` to compare a mathematical operation on a Python list using a for loop to the same mathematical operation on a NumPy array.

```{code-cell} ipython3
lst = list(range(10000))
%timeit for i, item in enumerate(lst): lst[i] = lst[i]*2
```

```{code-cell} ipython3
nparray = np.arange(0,10000,1)
%timeit 2*nparray
```

With 10,000 integers, the Python list and for loop takes an average of single milliseconds, while the NumPy array completes the same operation in tens of microseconds. This is a speed increase of over 100x by using the NumPy array (1 millisecond = 1000 microseconds).

For larger lists of numbers, the speed increase using NumPy is considerable.

```{code-cell} ipython3

```
