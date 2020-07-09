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

+++ {"latex": {"before_cell": "newpage"}}

## Summary


+++

In this chapter, you learned about symbolic math and how to complete symbolic math calculations with Python the SymPy package. Symbolic math treats variables as mathematical symbols rather than defining variables as numbers. 

At the start of the chapter, you learned how to create symbolic math variables with SymPy's ```symbols()``` function.

Symbolic math variables can be combined into symbolic math expressions and symbolic math equations. You learned how to substitute variables and numbers into symbolic math expressions and equations. 

At the end of the chapter, you learned how to solve linear and quadratic equations with SymPy. 

The final example in the chapter was a multi-variable statics problem where two equations were solved for two unknowns. 

+++

### Key Terms and Concepts

+++ {"latex": {"environment": "key_terms"}}

symbolic math

symbolic variable

object

numerical calculation

systems of equations

expression

equation

substitution

evaluate

linear equation

quadratic equation

+++

### SymPy Functions and Methods

+++

| SymPy Function | Description | Example |
| --- | --- | --- |
| ```symbols()``` | Define a symbolic math variable | ```x, y = symbols('x y')``` |
| ```.subs()``` | Substitute a variable or value | ```expr.subs(x, 2)``` |
| ```Eq()``` | Define a SymPy equation | ```eq1 = Eq(4*x + 2)``` |
| ```solve()``` | Solve a SymPy expression or equation | ```solve((eq1,eq2), (x, y))``` |

```{code-cell} ipython3

```
