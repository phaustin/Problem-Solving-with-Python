---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

## Advanced topics

+++

### Copies and views

If you have a large dataset, it may be too expensive to keep more than one copy in computer memory at any one time.   What if you want to work with slices of that dataset, or pass the array to a function, or change the data in some way?   The default for numpy arrays is that assignment of an array to a new variable does not copy
the array, instead in makes a *view* of the original data, which points to the data but takes up essentially
no space in memory.

+++

Consider the following array:

```{code-cell} ipython3
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
a
```

Note that if you assign a to a new variable b, the two arrays are linked and changes in b also change array a.
This is because assignment of a to b created a view and not a copy.

```{code-cell} ipython3
b=a
b[1,1] = -999.
a
```

Numpy has a method that will tell you whether an array is sharing memory with another array:

```{code-cell} ipython3
np.shares_memory(a,b)
```

What if you want to have two distinct arrays that start with the same content but don't share memory?
Numpy has several options:

1) Copy constructor  -- you can make a copy of an array by passing the array into the np.array *constructor*
that makes new arrays from data

```{code-cell} ipython3
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array(a)
np.shares_memory(a,b)
```

2) Indexing  -- if an existing array has the right shape and dtype, you can force a copy like this:

```{code-cell} ipython3
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
#
# create an empty array of the same shape and dtype using np.empty_like
#
c = np.empty_like(a)
c[:] = a
np.shares_memory(a,c)
```

3) copy method -- numpy arrays  have a method to explictly copy data

```{code-cell} ipython3
d = a.copy()
np.shares_memory(a,c)
```

Now go the other direction -- what if you want to guarantee that one array is a view of another array?  
There is a corresponding view methond for that.  First note that multiplying by a scalar creates a copy:

```{code-cell} ipython3
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b=2.*a
np.shares_memory(a,b)
```

```{code-cell} ipython3
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
b = 2.*a
c= b.view()
np.shares_memory(b,c)
```

### Scalars, vectors and arrays

+++

Take a look at the shape of the following numpy objects.  First a 2-d array:

```{code-cell} ipython3
a=np.ones([2,3])
print(f"{a.shape=}")
a
```

Next a 1-d vector:

```{code-cell} ipython3
a=np.ones([2,])
print(f"{a.shape=}")
a
```

Finally a zero-dimension scalar:

```{code-cell} ipython3
a=np.array(2)
print(f"{a.shape=}")
a
```

How do you wind up changing the shape of your data?  The cell below takes the average along rows of the three columns.

```{code-cell} ipython3
a=np.ones([2,3])
rowavg=np.mean(a,axis=0)
print(f"{rowavg.shape=}")
rowavg
```

and this takes the average along columns of the two rows:

```{code-cell} ipython3
a=np.ones([2,3])
colavg=np.mean(a,axis=1)
print(f"{colavg.shape=}")
colavg
```

and averaging over both rows and columns:

```{code-cell} ipython3
a=np.ones([2,3])
grandavg=np.mean(a,axis=(0,1))
print(f"{grandavg.shape=}")
grandavg
```

You can also add axes to increase the number of dimensions (rank) of the array using np.newaxis:

```{code-cell} ipython3
multiarray = grandavg[np.newaxis,np.newaxis,np.newaxis]
print(f"{multiarray.shape=}")
multiarray
```

```{code-cell} ipython3
multiarray[0,0,0]
```

```{code-cell} ipython3

```
