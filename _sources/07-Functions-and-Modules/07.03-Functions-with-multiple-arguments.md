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

## Functions with Multiple Arguments

+++

Functions can be written to accept multiple input arguments. When multiple arguments are specified, the arguments are listed within the parenthesis after the function name and separated by a comma:

```text
def function_name(argument1, argument2):
    <code>
    return output
```

A function that calculates the area of a triangle given the base and height of the triangle would accept two arguments ```base``` and ```height```.  The formula for the area $A$ of a triangle given base $b$ and height $h$ is below.

$$ A = \frac{1}{2} b \times h $$

Let's name our function ```triarea``` and accept ```base``` and ```height``` as input arguments. The ```triarea``` function will return a number, the area of a triangle.

```{code-cell} ipython3
def triarea(base, height):
    area = 0.5 * base * height
    return area
```

We can test our ```triarea()``` function with a couple of sets of input arguments.

```{code-cell} ipython3
triarea(10,5)
```

```{code-cell} ipython3
A = triarea(1,4)
A
```

Note if only one input argument is supplied to the ```triarea()``` function, an error is returned:

```{code-cell} ipython3
triarea(2)
```

```text
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-4-ddd55ccdd949> in <module>()
----> 1 triarea(2)

TypeError: triarea() missing 1 required positional argument: 'height'
```

+++

The variables ```base``` and ```height``` are local variables. If ```base``` or ```height``` is called outside the function definition, an error is returned.

```{code-cell} ipython3
triarea(base, height)
```

```text
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-4-1dd955b62482> in <module>()
----> 1 triarea(base, height)

NameError: name 'base' is not defined
```

```{code-cell} ipython3

```
