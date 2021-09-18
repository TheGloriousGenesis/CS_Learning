# Python

### Glossary
| Word | Definition|
|:----:|:---------:|
| Forking | Software that provides an interface between the user and the underlying operating system | 
| Threads | Smallest scheduled unit in an operating system | 


## Data streams

## Redirections

## Variables and Modules

## Shell


## System Programming

## Forking

During forking, apart from the address space used for the child and parent, everything regarding the parent process is 
identically duplicated in the child. The child and the parent processes can now independently operate.

> The return value from the .fork() method tells us whether we are in the child process (== 0), 
in the parent process  (==  x > 0) or an error has occured (== x < 0)

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
## Tasks


## Threads

<em><strong> "Smallest scheduled unit in an operating system" </strong></em>

- Threads exist in the space of a process, where there can be many threads to a given process.

- Threads are linked to tasks as threads are only created when a program is forked in multiple parallel tasks **

