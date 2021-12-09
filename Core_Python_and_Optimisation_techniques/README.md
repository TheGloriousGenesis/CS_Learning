# Python

In Python everything is an object, even types like int and floats (as there are no native number types).
This creates overhead, but is still easier to use hence popularised amongst coders.

Python by default makes shallow copies of the objects made. Some data types are immutable (int, float, tuples), and others are
mutable (list, dict). Immutable means that references can not be altered if copied to another variable, whereas 
mutable means that references can be changed if copied and manipulated in another variable.

immutable values can keep new state if manipulated within the inner scope of a method (unless value is reassigned outside method through return).
Mutable values can though.

## Glossary

| Word | Definition|
|:----:|:---------:|
| Forking | Software that provides an interface between the user and the underlying operating system | 
| Threads | Smallest scheduled unit in an operating system |

## Helpful commands

| Command | Definition|
|:----:|:---------:|
| Forking | Software that provides an interface between the user and the underlying operating system | 
| Threads | Smallest scheduled unit in an operating system |

## Variables

Variables in python should not be in camelcase like Java, but supposedly separated by `_`.
- To put formatted string , place `f` before the string in question such as the following: `print(f"Hello {firstname}")`

### Strings

  - To remove empty space from end of string use the `.rstrip()`.
  - To remove empty space from beginning of string use the `.lstrip()`.
  - To remove empty space from both sides of string use the `.strip()`.

### Numbers

  - Dividing numbers will give you a float regardless of number type.
  - Can use underscores to make large numbers readable like the following `universe_age = 14_000_000_000`.
  - Add commas to variables for multiple assignments `a, b, c = 1, 2, 3`.
  - Use capital letters to represent constant type of variables in python (although there are no built-in constant types
in python)

## Lists

Python lists do not need to be declared as they are a part of Python (unlike arrays, that need to be imported from a seperate module,
either `array` or `numpy`)

- Label list as plural as they contain multiple elements so `fruits = ['apple', 'banana']` not `fruit = [...]`.
- Square brackets `'[]'` indicate list.

Although lists are easy to use, Arrays are preferred as they can store data very compactly (good for storing large amounts of data).
Arrays also great for numerical operations as lists can not handle math operations on the list elements easily

## Dictionaries (HashMaps)

Dictionaries are like hashmaps in other languages. Under the hood, dictionaries uses a hash function to generate the addresses
of the locations of the item. They work in the same way as normal hashmap, they do not allow duplicate key entries, keys can be of
immutable types (boolean, tuple etc)

## Sets

Python also has inbuilt set type. This allows unique objects to be stored in a variable. Can be declared via `set()`
or `{}`. Elements within a set can be of different types (as commonly seen with other python inbuilt types). A set is an immutable 
object and can only hold immutable types (so )

Must remember:
- **Sets do NOT keep order! They are unordered data structures!** But maps/dicts *do*! BIG HINT ENERGY


## Python in-built functions
|Function|Definition|
|:------:|:--------:|
|`locals`| Defines the local variables, methods, classes within a function in a map format (what the compiler knows)|

## Data streams


## Specific helpful commands
`%timeit` function is very helpful to see how long a piece of code has taken to execute.
`input()` read from input

## System Programming

## Forking

During forking, apart from the address space used for the child and parent, everything regarding the parent process is 
identically duplicated in the child. The child and the parent processes can now independently operate.

> The return value from the .fork() method tells us whether we are in the child process (== 0), 
in the parent process  (==  x > 0) or an error has occurred (== x < 0)

```python
import os

def child():
    print("\n new child ", os.getpid())
    os._exit(0)
    
def parent():
    while True:
        newpid = os.fork()
        ## return value from fork() tells us if we are in
        if newpid == 0:
            child()
        else:
            pids = (os.getpid(), newpid)
            print("parent: %d , child: %d \n" % pids)
        reply = input("q for quit / c for new fork")
        if reply == "c":
            continue
        else:
            break
   
parent()
```

## Lambda

## Sorting

Commonly used sorting methods include the `.sort` and the `sorted` method in python. Both are used in similar way. 
To provide custom function to sorting algo, best use `sorted` as it allows more variation in

## Tasks


## Threads

<em><strong> "Smallest scheduled unit in an operating system" </strong></em>

- Threads exist in the space of a process, where there can be many threads to a given process.

- Threads are linked via tasks and can only be created when a program is forked in multiple parallel tasks **

## SDK
To set up an installer, write a setup configuration file (`setup.cfg`) as well as a setup script (`setup.py`) file.

Order in which the system executes files:

1. Installer
2. Setup.py
3. Setup.cfg
4. Command-line

## Conventions

Although python is not strictly typed, having strictly typed conventions helps make the code cleaner to read and minimises
bugs. This means defining the type of the output of the methods (e.g `def my_method(): -> str`)

## Class method and variation annotation

|Decorator|Definition|
|:--------:|:--------:|
|`@dataclass`| Useful for a class that has many attributes, has own define hash, equals method|
|`@abc.abstractmethod`| Must extend `abc.ABC`. Attached to methods so that class that extends from this can not be instantiated unless abstract methods implemented|
|`@property`| Has three methods, getter, setter and deleter. Define these methods by using the name of the method the decorator is attached too then adding `.setter` etc to it e.g `@exampleMethod.setter`|

## Types

### Abstract Types

With abstract type, the abstract class holds the constructor (`__init__`). So classes that extend do not need to define this method

### Type primitives

|Type|Definition|
|:--------:|:--------:|
|Union| define type as one type or the other. Defined as `Union[int, str]`|
|||

## Naming function
[The importance of underscore in Python](https://www.datacamp.com/community/tutorials/role-underscore-python)

- A single underscore prefixing method name signifies that the method is intended for internal use (not enforced by python
  as not strongly typed).
- Although not strictly enforced, if methods are **ALL** imported from modules (with `*`), methods with prefixing `_` do not get imported
- Double line before and after the method name (`__exampleMethod__`) used so that python knows that user does not want to use
  name as variable (like linting). These are called *magic methods*

## Testing in python

### Fixtures
- In pytest, it uses fixtures. Fixtures provide content to use for tests (like a database or predefined object).
- They are activated in a test by using the same name of the fixture, must have the same name in the method parameter if
  a fixture would be used in another fixture (example below):

```python
import pytest

class Fruit():
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

@pytest.fixture
def my_fruit():
    return Fruit("apple")

@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]

def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
```

To have a runnable test, prefix the method with `test_` in order to have runnable test. Ensure fixtures do not have prefixed
'test' names

### Parameterized

`@pytest.mark.parametrize("input, output", [(val, out)])`
Creates inputs and expected outputs, parametrized the methods it's attached to.
Input and expected output define within one bracket.


`@pytest.mark.usefixtures("")`

## Logging

Python has its own built-in logging function. This is called through `logging.getLogger(__name__)`. This calls the logger
using the modules name (given by `__name__`).

## Tips for interviews:
- See the restraints of the variables and estimate what the complexity should be
- Know your time and space complexity well!
- Use hash-tables where you can! The space complexity (O(n)) in trade for speed is helpful when you need to find something
  (or find the opposite of that something) in a table! Remember they can be used in double/triple sum to see if a part of a solution 
exist in map
- Think about constraints to problem! Constraints to variables (smallest it can be, biggest is can be). Best way to do this is
question the example given! why the numbers used, why the size, everything
- Try and not think about redundancy. with lists that are of the same size do you need additional variables to store lengths or can you just use knowhow
- Use bfs to search for questions that require you to search a search space and can trigger
- Runtime complexity:
  - If search space halves each iteration ~ O(LogN)
  - If recursive ~ Time: O(branches ^ depth), Space: This depends how much memory exists at a time
  - If outer loop starts 0 -> N and inter loop starts outer -> N: O(N^2)
  - Double loop -> O(N^2)
  - Sorting algorithm: O(NLogN)
  - Depth of (balance) binary tree: LogN 
  - Think of problems in smaller chunks!
  - 10^4 > is too large for recursive issues (or anything that requires O(n^2) functionality!)
  - Anytime you have to use data from previous solution, think recursive too! But remember space complexity! when you recurse
without an accumulator that passes through in the method, you are requiring the system to call stack to save result from previous result
Try and pass accumulators through to reduce space complexity