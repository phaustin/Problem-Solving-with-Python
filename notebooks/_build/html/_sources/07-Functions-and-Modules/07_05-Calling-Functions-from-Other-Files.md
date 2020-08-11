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

## Calling Functions from Other Files

+++

User-defined functions can be called from other files. A function can be called and run in a different file than the file where the function is defined.

If a new file called **_myfunctions.py_** is created and contains two function definitions, ```plustwo()``` and ```falldist()```, the functions ```plustwo()``` and ```falldist()``` can be used by a separate script as long as the file and function names are imported in the separate script first. It is essential that the file which contains the function definitions ends in the **_.py_** extension. Without a **_.py_** extension, the file where the functions are defined can not be imported.

+++

Inside the file **_myfuctions.py_**, two functions are defined using the code below.

```python
# myfunctions.py

def plustwo(n):
    out = n + 2
    return out


def falldist(t,g=9.81):
    d = 0.5 * g * t**2
    return d
```

+++

This file, **_myfunctions.py_** can be imported into another script (another **_.py_** file), or Jupyter Notebook.

**Remember the file that contains the function definitions and the file calling the functions must be in the same directory.**

To use the functions written in one file inside another file include the import line, ```from filename import function_name```. Note that although the file name must contain a **_.py_** extension, ```.py``` is not used as part of the filename during import.

The general syntax to import and call a function from a separate file is below:

```text
from function_file import function_name

function_name(arguments)
```

An example using this syntax with the **_myfunctions.py_** file and the function ```plustwo()``` is below:

```{code-cell} ipython3
from myfunctions import plustwo

plustwo(3)
```

Multiple functions can be imported from the same file by separating the imported functions with commas. The general syntax to import and call multiple functions from the same file is below:

```text
from function_file import function_name1, function_name2

function_name1(arguments)
function_name2(arguments)
```

An example using this syntax with the **_myfunctions.py_** file and the functions ```plustwo()``` and ```falldist()``` is below:

```{code-cell} ipython3
from myfunctions import falldist, plustwo

out1 = falldist(3)
out2 = plustwo(3)

print(out1, out2)
```

Another way to import and use the functions from **_myfunctions.py_** into another script or Jupyter notebook is to import the entire **_myfunctions.py_** file with ```import myfunctions```, then call the functions with the syntax below. 

```text
import function_file

function_file.function_name()
```

An example using this syntax with the **_myfunctions.py_** file is below.

```{code-cell} ipython3
import myfunctions

myfunctions.plustwo(3)
```

```{code-cell} ipython3
import myfunctions

myfunctions.falldist(3)
```

```{code-cell} ipython3

```
