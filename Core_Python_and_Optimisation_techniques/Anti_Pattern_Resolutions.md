I created this to help me improve my knowledge of some of the best practices i wasn't aware of when working in python. Follow in line with PEP 8 Styling standards. Credit [here](https://docs.quantifiedcode.com/python-anti-patterns/index.html) in helping me!

## 1. Do not assign lambda expression to variable
```python
# No
some_variable = lambda x: x + 2
# Yes
def some_func(x): return x + 2
```

## 2. Include `break` statement in loop
- Include break statements when you have a `for-else` loop in the following manner:
```python
from typing import List

def contains_even_number(list_of_numbers: List[int]) -> None:
    for number in list_of_numbers:
        if number % 2 == 0:
            print("Even number found!")
            # here break is important, otherwise the else clause will execute when for loop is finished/ empty list!
            break
    else:
        print("Sorry, no even numbers found")
        
contains_even_number([1,2,4,5])
```

## 3. Place `__future__` import at the very top of the file
- `__future__` import allows you to use future functionality available in later python versions within the file it's imported into. It's important to put it before any code/import as random behaviour could happen if this is not the case!  

## 4.