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

## Installing SymPy

+++

To work with symbolic math in Python, the SymPy library needs to be installed. SymPy comes pre-installed with the Anaconda distribution of Python.

+++

If you are not using the Anaconda distribution of Python, SymPy can be installed with the **Anaconda Prompt**. Use the command:

```text
> conda install sympy
```

+++

Alternatively, you can install SymPy using the Python package manager **pip**. The command below installs SymPy into the current environment.

```text
$ pip install sympy
```

+++

You can confirm your SymPy installation by opening up the Python REPL and typing the two commands below.

+++

```text
>>> import sympy
>>> sympy.__version__
'1.4'
```

+++

The ouput above shows SymPy version ```'1.4'``` is installed.
