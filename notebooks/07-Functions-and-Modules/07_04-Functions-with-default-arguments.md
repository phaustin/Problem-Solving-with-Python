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

## Functions with Default Arguments

+++

Functions can be specified with _default arguments_. If values for these arguments are not supplied when the function is called, the default values are used. The general format to define a function with default arguments is below:

```text
def function_name(argument1=default_value, argument2=default_value):
    <code>
    return output
```

+++

An example a function with default arguments might be a function that calculates the distance an object falls based on time. The general formula for fall distance $d$ based on fall time $t$ can be modeled as:

$$ d = \frac{1}{2}gt^2 $$

Where $g$ is the acceleration due to gravity. On earth the value of $g = 9.81 m/s^2$. But on the moon, $g = 1.625 m/s^2$.  Our ```falldist()``` function will include the default value for earth's gravity and give programmers the option of specifying a different value for $g$ if they choose.

```{code-cell} ipython3
def falldist(t, g=9.81):
    d = 0.5 * g * t**2
    return d
```

On earth, the distance a ball that falls for three seconds is calculated by ```falldist(3)```. In the function call ```falldist(3)```, no value is specified for ```g```, so the default value ```9.81``` is used.

```{code-cell} ipython3
falldist(3)
```

On earth, the ball falls ```44.145``` meters in 3 seconds.

However, on the moon gravity is much weaker than on earth. The acceleration of falling objects on the moon is $g = 1.625 m/s^2$. To calculate how far a ball falls on the moon in three seconds, two arguments need to be supplied to the ```falldist()``` function: ```3``` and ```1.625```. If a second argument is provided to the ```falldist()``` function, in this case ```1.625```, it overrides the default value assigned in the first line of the function.

```{code-cell} ipython3
falldist(3, 1.625)
```

On the moon, the ball falls ```7.3125``` meters in 3 seconds.

```{code-cell} ipython3

```
