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

# Reserved and Keywords in Python

+++

The following are reserved and keywords in Python. These words should not be used as the names for user-defined variables, functions, classes, methods or modules. Python's keywords can be accessed with the following code:

+++

```python
import keyword
print(f'There are {len(keyword.kwlist)} key words')
for keywrd in keyword.kwlist:
    print(keywrd)
```

```text
There are 33 key words
False
None
True
and
as
...

```

+++

## Logical Keywords

+++ {"latex": {"environment": "key_terms"}}

```text
True
False
not
and
or
is
None
in
```

+++

## Control Flow Key Words

+++ {"latex": {"environment": "key_terms"}}

```text
if
else
elif
for
while
break
continue
pass
try
except
finally
raise
return
yield
```

+++

## Definition Key Words

+++ {"latex": {"environment": "key_terms"}}

```text
def
global
nonlocal
class
lambda
with
assert
del
```

+++

## Module Keywords

+++ {"latex": {"environment": "key_terms"}}

```text
import
from
as
```

```{code-cell} ipython3

```
