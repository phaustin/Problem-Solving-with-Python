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

## For Loops

+++

In this chapter, you will learn about two kinds of _repetition structures_ in Python: _for loops_ and _while loops_. This section describes for loops.

_For Loops_ are a component of many programming languages. A _for loop_ is a repetition structure where a section of code runs a specified number of times. 

Say we want to print out the statements:

```text
Problem solving in teams
Problem solving in teams
Problem solving in teams
```

One way to accomplish this task is by coding three print statements in a row:

```{code-cell} ipython3
print('Problem solving in teams')
print('Problem solving in teams')
print('Problem solving in teams')
```

Another way to accomplish the same task is to use a for loop. The basic structure of a for loop in Python is below:
    
```python
for <var> in range(<num>):
    <code>
    
```

Where ```<var>``` can be any variable, ```range(<num>)``` is the number of times the for loop runs and ```<code>``` are the lines of code that execute each time the for loop runs. 

Note the for loop starts with the keyword ```for``` and includes a colon ```:```. Both ```for``` and the colon ```:``` are required. Also, note ```<code>``` is indented. Each line of code that runs as part of the for loop needs to be indented the same number of spaces. Standard indentation in Python is four spaces. 

The example above can be rewritten using a for loop:

```{code-cell} ipython3
for i in range(3):
    print('Problem solving in teams')
```

#### Python's ```range()``` function

Python's ```range()``` function returns an iterable list of values starting at zero and ending at ```n-1```. For example, when ```range(3)``` is called, the values ```0, 1, 2``` are returned. ```3``` is not part of the output, even though the function input was ```range(3)```. We can be confirm the behavior of ```range()``` with a for loop:

```{code-cell} ipython3
for i in range(3):
    print(i)
```

**Remember Python counting starts at ```0``` and ends at ```n-1```.**

+++

#### Customizing ```range()```

Python's ```range()``` function can be customized by supplying up to three arguments. The general format of the range function is below:

```python
range(start,stop,step)
```

When ```range(3)``` is called, it produces the same output as ```range(0,3,1)``` (```start=0```,```stop=3```,```step=1```). Remember Python counting starts at ```0``` and ends at ```n-1```. If only two arguments are supplied, as in ```range(0,3)```, a ```step=1``` is assumed.

The table below includes examples of the Python's ```range()``` function and the associated output.

| ```range()``` function | output |
| --- | --- |
| ```range(3)``` | 0, 1, 2 |
| ```range(0,3)``` | 0, 1, 2 |
| ```range(0,3,1)``` | 0, 1, 2 |
| ```range(2,7,2)``` | 2, 4, 6 |
| ```range(0,-5,-1)``` | 0, -1, -2, -3, -4 |
| ```range(2,-3,1)``` | (no output) |

A code section that uses a for loop and ```range()``` with three arguments is below:

```{code-cell} ipython3
for i in range(5,9,1):
    print(i)
```

### For loops with lists

For loops can also be run using Python lists. If a list is used, the loop will run as many times as there are items in the list. The general syntax is:

```python
for <var> in <list>:
    <code>
```
 
Where ```<var>``` is a variable name assigned to the item in the list and ```<list>``` is the list object. Remember to include a colon ``` : ``` after the list.  ```<code>``` is the programming code that runs for each item in the list. 

An example of a list in a for loop is  below:

```{code-cell} ipython3
my_list = ['electrical','civil','mechanical']
for item in my_list:
    print(item)
```

The loop ran three times because there are three items in ```my_list```. Each time through the loop, the variable ```item``` is set to one of the items in the list.

 * first time through the loop, ```item='electrical'```
 * second time through the loop ```item='civil'``` 
 * third time through the loop ```item='mechanical'```. 

+++

### For loops with strings

For loops can also be run using strings. In Python, strings can be indexed just like lists. A loop defined by a string runs as many times as there are characters in the string. The general structure a for loop using a string is:

```python
for <char> in <string>:
    <code>
```
 
Where ```<char>``` is one of the characters in the string ```<string>```. Just like for loops with ```range()``` and for loops with lists, make sure to include a colon ``` : ``` after the list.  ```<code>``` is the programming code that runs for each character in the string. ```<code>``` needs to be indented

An example of a string in a for loop is below:

```{code-cell} ipython3
for letter in "Gabby":
    print(f"looping over letters in name: {letter}")
```
