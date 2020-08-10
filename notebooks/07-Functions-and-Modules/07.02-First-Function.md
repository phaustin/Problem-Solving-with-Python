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

## First Function

+++

### Defining Functions in Python

+++

Function definitions in Python typically contain at least two lines. The first line defines the function name and arguments. The last line typically defines the function output. In between is the code that runs when the function is called.

```text
def function_name(arguments):
    <code>
    return output
```

The first line of code above contains a couple of parts:

```text
def
```

The keyword ```def``` needs to be the start of the line that declares the function. ```def``` stands for _definition_ and indicates to the Python interpreter that a function definition will follow.

```text
function_name
```

Each function needs a name. The function name must start with a letter (or underscore) and is typically all lowercase (in Python, names that start with Uppercase are usually used to define _classes_). Function names can only contain letters, numbers and the underscore character. Just about any name will do, but it is best to avoid using any Python keywords such as ```def```, ```class```, ```if```, ```else```, ```for```. A complete list of reserved Python keywords is in the Appendix.  

```text
(argument):
```

Function names are followed by a set of parenthesis ```( )```. Many functions have code, called _arguments_ in between the parenthesis. The name used for the function argument(s) should be used in the body of the function. After the function name, parenthesis, and arguments comes a ```:``` colon. In Python, a colon is required to end the first line of all functions.

+++ {"latex": {"environment": "alert-warning"}}

<div class="alert alert-warning" role="alert">
  <strong>A colon :</strong> is required at the end of the first line of every function. If the <strong>:</strong> is not present the code will not run.
</div>

+++

```text
<code>
```

The body of the function contains the code that will run when the function is called. Any variables declared by the function arguments can be used in the body of the function. Any variables used in the body of the function are _local variables_.  Local variables cannot be called or accessed by other scripts, or used outside the function body.

```text
return
```

The ```return``` keyword is often the last line of a function. ```return``` indicates that whatever expression that follows is the output of the function. The ```return``` keyword is not a function or a method, and parenthesis are not used after ```return```, just a space.

```text
output
```

Whatever expression is included after ```return``` will be _returned_ by the function. The output expression after ```return``` can be a single variable, value or be a complex expression that includes multiple variables.

+++

### Your First User-defined Function

+++

When you write your own functions, called _user-defined functions_, consider these criteria:

 * What will you name the function?
 * What, if any, input arguments will the function accept?
 * What will the function do? What is the purpose of the code that runs when the function is called?
 * What, if any, output will the function return?
 
Let's write a simple function which adds two to any number. We will call our function ```plustwo```. Our function has one input argument, a number. The function will return that number plus ```2```. 

Let's apply this description to our four criteria:

 * Function name: ```plustwo```
 * Input arguments: a number
 * What does the function do: add 2 to any number
 * Output: a number (2 + the input number)


Our ```plustwo()``` function will operate as shown below:

```python
plustwo(3)
5
```

The code section below defines our ```plustwo()``` function. 

```{code-cell} ipython3
def plustwo(n):
    out = n + 2
    return out
```

The code section above includes the keyword ```def```, a space and then the function name ```plustwo```. The input argument, ```n```, is enclosed in parenthesis ```(  )``` after the function name. After the set of parenthesis is a colon ``` : ```. The body of the function includes the code ```out = n + 2```. The last line of the function includes the keyword ```return``` followed by a space and the variable ```out```. Note variable ```n``` is a _local variable_ and can only be used inside the function definition.

Let's run our ```plustwo()``` function and see the output.

```{code-cell} ipython3
plustwo(3)
```

The output of the ```plustwo()``` function can be assigned to variable.

```{code-cell} ipython3
ans = plustwo(10)
ans
```

```{code-cell} ipython3

```
