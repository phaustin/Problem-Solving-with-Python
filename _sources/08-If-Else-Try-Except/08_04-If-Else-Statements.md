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

## If Else Statements

+++

In Python, if-statements can include _else_ clauses. An else clause is a section of code that runs if the if-statement is ```False```.  If the if-statement is ```True```, the code section under the else clause does not run. 

The general form of an if-statement with an else statement is below:

```python
if <logical_condition>:
    <code block 1>
else:
    <code block 2>
```

The  keyword ```else``` needs to be on its own line and be at the same indentation level as the ```if``` keyword that the ```else``` corresponds to. The keyword ```else``` needs to be followed by a colon ``` : ```. Any code that is included as part of the else statement must be indented the same amount. 

A sample if/else code section is below:

```{code-cell} ipython3
a = 5
if a>10:
    print('a is greater than 10')
else:
    print('a is less than 10')
```

Since ```a=5``` assigns a value to ```a``` that is less than 10, ```a>10``` is ```False``` and the code under the ```if``` statement does not run. Therefore, the code under the ```else``` statement does run, and ```"a is less than 10"``` is printed. 

If the value of ```a``` is modified so that ```a``` is greater than ```10```, ```a>10``` returns ```True```, and the code under the ```if``` statement _will_ run, and the code under the ```else``` keyword _will not_.

```{code-cell} ipython3
a = 20
if a>10:
    print('a is greater than 10')
else:
    print('a is less than 10')
```

### elif

+++

The _else if_ statement can be added to an if statement to run different sections of code depending on which one of many conditions are ```True```. The basic syntax of an else if section of code is:

```python
if <logical_condition>:
    <code block 1>
elif <logical_condition>:
    <code block 2>
else:
    <code block 3>
```

The keyword ```elif``` must be followed by a logical condition that evaluates as ```True``` or ```False``` followed by a colon ```:```. The ```<code block>``` runs if the ```elif``` condition is ```True``` and is skipped if the ```elif``` condition is ```False```.

An example section of code using ```if```, ```elif``` and ```else``` is below:

```{code-cell} ipython3
color = 'green'
if color == 'red':
    print('The color is red')
elif color == 'green':
    print('The color is green')
else:
    print('The color is not red or green')
```

If we modify the code and set ```color = 'orange'```, the code under the ```if``` does not run, and the code under the ```elif``` does not run either. Only the code under the ```else``` is executed.

```{code-cell} ipython3
color = 'orange'
if color == 'red':
    print('The color is red')
elif color == 'green':
    print('The color is green')
else:
    print('The color is not red or green')
```

```{code-cell} ipython3

```
