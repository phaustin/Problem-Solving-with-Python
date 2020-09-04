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

# Saving plots

+++

Matplotlib plots can be saved as image files using the ```plt.savefig()``` function.

The ```plt.savefig()``` function needs to be called right above the ```plt.show()``` line. All the features of the plot must be specified before the plot is saved as an image file. If the figure is saved after the ```plt.show()``` command; the figure will not be saved until the plot window is closed. Calling ```plt.savefig()``` after calling ```plt.show()``` can be problematic when building plots in a Jupyter notebook with ```%matplotlib inline``` enabled.

A standard ```savefig()``` command is:

```python
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
```

Where ```'plot.png'``` is the name of the saved image file. Matplotlib infers the image file format (**_.png_**, **_.jpg_**, etc) based on the extension specified in the filename. 

The keyword argument ```dpi=``` specifies how many dots per inch (image resolution) are in the saved image. ```dpi=72``` is fine for web images. ```dpi=300``` is better for an image designed to go in a written report or **_.pdf_** document. 

The keyword argument ```bbox_inches='tight'``` is optional. If the axis labels in the plot are cut off in the saved image, set ```bbox_inches='tight'```.

The following code section constructs a line plot and saves the plot to the image file **_plot.png_**.

```{code-cell} ipython3
import matplotlib.pyplot as plt
# if using a Jupyter notebook, include:
%matplotlib inline

x = [0, 2, 4, 6]
y = [1, 3, 4, 8]

plt.plot(x,y)

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('plotted x and y values')
plt.legend(['line 1'])

# save the figure
plt.savefig('plot.png', dpi=300, bbox_inches='tight')

plt.show()
```

```{code-cell} ipython3

```
