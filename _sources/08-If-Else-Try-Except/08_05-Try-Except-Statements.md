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

## Try-Except Statements

+++

Try-except statements are another selection structure in Python. Like ```if```, ```elif``` and ```else``` statements, a try-except statements select a particular block of code to run based on a condition. Unlike ```if```, ```elif``` and ```else``` clauses, try-except blocks are not based on _logical conditions_. Try-except blocks are based upon whether a line or section of code returns an error. 

Therefore, before we learn how to use try-except statements, we need to understand two types of errors in Python: syntax errors and exception errors.

+++

### Syntax Errors

A _syntax error_ is a type of error in Python that occur when the syntax in a line of code is not valid Python code. Syntax errors include quotes that are not closed and variable names that do not start with a letter.

The line of code below contains a syntax error. The string ```"problem solving ``` is missing a quotation mark ```"```.

```{code-cell} ipython3
string = "problem solving
```

When you encounter syntax errors in Python, the Python interpreter displays ```SyntaxError``` and often a cryptic message.

Even if a line of code does not run when a program is executed, syntax errors in Python are not allowed. For instance, a line of code indented after the if-statement ```if 'a' == 'b':``` will not be executed. But if the indented line of code contains a syntax error, the Python interpreter still flags the error as a syntax error and does not complete the program.

```{code-cell} ipython3
if 'a' == 'b':
    string = 10problems
```

#### Exception Errors

Syntax errors are lines of code that are not valid Python. Another type of error in Python is an _exception error_. Exception errors result when a _valid_ line of Python code _cannot run_.  Lines of code with exception errors contain _valid_ Python code, but the line of code still cannot be executed. 

For example, the statement ```f = open('file.txt','r')``` is valid Python code. But if the file **_file.txt_** does not exist, Python throws an exception error because  ```f = open('file.txt','r')``` cannot be executed.

```{code-cell} ipython3
f = open('file.txt','r')
```

Another valid line of Python code is ```print(a[0])```, but if ```a``` is defined as an integer, ```a``` can not be indexed and an exception error is shown.

```{code-cell} ipython3
a = 1
print(a[5])
```

Try except statements can be used to try to run sections of Python code that _may_ return an exception error. The general syntax of a try except statement is below:

```python
try:
    <code to try>
except:
    <code to run instead>
```

For instance, if the file **_file.txt_** does not exist, a line of code that tries to open **_file.txt_** can be included in a ```try``` statement.

```{code-cell} ipython3
try:
    f=open('file.txt','r')
except:
    print('file does not exist')
```

Similarly, we can wrap the code ```a = 5``` and ```print(a[0])``` in a try block and attempt to run it. If the line ```a = 5``` and ```print(a[0])``` throws an exception error, the code below ```except``` runs.

```{code-cell} ipython3
try:
    a = 5
    print(a[0])
except:
    print('variable a is not a list')
```

When the Python code in a try block does run and does not throw an exception error, the code in the ```except``` block does not run.

```{code-cell} ipython3
try:
    a = 'Solution'
    print(a[0])
except:
    print('variable a is not a list')
```

```{code-cell} ipython3

```
