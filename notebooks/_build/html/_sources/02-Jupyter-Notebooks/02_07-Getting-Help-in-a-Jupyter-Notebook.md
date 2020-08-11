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

## Getting Help in a Jupyter Notebook

+++

There are a couple of different ways to get help when using a Jupyter notebook.

+++

### Get help using ```dir```

Typing ```dir()``` and passing in a function, method, variable or object shows the possible object, method and function calls available to that object. For example, we can investigate the different functions in the **glob** module, part of Python's Standard Library, by importing ```glob```, then calling ```dir(glob)```.

```{code-cell} ipython3
import glob
dir(glob)
```

### Get help using Tab

After typing the name of a variable, object or function following the ```.``` character hit the ```[Tab]``` key. Typing ```[Tab]``` brings up a list of available options. Scroll through the list or type a letter to filter the list to certain starting letters. Use ```[Enter]``` to select the option you want.

Tab completion can also be used during module import. Hit ```[Tab```] after typing the module name to see which functions and classes are available in that module.

+++

```python
from math import <tab>
```

+++

### Get help using the ```help()``` function

After importing a module, you can use the ```help()``` function to see documentation about the command if it is available.

```{code-cell} ipython3
import math
help(math.sin)
```

After importing a module, you can view help on the imported module by typing the module name followed by a question mark ```?```

```{code-cell} ipython3
import statistics
statistics.mean?
```

```text
Signature: statistics.mean(data)
Docstring:
Return the sample arithmetic mean of data.

>>> mean([1, 2, 3, 4, 4])
2.8

>>> from fractions import Fraction as F
>>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
Fraction(13, 21)

>>> from decimal import Decimal as D
>>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
Decimal('0.5625')

If ``data`` is empty, StatisticsError will be raised.
File:      ~/anaconda3/envs/book/lib/python3.6/statistics.py
Type:      function
```

+++

You can view the source code where a particular function is defined using a double question mark ```??```

```{code-cell} ipython3
import statistics
statistics.mean??
```

```text
Signature: statistics.mean(data)
Source:   
def mean(data):
    """Return the sample arithmetic mean of data.

    >>> mean([1, 2, 3, 4, 4])
    2.8

    >>> from fractions import Fraction as F
    >>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
    Fraction(13, 21)

    >>> from decimal import Decimal as D
    >>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
    Decimal('0.5625')

    If ``data`` is empty, StatisticsError will be raised.
    """
    if iter(data) is data:
        data = list(data)
```

+++

### Help online

Help is also available online at in the offical Jupyter documentation:

 > [http://jupyter.readthedocs.io/en/latest/](http://jupyter.readthedocs.io/en/latest/)

You can always try to find help by typing something into Google. The site Stack Overflow is devoted to programming questions and answers. The highest rated answers on Stack Overflow are at the top of each question page.

```{code-cell} ipython3

```
