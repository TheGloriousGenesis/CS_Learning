# Python

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

## Logging

Python has its own built-in logging function. This is called through `logging.getLogger(__name__)`. This calls the logger
using the modules name (given by `__name__`).


