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

# Multi Line Plots

+++

Multi-line plots are created using Matplotlib's ```pyplot``` library. This section builds upon the work in the previous section where a plot with one line was created. This section also introduces Matplotlib's _object-oriented_ approach to building plots. The object-oriented approach to building plots is used in the rest of this chapter.

+++

## The Matplotlib's object-oriented interface

An object-oriented plotting interface is an interface where components of the plot (like the axis, title, lines, markers, tick labels, etc.) are treated as programmatic _objects_ that have _attributes_ and _methods_ associated with them.

To create a new _object_ is called _instantiation_. Once an object is created, or _instantiated_, the properties of that object can be modified, and methods can be called on that object.

The basic anatomy of a Matplotlib plot includes a couple of layers, each of these layers is a Python _object_:

* Figure object: The bottom layer. Think of the figure object as the figure window which contains the minimize, maximize, and close buttons. A figure window can include one plot or multiple plots.
* Plot objects: A plot builds on the figure layer. If there are multiple plots, each plot is called a subplot. 
* Axis objects: An axis is added to a plot layer. Axis can be thought of as sets of x and y axis that lines and bars are drawn on. An Axis contains daughter attributes like axis labels, tick labels, and line thickness.
* Data objects: data points, lines, shapes are plotted on an axis.

+++

Matplotlib's ```plt.subplot()``` function is used to build figure objects. The ```plt.subplot()``` function creates both a figure _object_ and axis _objects_. We say the ```plt.subplot()``` function _instantiates_ a figure _object_ and _instantiates_ an axis object. For now, we'll leave the ```subplot()``` arguments blank. By default, the ```subplot()``` function creates a single figure object and a single axis object.  By convention we'll call the figure object ```fig``` and the axis object ```ax```. Note these two outputs of the ```plt.subplots()``` function are separated by a comma.

```text
fig, ax = plt.subplots()
```

We instantiated a figure object and axis object, now both of these objects need attributes. We add attributes to the axis object to build a plot. NumPy arrays or Python lists ```x```, ```y```, and ```z``` can be added to axis object ```ax```.

```text
ax.plot(x,y)
ax.plot(x,z)
```

We add a plot attribute (a line) to our axis object ```ax``` using the object-oriented structure ```<object>.<attribute>```. In this case, ```ax``` is the object and ```plot``` is the attribute.

The next code section demonstrates how to build a multi-line plot with Matplotlib's object-oriented interface.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, inlcude:
%matplotlib inline

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x,y)
ax.plot(x,z)

plt.show()
```

The ```ax``` object has many _methods_ and _attributes_. In Python a method is sort of like a function, but methods typically modify the object they are associated with, while functions modify their input arguments.

Two methods we can run on the ```ax``` object include ```ax.set_title()``` and ```ax.legend()```. A couple daughter objects include ```ax.xaxis``` and ```ax.yaxis```. These daughter objects in turn have methods such as ```ax.xaxis.set_label_text()``` and ```ax.yaxis.set_label_text()```.

The code section below demonstrates using objects, attributes, and methods to build a multi-line plot.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
%matplotlib inline

x = np.arange(0,4*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x,y)
ax.plot(x,z)

ax.set_title('Two Trig Functions')
ax.legend(['sin','cos'])
ax.xaxis.set_label_text('Angle $\Theta$')
ax.yaxis.set_label_text('Sine and Cosine')

plt.show()
```

The table below shows common commands to build plots using Matplotlib's  object-oriented interface.

| Object-oriented command | Description | Corresponding ```plt.``` command |
| --- | --- | --- |
| ```fig, ax = plt.subplots()``` | create a figure and axis object | - |
| ```ax.plot(x,y)``` | create a line plot | ```plt.plot(x,y)``` |
| ```ax.set_title('My Title')``` | plot title | ```plt.title('My Title')``` |
| ```ax.set_xlabel('x label')``` | x-axis label | ```plt.xlabel('x label')``` |
| ```ax.set_ylabel('x label')``` | y-axis label | ```plt.ylabel('x label')``` |
| ```ax.legend(['line1','line2'])``` | legend | ```plt.legend(['line1','line2'])``` |
| ```ax.set_xlim([0, 5])``` | x-axis limits | ```plt.xlim([0, 5])``` |
| ```ax.set_ylim([-1, 1])``` | y-axis limits | ```plt.ylim([-1, 1])``` |
| ```ax.axis([-x, +x, -y, +y])``` | both axis limits | - |
| ```ax.grid(True)``` | grid in both directions | ```plt.grid(True)``` |
| ```ax.xaxis.grid(True)``` | vertical grid lines | - |
| ```ax.yaxis.grid(True)``` | horizontal grid lines | - |
| ```ax.xaxis.set_xticks([loc])``` | x-axis tick locations | ```plt.xticks([loc],[label])``` |
| ```ax.xaxis.set_xticklabels([labels])``` | x-axis tick labels | ```plt.xticks([loc],[label])``` |
| ```ax.yaxis.set_yticks([loc])``` | y-axis tick locations | ```plt.yticks([loc],[label])``` |
| ```ax.yaxis.set_yticklabels([labels])``` | y-axis tick labels | ```plt.yticks([loc],[label])``` |
| ```ax.xaxis.set_ticks([])``` | remove x tick labels | ```plt.xticks([],[])``` |
| ```ax.yaxis.set_ticks[])``` | remove y tick labels | ```plt.yticks([],[])``` |
| ```ax.set_aspect('equal')``` | equal axis scales | - |
| ```fig.tight_layout()``` | adjust padding | ```plt.tight_layout()``` |
| ```plt.show()``` | show the plot | ```plt.show()``` |

```{code-cell} ipython3

```
