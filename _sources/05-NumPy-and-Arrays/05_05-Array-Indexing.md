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

## Array Indexing

+++

Elements in NumPy arrays can be accessed by _indexing_. Indexing is an operation that pulls out a select set of values from an array. The _index_ of a value in an array is that value's _location_ within the array. There is a difference between _the value_ and _where the value is stored_ in an array. 

An array with 3 values is created in the code section below.

```{code-cell} ipython3
import numpy as np

a = np.array([2,4,6])
print(a)
```

The array above contains three values: ```2```, ```4``` and ```6```. Each of these values has a different index. 

**Remember counting in Python starts at ```0``` and ends at ```n-1```.**

The value ```2``` has an index of 0. We could also say ```2``` is in location 0 of the array. The value ```4``` has an index of ```1``` and the value ```6``` has an index of ```2```. The table below shows the index (or location) of each value in the array.

| Index (or location) | Value |
| --- | ---|
| 0 | ```2``` |
| 1 | ```4``` |
| 2 | ```6``` |

Individual values stored in an array can be accessed with indexing. 

The general form to index a NumPy array is below:

```python
<value> = <array>[index]
```

Where ```<value>``` is the value stored in the array, ```<array>``` is the array object name and ```[index]``` specifies the index or location of that value. 

In the array above, the value 6 is stored at index 2.

```{code-cell} ipython3
import numpy as np

a = np.array([2,4,6])
print(a)
value = a[2]
print(value)
```

### Multi-dimensional Array Indexing

+++

Multi-dimensional arrays can be indexed as well. A simple 2-D array is defined by a list of lists.

```{code-cell} ipython3
import numpy as np

a = np.array([[2,3,4],[6,7,8]])
print(a)
```

Values in a 2-D array can be accessed using the general notation below:

```python
<value> = <array>[row,col]
```

Where ```<value>``` is the value pulled out of the 2-D array and ```[row,col]``` specifies the row and column index of the value. Remember Python counting starts at ```0```, so the first row is row zero and the first column is column zero.

We can access the value ```8``` in the array above by calling the row and column index ```[1,2]```.  This corresponds to the 2nd row (remember row 0 is the first row) and the 3rd column (column 0 is the first column).

```{code-cell} ipython3
import numpy as np

a = np.array([[2,3,4],[6,7,8]])
print(a)
value = a[1,2]
print(value)
```

### Assigning Values with Indexing

+++

Array indexing is used to _access_ values in an array. And array indexing can also be used for _assigning_ values of an array.

The general form used to assign a value to a particular index or location in an array is below:

```python
<array>[index] = <value>
```

Where ```<value>``` is the new value going into the array and ```[index]``` is the location the new value will occupy. 

The code below puts the value ```10``` into the second index or location of the array ```a```.

```{code-cell} ipython3
import numpy as np

a = np.array([2,4,6])
a[2] = 10
print(a)
```

Values can also be assigned to a particular location in a 2-D arrays using the form:

```python
<array>[row,col] = <value>
```

The code example below shows the value ```20``` assigned to the 2nd row (index ```1```) and 3rd column (index ```2```) of the array.

```{code-cell} ipython3
import numpy as np

a = np.array([[2,3,4],[6,7,8]])
print(a)

a[1,2]=20
print(a)
```

```{code-cell} ipython3

```
