# Design Patterns

## Glossary

| Word | Definition|
|:----:|:---------:|
| Design Pattern | Solutions to implement that addresses issues surrounding coding software for change. |
| Observer Pattern | One to many dependency between objects, dynamically updating multiple objects depending on the change of state of given object |

## Basics
To understand design patterns, we must first understand Object-Orientated basics and principles. 

| OO basics| Definition |
|:--------:|:----------:|
| Abstraction | Ensure there is one functionality to each core piece of code/method |
| Encapsulation | Combining data and behaviour in a package and hiding implementation away from the users of the package |
| Polymorphism | Objects inheriting from same parent can be exchanged during instantiation |
| Inheritance | Child components obtain functionality and variables from parent classes |

| OO Principles | Explanation |
|:-------------:|:-----------:|
| <em> ' Encapsulates what varies ' </em> | To ensure there is no repetition of the code base |
| <em> ' Favor composition over inheritance ' </em> | To ensure flexibility, favour interfaces over class inheritance if possible|
| <em> ' Program to interface, not implementation ' </em> | To ensure flexibility and extension of code base if needed |


# ==Software design patterns (prevalent in python)==


## SOLID principles

### Single Responsibility Principle

- *Each class/module/service/component should only have one responsibility*

### Open-Close Principle

- *Should be able to extend class behaviour without extending it*

This means the classes should be open for extension (the class behaviour can be 
extended) but closed for modification (mean the source code written should not be changed).

Usually this is done through the use of polymorphic substitution 

### Liskov Substitution Principle

- *Ever derived class should be substituted for its parent class*

All classes must derive base class without changing behaviour of base class

**Child class should be able to exchange with parent class without raising error**

### Interface segregation principle

- *Make fine-grained interfaces that are client specific, as it is better to have a lot smaller ones than few larger ones*

Have a class implement new interfaces over adding methods to existing interfaces.


### Dependency Inversion Principle

- *Code to interface not to concrete implementations*

==Look at dependancy inversion pattern?==


## Observer Pattern
*<strong> Publishers (<span style="color:green"> subject </span>) + Subscribers (<span style="color:green"> observers </span>)
= Observer Pattern </strong>*


## Sharding and data distribution
