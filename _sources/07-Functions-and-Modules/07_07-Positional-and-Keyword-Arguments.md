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

## Positional and Keyword Arguments

+++

Python functions can contain two types of arguments: _positional arguments_ and _keyword arguments_. Positional arguments must be included in the correct order. Keyword arguments are included with a keyword and equals sign.

+++

### Positional Arguments

An _argument_ is a variable, value or object passed to a function or method as input. _Positional arguments_ are arguments that need to be included in the proper position or order. 

The first positional argument always needs to be listed first when the function is called. The second positional argument needs to be listed second and the third positional argument listed third, etc. 

An example of positional arguments can be seen in Python's ```complex()``` function. This function returns a complex number with a real term and an imaginary term. The order that numbers are passed to the ```complex()``` function determines which number is the real term and which number is the imaginary term.

If the complex number ```3 + 5j``` is created, the two positional arguments are the numbers ```3``` and ```5```. As positional arguments, ```3``` must be listed first, and ```5``` must be listed second. 

```{code-cell} ipython3
complex(3, 5)
```

On the other hand, if the complex number ```5 + 3j``` needs to be created, the ```5``` needs to be listed first and the ```3``` listed second. Writing the same arguments in a different order produces a different result.

```{code-cell} ipython3
complex(5, 3)
```

#### Positional Arguments Specified by an Iterable

Positional arguments can also be passed to functions using an iterable object. Examples of iterable objects in Python include lists and tuples. The general syntax to use is:

```text
function(*iterable)
```

Where ```function``` is the name of the function and ```iterable``` is the name of the iterable preceded by the asterisk ```*``` character. 

An example of using a list to pass positional arguments to the ```complex()``` function is below. Note the asterisk ```*``` character is included before the ```term_list``` argument.

```{code-cell} ipython3
term_list = [3, 5]
complex(*term_list)
```

### Keyword Arguments

A _keyword argument_ is an argument passed to a function or method which is preceded by a _keyword_ and an equals sign.  The general form is:

```text
function(keyword=value)
```

Where ```function``` is the function name, ```keyword``` is the keyword argument and value is the value or object passed as that keyword.

Python's complex function can also accept two keyword arguments. The two keyword arguments are ```real=``` and ```imag=```. To create the complex number ```3 + 5j``` the ```3``` and ```5``` can be passed to the function as the values assigned to the keyword arguments ```real=``` and ```imag=```.

```{code-cell} ipython3
complex(real=3, imag=5)
```

Keyword arguments are passed to functions after any required positional arguments. But the order of one keyword argument compared to another keyword argument does not matter. Note how both sections of code below produce the same output.

```{code-cell} ipython3
complex(real=3, imag=5)
```

```{code-cell} ipython3
complex(imag=5, real=3)
```

#### Keyword Arguments Specified by a Dictionary

Keyword arguments can also be passed to functions using a Python dictionary. The dictionary must contain the keywords as keys and the values as values. The general form is:

```text
keyword_dict = {'keyword1': value1, 'keyword2': value2}
function(**keyword_dict)
```

Where ```function``` is the name of the function and ```keyword_dict``` is the name of the dictionary containing keywords and values preceded by the double asterisk ```**``` character. Note that the keywords assigned as keys in a dictionary must be surrounded by quotes ``` ' ' ```. An example of using a dictionary to pass keyword arguments to the ```complex()``` function is below:

```{code-cell} ipython3
keyword_dict = {'real': 3, 'imag': 5}
complex(**keyword_dict)
```

```{code-cell} ipython3

```
