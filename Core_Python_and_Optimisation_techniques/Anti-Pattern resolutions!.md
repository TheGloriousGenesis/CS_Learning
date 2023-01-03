I created this to help me improve my knowledge of some of the best practices i wasn't aware of when working in python. Follow in line with PEP 8 Styling standards. Credit [here](https://docs.quantifiedcode.com/python-anti-patterns/index.html) in helping me!

## 1. Do not assign lambda expression to variable
```python
# No
some_variable = lambda x: x + 2
# Yes
def some_func(x): return x + 2
```

## 2. 