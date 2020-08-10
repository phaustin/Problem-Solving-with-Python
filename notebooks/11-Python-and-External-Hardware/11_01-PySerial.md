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

## PySerial

+++

PySerial is a Python package that facilitates serial communication. A computer running Python with the PySerial package installed can communicate with external hardware.  PySerial is a useful package for problem solvers because it allows us to exchange data between computers and pieces of external hardware such as voltmeters, oscilloscopes, strain gauges, flow meters, actuators, and lights.

PySerial provides an interface to communicate over the _serial_ communication protocol. Serial communication is one of the oldest computer communication protocols. Serial communication protocol predates the USB specification used by computers and other pieces of hardware like mice, keyboards, and webcams. USB stands for Universal Serial Bus. USB and is built upon and extends the original serial communication interface.

+++

### Installing PySerial

+++

To use the PySerial package with Python, PySerial first needs to be installed.  If you installed the full Anaconda distribution of Python, PySerial comes pre-installed. If you do have the full Anaconda distribution of Python installed, PySerial can be installed using the **Anaconda Prompt**. 

```text
> conda install pyserial
```

Alternatively, PySerial can be installed on the command line using **pip**:

```text
$ pip install pyserial
```

After PySerial is installed, the installation can be confirmed at the Python REPL:

```{code-cell} ipython3
>>> import serial
>>> print(serial.__version__)
```

**NOTE: Even though the command to install PySerial was** ```> conda install pyserial```, **the PySerial module is imported with the line** ```import serial```**.**

```{code-cell} ipython3

```
