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

# Problem Solving with Python Book Construction

+++

## Jupyter Notebooks

+++

This book was constructed using Jupyter notebooks. The GitHub.com repo for the book can be found at:

 > [github.com/ProfessorKazarinoff/Problem-Solving-with-Python-37-Edition](https://github.com/ProfessorKazarinoff/Problem-Solving-with-Python-37-Edition)

+++

The directory structure of the GitHub repo contains all the Jupyter notebooks used the write the book. The repo also contains a set of custom conversion scripts and templates which convert the Jupyuter notebooks into **_.html_** and **_.tex_** files.

+++

```text
Problem-Solving-with-Python-37-Edition/
|-- conversion_tools/
|-- notebooks/
|-- LICENSE
|-- notebooks/
|-- pdf/
|-- README.md
|-- website/
```

+++

The ```notebooks``` directory contains a directory for each chapter of the book:

+++

```text
notebooks/
|-- Preface/
|-- Orientation/
|-- Jupyter-Notebooks/
|-- The-Python-REPL/
|-- Data-Types-and-Variables/
|-- Matrices-and-Arrays/
|-- Plotting-with-Matplotlib/
|-- Functions-and-Modules/
|-- If-Else-Try-Except/
|-- Loops/
|-- Symbolic-Math/
|-- Appendix/
`-- figures/
```

There is a Jupyter notebook for each section of the book within each chapter directory. Each chapter directory contains an ```images``` directory for any images used in the markdown cells of the notebooks.

```text
Orientation/
|-- Welcome.md
|-- Why-Python.md
|-- The-Anaconda-Distribution-of-Python.md
|-- Installing-Anaconda-on-Windows.md
|-- Installing-Anaconda-on-MacOS.md
|-- Installing-Anaconda-on-Linux.md
|-- Installing-Python-from-Python-dot-org.md
|-- Summary.md
|-- Review-Questions.md
`-- images/
```
