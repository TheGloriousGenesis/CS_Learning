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

## 4. Do not use mutable object as a default value to function 
- In the below code, Python will only create the first instance of the list the first time the method is called. Use `None` instead.
```python
def add(x: int, y: List[int]=[]) -> int:
    y.append(x)
    return y
```

## 5. Use defaultdict to create dictionary with default values for all elements
- For example:
```python
def count_occurences(sentence: str, letter: str) -> int:
    letter_map = defaultdict(lambda: 0)
    for character in sentence:
        if character.isalpha() and charcater not in letter_map:
            letter_map[character]+=1
```

## 6. Use setdefault to set specific element of dictionary to given value
```python
def store_value(number: int):
    value_map = dict()
    value_map.setdefault("a", 6)
```

## 7. Use unpacking of a list instead of invidual assignment of elements in list
- For example:
```python
def print_second_item(numbers: List[int]) -> None:
    _, number, _ = numbers
    print(number)
```

## 8. Be weary of the `setattr` method when dynamically creating functions/methods/variables
- It is bad practices to set class variables, functions etc (example below) at instantiation. Think about either doing something with that data within the method, or not storing those values within a class
```python
class helepr:

    def __init__(self, list_of_values: List[str]):
        counter=0
        for i in list_of_values:
            setattr(self, counter + i, i)
            counter++
```
Do something like this instead:
```python
class helepr:

    def __init__(self, list_of_values: List[str]):
        counter=0
        for i in list_of_values:
            process_value(i, counter)
            counter++
```

## 9. Ask for forgiveness not permission! Assume necessary things exist and use `try / except`  instead of `if` .

## 10. 

