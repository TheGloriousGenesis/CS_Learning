# System Design

## Glossary

| Word | Definition|
|:----:|:---------:|
| Shell | Software that provides an interface between the user and the underlying operating system | 

## Introduction
Architecturing is decomposing system into coding blocks units and optimising communication between them
Number one reason to do new architecture is because system is at end of life.

## Things to avoid when developing architecture

### <span style="color:red"> 1. Avoid Functional Decomposition </span>
- Creates an inherit dependancy of processes before and after. 
- Creates a time dependancy on services to be done before and after
- Creates duplication of code throughout code base
- Requires client knowledge to implement design (must know that A is before B)
- Increases multiple point of entry (must go to A, then go to B). High security issue.
- Creates coupling, creates an inability to handle change!
- Everytime there is change in requirements, theres change in solution! Very bad

### <span style="color:red"> 2. Avoid encapsulating possible change to nature of business </span>


### <span style="color:green"> 1. Do: Decompose based on volatility! </span>
- Identify areas of change (can be functional but not domain functional)
- Encapsulate these areas in services
- Create methods based on interactions between services (think of organs and how they encapsulate volalities)
- Do not resonate with the change!

### <span style="color:green"> 2. Do: Practice on Non-Software systems! </span>
- Decompose how to make a bike

### Create system that can do regression testing
- test subsystems and interactions between them

## Design Techniques/Processes
- Axes of volatility
  - Give system to the same customer over time, how will system change? (will they be happy over time with this?)
    - Example: Same customer over time when building a house: Furniture volatility, Appliances volatility, 
    Occupants volatility, Appearance volatility (change wallpaper, color, add bedroom), Utility volatility

  - Freeze system and give it to current customers, how will customers change? (are they all the same?)
    - Example: Same time across different customers (House now in LA instead of NY): Structure volatility, 
    Neighbour volatility, City volatility
    - Volatility in customers often change how customers interact with the system (through mobile, desktop), as well as 
    how they authenticate (fingerprint, face, through fb), how they authorise (user, trader, admin)

- Axes should be independent of each other (roughly independant as much as posisble)!
- Common example remember that where data is stored is volatile, system notification is volatile
- Axes of volatility should be valid until the end of time.
- Transition from list of areas of volatility to services is hardly ever 1:1. This is because:
  - Sometimes a single service can encapsulate multiple volatile areas
  - Sometimes said area describes an implementable data structure instead of service (or operational concept) (e.g use queue)

## Common components to decompose a problem
- think about scalability especially in regard to devices or how the user will interact with the system
- Think about the underlying services hosting the functions
- Think of the flow and how it could be impeded/blocked (can it be asynchronous? Do we need buffer to know order?)
- The product being used, how does that evolve? (If tasked with stocks, can system deal with commodities?)
- Globalisation regarding versions of your system
- Authorization and various ways it can happen
- Variation in transport/storage of data

- Storage can be database, queue, hash table, file etc


## Layers when VBD'in (Top to bottom)
![image info](./Template System decomposition.png)
### Client

- Advocates single point of entry
- Encapulates different type of clients, the technologies they use and how the information is transported to them

### Business

- capture use cases: series of required behaviours

### Resource access

- Encapsulate resource access
- Physical resources / Utilities common to all services
- 




# TODO
- Think about all the design patterns and what type of volatility they are encapsulating e.g pub/sub pattern encapsulating
publisher, subscriber transport volatility
