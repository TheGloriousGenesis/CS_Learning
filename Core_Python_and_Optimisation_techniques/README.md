# Python

## Glossary

| Word | Definition|
|:----:|:---------:|
| Forking | Software that provides an interface between the user and the underlying operating system | 
| Threads | Smallest scheduled unit in an operating system |

## Variables

Variables in python should not be in camelcase like Java, but supposedly separated by `_`.
- To put formatted string , place `f` before the string in question such as the following: `print(f"Hello {firstname}")`

### <strong> Strings </strong>

  - To remove empty space from end of string use the `.rstrip()`.
  - To remove empty space from beginning of string use the `.lstrip()`.
  - To remove empty space from both sides of string use the `.strip()`.

### <strong> Numbers </strong>

  - Dividing numbers will give you a float regardless of number type.
  - Can use underscores to make large numbers readable like the following `universe_age = 14_000_000_000`.
  - Add commas to variables for multiple assignments `a, b, c = 1, 2, 3`.
  - Use capital letters to represent constant type of variables in python (although there are no built-in constant types
in python)

## Lists

- Label list as plural as they contain multiple elements so `fruits = ['apple', 'banana']` not `fruit = [...]`.
- Square brackets `'[]'` indicate list.

## Data streams

## Redirections

## Variables and Modules

## Shell

## Specific helpful commands
`%timeit` function is very helpful to see how long a piece of code has taken to execute.


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


## Tasks


## Threads

<em><strong> "Smallest scheduled unit in an operating system" </strong></em>

- Threads exist in the space of a process, where there can be many threads to a given process.

- Threads are linked via tasks and can only be created when a program is forked in multiple parallel tasks **



