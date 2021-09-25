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

## Array Creation

+++

NumPy arrays are created with the ```np.array()``` function. The arguments provided to ```np.array()``` needs to be a list or iterable. An example is below. Note how the list ```[1,2,3]``` is passed into the function with square brackets at either end.

```{code-cell} ipython3
import numpy as np
np.array([1,2,3])
```

The data type can be passed into the ```np.array()``` function as a second optional keyword argument. Available data types include ```'int64'```, ```'float'```, ```'complex'``` and ```'>U32'``` (a string data type).

```{code-cell} ipython3
import numpy as np
np.array([1,2,3], dtype='float')
```

The data type used in a NumPy array can be determined using the ```.dtype``` attribute. For instance, an array of ```floats``` returns ```float64```.

```{code-cell} ipython3
import numpy as np
my_array = np.array([1,2,3], dtype='float')
my_array.dtype
```

In addition to ```np.array()```, there are other functions you can use to create NumPy arrays.

+++

### Arrays of Regularly Spaced Numbers

There are multiple ways to create arrays of regularly spaced numbers with NumPy. The next section introduces five NumPy functions to create regular arrays.

+++

#### np.arange()

NumPy's ```np.arange()``` function creates a NumPy array according the arguments ```start```, ```stop```,```step```.

```python
my_array = np.arange(start, stop, step)
```

The ```np.arange()``` function is useful for creating an array of regularly spaced numbers where you know the step size. 

Consider creating a NumPy array of even numbers between ```0``` and ```10```. Note that just like counting in Python, counting in NumPy starts at ```0``` and ends at ```n-1```.

```{code-cell} ipython3
np.arange(0,10+2,2)
```

#### np.linspace()

NumPy's ```np.linspace()``` function creates a NumPy array according the arguments ```start```, ```stop```,```number of elements```.

```python
my_array = np.linspace(start, stop, number of elements)
```

The ```np.linspace()``` function is useful for creating an array of regularly spaced numbers where the spacing is not known, but the number of values is. Consider creating a NumPy array of 10 numbers between ```0``` and ```2pi```.

```{code-cell} ipython3
np.linspace(0,2*np.pi,10)
```

#### np.logspace()

NumPy's ```np.logspace()``` function creates a NumPy array according the arguments ```start```, ```stop```,```number of elements```, but unlike ```np.linspace()```, ```np.logspace()``` produces a logarithmically spaced array.

```python
my_array = np.logspace(start, stop, number of elements, base=<num>)
```

The ```np.logspace()``` function is useful for creating an array of logarithmically spaced numbers where the spacing interval is not known but the number of values is. Consider creating a NumPy array of 4 logarithmically spaced numbers between ```10``` and ```100```. The function call is ```np.logspace(1, 2, 4)```. The ```start``` is $10^1 = 10$ and the ```stop``` is $10^2 = 100$, and the number of elements is ```4```. Be careful about putting large numbers in for ```stop``` because the stop argument is the power of 10, not the stop value.

```{code-cell} ipython3
np.logspace(1, 2, 4)
```

Large numbers passed to ```np.logspace()``` will produce errors. Remember to pass exponents to ```np.logspace()```. The code below throws an error because $10^{1000}$ is bigger than the largest floating point number supported by a 64 bit computer.

```{code-cell} ipython3
np.logspace(10,1000,4)
```

#### np.zeros()

NumPy's ```np.zeros()``` function creates a NumPy array containing all  zeros of a specific size. ```np.zeros()``` is useful when the size of an array is known, but the values that will go into the array have not been created yet.

```python
my_array = np.zeros((rows,cols))
```

```{code-cell} ipython3
np.zeros((5,5))
```

#### np.ones()

NumPy's ```np.ones()``` function creates a NumPy array containing all 1's of a specific size. Like ```np.zeros()```, ```np.ones()``` is useful when the size of an array is known, but the values that will go into the array have not been created yet.

```python
my_array = np.ones((rows,cols))
```

```{code-cell} ipython3
np.ones((3,5))
```

In the next section, you'll learn how to create array of random numbers with NumPy.

+++

### Arrays of Random Numbers

+++

NumPy has functions to create arrays of many different types of random numbers in the ```np.random``` module. A few of the common random number types are detailed below.

+++

#### Array of Random Integers

Arrays of random integers can be created with NumPy's ```np.random.randint()``` function. The general syntax is:

```python
np.random.randint(lower limit, upper limit, number of values)
```

The code below creates an array of 5 random integers, each random integer between 1 and 10:

```{code-cell} ipython3
np.random.randint(0,10,5)
```

Array dimensions can be provided as the third argument to the ```np.random.randint()``` function. The code below creates a 5 $\times$ 5 array of random numbers between 1 and 10:

```{code-cell} ipython3
np.random.randint(0,10,[5,5])
```

#### Array of Random Floats

Arrays of random floating point numbers can be created with NumPy's ```np.random.rand()``` function. The general syntax is:

```python
np.random.rand(number of values)
```

To create an array of 5 random floats between 0 and 1:

```{code-cell} ipython3
np.random.rand(5)
```

The upper and lower ranges of random floats can me modified with arithmetic.

To expand the range of random floats to between ```0``` and ```10```, multiply the result by ```10```

```{code-cell} ipython3
np.random.rand(5)*10
```

To change the range to between ```11``` and ```13```, we multiply the range by ```2``` (range 0-2), then add ```11``` to the result.

```{code-cell} ipython3
np.random.rand(5)*2+11
```

#### Random Array Choice from  a List

```python
np.random.choice(list of choices, number of choices)
```

To choose three numbers at random from a list of ```[1,5,9,11]``` use:

```{code-cell} ipython3
lst = [1,5,9,11]
np.random.choice(lst,3)
```

#### Random Array with a Normal Distribution

```np.random.randn()``` returns an array of  random numbers with a normal distribution, assuming a mean of 0 and variance of 1.  

```python
np.random.randn(number of values)
```

```{code-cell} ipython3
np.random.randn(10)
```

To specify a mean ```mu``` and a standard deviation ```sigma```, the function can be wrapped with:

```{code-cell} ipython3
mu = 70
sigma = 6.6

sigma * np.random.randn(10) + mu
```

Matplotlib's ```plt.hist()``` function can be used to quickly plot a normal distribution created with NumPy's ```np.random.randn()``` function.

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

mu = 70
sigma = 6.6

sample = sigma * np.random.randn(1000) + mu
plt.hist(sample)
plt.show()
```

The next section introduces methods to create 2D NumPy arrays.

+++

### 2-D Arrays

+++

#### np.meshgrid()

NumPy's ```np.meshgrid()``` function takes in two positional arguments which are 1D NumPy arrays. The two input arrays do not have to contain the same number of elements. The outputs of the ```np.meshgrid()``` function are two 2D arrays. One of the 2D arrays has the same values in each row; the other 2D array has the same values in each column. 

```python
np.meshgrid(array1, array2)
```

```{code-cell} ipython3
x = np.arange(0,6)
y = np.arange(0,11,2)
X, Y = np.meshgrid(x,y)
print(X)
print(Y)
```

Note how the first array ```X``` has the same numbers in each row, and the second array ```Y``` has the same numbers in each column.

+++

#### np.mgrid[]

NumPy's ```np.mgrid[]``` function is similar to ```np.meshgrid()```, but has a "MATLAB-like" syntax and behavior. 

Use square brackets ```[ ]``` after the ```np.mgrid``` function name. Separate the two "lists" passed as input arguments with a comma and use the ```start:stop:step``` indexing method. The outputs of the ```np.mgrid[]``` function are two 2D arrays. The first 2D array has the same values in each row; the second 2D array has the same values in each column. 

```python
np.mgrid[start:stop:step, start:stop:step]
```

```{code-cell} ipython3
X, Y = np.mgrid[0:5,0:11:2]
print(X)
print(Y)
```

### Section Summary

+++

Below is a list of NumPy functions and associated descriptions used in this section.

| Function | Description |
| --- | --- |
| ```np.array([list, of, numbers])``` | Array from a list |
| ```np.arange(start, stop, step)``` | Array with know step |
| ```np.linspace(start, stop, num)``` | Array with known num |
| ```np.logspace(start, stop, num)``` | Logorithmically spaced array |
|```np.zeros((rows, cols))``` | Array of zeros |
| ```np.ones((rows, cols))``` | Array of ones |
| ```np.random.randint(start, stop, num)``` | Random integers |
| ```np.random.rand(num)``` | Random float 0 to 1 |
| ```np.random.choice(list, num)``` | Randome choice from a list | 
| ```np.random.randn(num)``` | Random normal distribution |
| ```np.meshgrid(array1, array2)``` | Two 2D arrays from two 1D arrays  |
| ```np.mgrid[start:stop:step, start:stop:step]``` | MATLAB meshgrid |

```{code-cell} ipython3

```
