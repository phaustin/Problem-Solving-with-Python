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

## Magic Commands

+++

Jupyter notebook code cells can contain special commands which are not valid Python code but affect the behavior of the notebook. These special commands are called _magic commands_.

+++

### %matplotlib inline

One of the most popular magic commands is:

```text
%matplotlib inline
```

Entering the ```%matplotlib inline``` command at the top of a Jupyter notebook renders Matplotlib plots in cells of the notebook. Without ```%matplotlib inline```, plots may jump out as external windows. A typical start to a Jupyter notebook using **Matplotlib** might start as:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```

+++

### %load

The ```%load``` command loads a Python module, webpage or file into a Jupyter notebook. If there is a file called **_hello.py_** in the same directory as the notebook with some Python code written in it, we can load that same code into a Jupyter notebook code cell with the ```%load``` command. 

Within a Jupyter notebook code cell type the command:

```python
%load hello.py
```

The result is the code from the file **_hello.py_** is copied into the current notebook.

```{code-cell} ipython3
# %load hello.py
# hello.py

print('This code was run from a seperate Python file')
print('Hello from the file hello.py')
```

### %run

+++

If the ```%run``` magic command followed by the name of a valid Python file,  the Python file runs as a script. Suppose the file **_hello.py_** is created in the same directory as the running Jupyter notebook. The directory structure will look something like this:

```text
| folder
---| notebook.ipynb
---| hello.py
```

In the file **_hello.py_** is the code:

```python
# hello.py

print('This code was run from a separate Python file')
print('Hello from the file hello.py')
```

Within our Jupyter notebook, if we ```%run``` this file, we get the output of the **_hello.py_** script in a Jupyter notebook output cell.

```{code-cell} ipython3
%run hello.py
```

### Other useful magic commands

+++

Below is a table of other useful Jupyter notebook magic commands

| Magic command | Result |
| --- | --- |
| %pwd | Print the current working directory |
| %cd | Change the current working directory |
| %ls | List the contents of the current directory |
| %history | Show the history of the ```In [ ]:``` commands |

You can list all of the available magic commands by typing and running ```%lsmagic``` in a Jupyter notebook code cell:

```python
%lsmagic
```

The output shows all the available line magic commands that begin with the percent sign ```%```.

```text
Available line magics:
%alias  %alias_magic  %autocall  %automagic  %autosave ...
%dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui ...
dir  %more  %mv  %notebook  %page  %pastebin  %pdb  %pdef ...
...

Available cell magics:
%%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html ...
%%python  %%python2  %%python3  %%ruby  %%script  %%sh  %%svg ...
```

```{code-cell} ipython3

```
