---
jupytext:
  cell_metadata_filter: all
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.10'
    jupytext_version: 1.5.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

## If statements

+++

The _if-statement_ is one of the basic selection structures in Python. The syntax for a section of code that contains an if-statement is below:

```python
if <logical_condition>:
    <code to run>
```

The keyword ```if``` begins the statement. Following ```if```, a logical condition must to be included. A logical condition is an variable or expression that can be evaluated as ```True``` or ```False```. An example of a logical condition is ```a<5```. The logical condition ```a<5``` returns ```True``` if ```a``` is less than 5. Otherwise, if ```a``` is 5 or greater ```a<5``` returns ```False```. Following the logical condition, a colon ```:``` is required. After the if-statement, a section of code to run when the condition is ```True``` is included. The section of ```<code to run>``` must be indented and every line in this section of code must be indented the same number of spaces. By convention, four space indentation is used in Python. Most Python code editors, including Jupyter notebooks, indent code after if-statements automatically four spaces. 

The section of code below demonstrates an if-statement in Python:

```{code-cell} ipython3
a = 2
if a<5:
    print('less than five')
```

In the first line of code in the example above, the variable ```a``` is assigned the value ```2```. The second line of code is the if-statement. The if-statement starts with the keyword ```if``` and is followed by the logical condition ```a<5``` and a colon ```:```. The logical condition ```a<5``` will return either ```True``` or ```False``` depending on the value of ```a```. Since ```a=2```, the logical condition ```a<5``` evaluates as ```True```. The line ```print('less than five')``` is indented after the if-statement. The line of code including the ```print()``` statement will run if the if-statement is ```True```. Since the if-statement _is_ ```True```, the indented line ```print('less than five')``` runs.

As a result of running these three lines of code, the user sees the text ```less than five```.

+++

### Multiple if statements

+++

If-statements can be chained together one after another to create a programmatic flow. For example, the following code block utilizes three different if-statements, each if-statement is followed by an indented code block.

```{code-cell} ipython3
a = 2
if a<0:
    print('is negative')
if a == 0:
    print('is zero')
if a>0:
    print('is positive')
```

Note how each if-statement is followed by a logical condition and a colon ```:```. Also, note how the code below each if-statement is indented. If the code is left-justified (not indented), all three code lines run, and the output is different. 

The code block below will not run unless at least one line of code is indented after the if-statement. Python's ```pass``` keyword is a line of code that does nothing when executed. ```pass``` is added under the if-statments so the code runs error-free.

```{code-cell} ipython3
a = 2
if a<0:
    pass
print('a is negative')
if a == 0:
    pass
print('a is zero')
if a>0:
    pass
print('a is positive')
```

```{code-cell} ipython3

```
