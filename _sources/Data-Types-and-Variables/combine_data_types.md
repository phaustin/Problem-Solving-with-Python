---
jupytext:
  formats: ipynb,md:myst
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

# Combining Data Types

## Casting, Calculation, and Concatination

Python is a *loosely typed* programming language, meaning that variables do not need to be explicitly declared alongside their data type, and they can sometimes dynamically change type to suit a particular requirement.

+++

### Casting

Sometimes it is useful to explicitly force a variable to change from one data type to another. We can do this with *type casting,* re-assigning variables the basic data types int, float, string, or boolean. The syntax doing this is:

```python
float(variable)  # re-assigns a variable as data type "float"

int(variable)  # re-assigns a variable as data type "int"

str(variable)  # re-assigns a variable as data type "str"

bool(variable)  # re-assigns a variable as data type "boolean"
```

Casting to float will add a decimal place to an integer, or convert the string `"3.0"` to the float `3.0`. The boolean `False` will be converted to `0.0` and `True` to `1.0`

```{code-cell} ipython3
float(3)
```

```{code-cell} ipython3
float("3.0")
```

```{code-cell} ipython3
float(True)
```

Casting from float to int will *truncate* the decimal place, **not round it** (if you want to round a number to the nearest integer, use the built-in function ```round()```) Booleans `True` and `False` are converted to `1` and `0`.

```{code-cell} ipython3
int(2.0)
```

```{code-cell} ipython3
int(2.9)
```

```{code-cell} ipython3
round(2.9)
```

```{code-cell} ipython3
int(False)
```

```{code-cell} ipython3
int("19")
```

Casting to a string will return a string containing the number or boolean value

```{code-cell} ipython3
str(29)
```

```{code-cell} ipython3
str(29.1)
```

```{code-cell} ipython3
str(True)
```

Casting to boolean will return `False` for the integer `0`, float `0.0` or empty string "", and `True` for pretty much anything else

```{code-cell} ipython3
bool(0)
```

```{code-cell} ipython3
bool(1.0)
```

```{code-cell} ipython3
bool('')
```

```{code-cell} ipython3
bool("pirates")
```

Casting only works within a valid range of variables that can be converted. Invalid type casts will raise an *error*:

```{code-cell} ipython3
int("fourteen")
```

### Calculations

For many operations, *type casting* occurs automatically. Python's built-in mathematical functions work with any combination of *int* and *float* data types, and the python interpreter will assign the output as type *int* if possible, or *float* if not.

```{code-cell} ipython3
ans = 6 + 2
ans
```

```{code-cell} ipython3
type(ans)
```

```{code-cell} ipython3
ans = 8 - 5.2
ans
```

```{code-cell} ipython3
type(ans)
```

Similarly for multiplication and division:

```{code-cell} ipython3
ans = 4 * 2
type(ans)
```

```{code-cell} ipython3
ans = 5 / 2
type(ans)
```

### Concatenation/Formatted Strings

Often, we would like to stick strings together, or express a numerical value within an existing string. The python syntax offers several ways to do this. 

1. The `+` operator works to *concatenate* strings together, i.e. take the string to the right of the operator and stick it to the end of the string on the left

```{code-cell} ipython3
str1 = "race"
str2 = "car"

str1 + str2
```

However, this doesn't work for combinations of string and numeric data types, as the `+` operator has a different meaning for int and float -- the interpreter can't figure out whether to add numeric values or concatenate strings.

```{code-cell} ipython3
num = 3
print(num + " blind mice")
```

There are a few ways to overcome this problem. 

A) Using *type casting*:

```{code-cell} ipython3
print(str(3) + " blind mice")
```

B) Use a *tuple* containing strings and numeric data:

```{code-cell} ipython3
print(3, "blind mice")
```

C) Using *f string literals*. Type the letter `f` at the beginning of a string, then insert any variable inside of curly brackets `{variable}` and it will format the variable into the string (This is the best way that will work in the largest variety of contexts):

```{code-cell} ipython3
print(f"{3} blind mice")
```
