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

## While Loops

+++

A _while loop_ is a type of loop that runs as long as a logical condition is ```True```. When the logical condition becomes ```False```, the loop stops running. The general form of a while loop in Python is below:

```python
while <logical_condition>:
    <code>
```

The keyword ```while``` must be included, as well as a ```<logical_condition>``` which can be evaluated as ```True``` or ```False```. The ```<code>``` after the while statement must be indented. Each line of code runs in the while loop needs to be indented the same number of spaces. (Many code editors, including Jupyter notebooks, auto-indent after a ```while``` statement) If you add indentation manually, four space spaces is the Python standard.

An example of a while loop is below:

```{code-cell} ipython3
i = 0
while i<4:
    print(i)
    i = i+1
```

The first line ```i=0``` creates the variable ```i``` and assigns it the value ```0```. The next line declares the logical condition needed to keep the loop running. The statement ```i<4``` is ```True``` or ```False``` depending on the variable ```i```. Since ```i=0```, the statement ```i<4``` is ```True``` and the while loop starts to run. The code inside while the loop prints the value of ```i``` then increases ```i``` by ```1```. When ```i=4```, the statement ```i<4``` is ```False``` and the while loop ends.

+++

### Using a while loop to validate user input

While loops can be used to validate user input. Say you want to insist that a user inputs positive number. You can code this into a while loop that keeps repeating ```'Enter a positive number: '``` until the user enters valid input. 

The code below continues to ask a user for a positive number until a positive number is entered. 

```{code-cell} ipython3
num_input = -1
while num_input < 0:
    str_input = input('Enter a positive number: ')
    num_input = float(str_input)
```

In the section of code above, it is important to initialize the variable ```num_input``` with a value that causes the statement ```num_input < 0``` to evaluate as ```True```. ```num_input = -1``` causes the statement ```num_input < 0``` to evaluate as ```True```. Besides ```num_input = -1```, any other negative number would have worked.

If the while statement can't be evaluated as ```True``` or ```False```, Python throws an error. Therefore, it is necessary to convert the user's input from a string to a float. The statement ```'5' < 0``` does not evaluate to ```True``` or ```False```, because the string ```'5'``` can't be compared to the number ```0```.
