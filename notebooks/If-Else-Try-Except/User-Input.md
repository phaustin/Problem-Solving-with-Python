---
jupytext:
  formats: ipynb,md:myst,py:percent
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

## User Input

+++

To begin this chapter, Python's ```input()``` function is discussed.

**Editorial note**:  When we turn this chapter into a website, the automated notebook
runner will produce an error when asked for interactive input.  To get around this, we're going to
use the `try/except` blocks that we will discuss in Section 9.6
to catch the error and substitute default values for the variables.  When you run this notebook
on a jupyterhub you will be prompted for the values instead.

+++

Python can be used to ask users for input. The input entered by a user can be saved to a variable and used in subsequent parts of the program. The syntax of Python's ```input()``` function is below:

```
var = input('message')
```

Where ```var``` is the variable that stores the user's input and ```'message'``` is the message the user sees at the prompt. A string enclosed in quotes, like ```'message'```, needs to be passed as an input argument to the ```input()``` function.  Let's ask a user for their age:

```{code-cell} ipython3
try:
    age = input('how old are you? ')
except:
    age= '-5'
```

Since the user's input is assigned to a variable, further operations can be run on it. Now, let's print the user's age back to them. This can be accomplished with an f-string. Note the ```f' '``` inserted before the string. A set of curly braces ```{  }``` surrounds the variable's name and the variable's value is printed back to the user.

```{code-cell} ipython3
try:
    age = input('how old are you? ')
except:
    age = '-5'
print(f'you are {age} years old')
```

Let's try another example. We will we ask the user for the base and height of a triangle and print out the area of the triangle. 

But, there is a problem with the approach below. The code block does not run because a common error is present.

```{code-cell} ipython3
try:
    b = input('base of triangle: ')
except:
    b = '5'
try:
    h = input('height of triangle: ')
except:
    h = '10'
A = (1/2)*b*h
print(f'The area of the triangle is: {A}')
```

The previous section of code returns an error because of the _data type_ of the variables ```b``` and ```h```. We can investigate ```b``` and ```h```'s data type with Python's ```type()``` function.

```{code-cell} ipython3
try:
    b = input('base of triangle: ')
except:
    b = '5'
try:
    h = input('height of triangle: ')
except:
    h = '10'
print(f'b and h are of type: {type(b)}, {type(h)}')
```

Notice both ```b``` and ```h``` are strings, even though the numbers ```5``` and ```2``` were entered as input. The output of the ```input()``` function is always a string, even if the user enters a number. 

To complete the area calculation, ```b``` and ```h``` first need to be converted to floats using Python's ```float()``` function, then the mathematical operation will run without error:

```{code-cell} ipython3
try:
    b = input('base of triangle: ')
except:
    b = '5'
try:
    h = input('height of triangle: ')
except:
    h= '10'
A = (1/2)*float(b)*float(h)
print(f'The area of the triangle is: {A}')
```

Now that you are familiar with Python's ```input()``` function, let's utilize a user's input to decide which lines of code will run. The concept of an selection statement is introduced the next section.

```{code-cell} ipython3

```
