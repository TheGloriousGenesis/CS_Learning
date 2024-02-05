# Distributed systems


## Glossary

|              Word               |              Definition              |
|:-------------------------------:|:------------------------------------:|
| The Byzantine Generals' Problem |                  -                   |
|              CAP                | Consistency, Availability, Partition |

## Traditional systems

In a traditional centralized system there are two main components:
- client (makes requests)
- server (completes requests and acts like centralized middleman between clients)

Having a centralised system works fine (currently used for web/app to app communication)
but is sensitive to influence by third evil entity. Distributed system came into play where
the server is split onto nodes. All nodes can be a client or a server or both and nodes are 
distinguished from each other (making it more safe as attacker wouldn't know what component 
they interact with- good for privacy?)

## CAP Theorem
[Clear simple example](http://tinyurl.com/4djnzh3m)

When we are designing a distributed system, we can only have 2/3 desired characteristics:
- Consistency: Up-to-date data - whenever a user modifies data that modification is available as soon as to all nodes
- Availability: Always able to access data
- Partition tolerance: If there are communication issues between nodes, system should still work

<details><summary> <b>Database management system CAP</b> </summary>
<a href="https://www.ibm.com/topics/cap-theorem">Databases types for distributed systems</a>

Databases are classified into three types depending on the two characteristics they satisfy in CAP theorem: CP, AP, CA.
In distributed systems, you actually can't have a CA distributed database **BUT** you can use relational databases (CA) 
such as **PostgreSQL**

NoSQL databases are commonly used for distributed systems as they are horizontally scalable and distributed by design.
</details>

## Distributed systems building blocks

Groups of containers co-located on a single machine make up the atomic elements of a distributed system (the nodes)

Containerization main purpose is to:
- Create boundaries around resource allocation 
- Create boundaries around team ownership
- Create boundaries around separation of concerns  

This is the reason why containerization is very helped. It allows easier testing, updating, deploying and flexibility.

## Single node patterns

The idea of running multiple containers on a single node (machine). Think of multiple 
containers on the same pod in kubernetes.

### Sidecar pattern

Add functionality to existing application without refactoring or amending existing application and deploy this solution to the same space that shares
resources with the original application. The sidecar and the main application share state (e.g same network, disk etc) so they do not have to
send messages insecurely.

Sidecar should be modular and reusable

To ensure you can do this, ensure that:
<details><summary>Parameterizing containers</summary>
- Consider containers as a function in your program
- Consider parameters (environment vars) as inputs to this function
</details>

<details><summary>Creating the API surface of container</summary>

</details>

<details><summary>Document operation of container</summary>

</details>







