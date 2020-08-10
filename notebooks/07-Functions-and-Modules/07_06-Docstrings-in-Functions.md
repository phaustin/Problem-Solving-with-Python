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

## Docstrings in Functions

+++

It is good programming practice to document your code. Reusable chunks of code are particularly relevant to document as other programmers may use the code, and you may use the code again at a different time. 

Python has a couple of different ways for programmers to add documentation. One way is to use simple comments. Comments are lines of code that do not get run by the Python interpreter. Comments are meant to be viewed by humans. In Python, comment lines start with the pound symbol ```#```. Any line that starts with a ```#``` symbol will not be run by the Python Interpreter.

Another way to document code is to use _docstrings_. Docstrings are comments which are surrounded with triple quotation marks and usually contain multiple lines of explanation. A function containing a docstring takes the form:

```
def function_name(arguments):
    """"
    Docstring text
    
    
    
    """
    <code>
    
    return output
    
```

Doc strings are what you see when the ```help()``` function is called. As an example, running the ```help()``` function on the built-in function ```sum``` brings up:

```{code-cell} ipython3
help(sum)
```

We can produce the same type of output when a user types types ```help()``` by adding docstrings to a function.

+++

Let's create a new function that converts grams (g) to kilograms (kg). 1000 grams is equal to 1 kilogram. Let's call our function ```g2kg```. Remember the **parenthesis**, **colon**, and **return** statement. 

```{code-cell} ipython3
def g2kg(g):
    kg = g/1000
    
    return kg
```

Now let's try and use our function. How many kilograms is 1300 grams? We expect the output to be ```1.3``` kilograms.

```{code-cell} ipython3
g2kg(1300)
```

If we call ```help()``` on our ```g2kg()``` function, nothing is returned. ```help(g2kg)``` does not return any output because our new ```g2kg()``` function does not contain a docstring yet.

```{code-cell} ipython3
help(g2kg)
```

If we insert a docstring into the function definition, ```help(g2kg)``` will return whatever text we included in the docstring.

The standard components of docstrings included in function definitions are:

 * a summary of the function
 * the function inputs
 * the function outputs
 * an example of the function running including the result
 
The docstring is included right below the ```def``` line and is enclosed in triple quotes ```"""  """```. The triple quotes are typically included on their own lines. The syntax to add a docstring in a function definition is below.
 
```text
 def function_name(arguments):
     """
     
     <docstring text>
     
     """
     
     <code>
     
     return output
```

Let's include a docstring with our ```g2kg()``` function definition.

```{code-cell} ipython3
def g2kg(g):
    """
    
    Function g2kg converts between g and kg
    
    input: number of grams, int or float
    output: number of kilograms, float
    
    Example:
    
        >>> g2kg(1300)
            
            1.3
        
    """
    kg = g/1000
    
    return kg
```

Now let's ask for ```help()``` on our ```g2kg()``` function and see the docstring we wrote in the ```g2kg()``` function definition printed back to us.

```{code-cell} ipython3
help(g2kg)
```

```{code-cell} ipython3

```
