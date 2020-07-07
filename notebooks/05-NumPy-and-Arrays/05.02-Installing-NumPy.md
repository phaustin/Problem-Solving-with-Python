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

## Installing NumPy

+++

Before NumPy's functions and methods can be used, NumPy must be installed. Depending on which distribution of Python you use, the installation method is slightly different.

+++

### Install NumPy on Anaconda

If you installed the Anaconda distribution of Python, NumPy comes pre-installed and no further installation steps are necessary. 

If you use a version of Python from python.org or a version of Python that came with your operating system, the **Anaconda Prompt** and **conda** or **pip** can be used to install NumPy.

+++

### Install NumPy with the Anaconda Prompt

To install NumPy, open the **Anaconda Prompt** and type:

```text
> conda install numpy
```

Type ```y``` for yes when prompted.

+++

### Install NumPy with pip

To install NumPy with **pip**, bring up a terminal window and type:

```text
$ pip install numpy
```

This command installs NumPy in the current working Python environment.

+++

### Verify NumPy installation

To verify NumPy is installed, invoke NumPy's version using the Python REPL. Import NumPy and call the ```.__version__``` attribute common to most Python packages.

```{code-cell} ipython3
import numpy as np
np.__version__
```

A version number like ```'1.16.4'``` indicates a successful NumPy installation.

```{code-cell} ipython3

```
