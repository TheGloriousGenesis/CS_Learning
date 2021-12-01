# System Design

## Glossary

| Word | Definition|
|:----:|:---------:|
| Shell | Software that provides an interface between the user and the underlying operating system | 
| Behaviour ||
| Functional | Actual requirements of the application e.g User should be able to see website |
| Non-Functional | (CAP Theorem) reliability, availability, latency, scalability|
| Distributed System | A network that stores data on more than one physical/virtual machine|
| CAP Theorem |That no distributed system that can all three at a time: consistency (same data, availability, partition tolerance)|
| HTTP | Method for encoding an transporting data between client and server|
| TCP (Hypertext transfer protocol)| Connection over IP network established through handshake. Less time critical, Used when you need all data to arrive intact, best throughput. Data can be lost though if sender doesn't recieve|
| UDP (User datagram protocol) | Sends packets of data, connectionless (does not require IP address). Less reliable, works real time use cases, video chat, streaming. Used when you need low latency, late data worst than lost data |
| Web Client | Web browser is an example of this. Communicates with web server via HTTP to render HTTP files |
| Web Server | Machine that holds HTTP files ready for when people request the file. In system design, also known as **Managers** or **Services**|

## Conversion
| Measurement | Equivalent|
|:----:|:---------:|
|2.5 million seconds| 1 month|

## Introduction

System design is about decomposing a system into coding blocks and optimising the communication between them.
The number one reason to do it is usually because the system is at the end of it's life.

## Steps to answering System Design Interview

The most basic structure is Client, Server, Database. Each of these levels require different requirements of the application.

### Step 1: Outline use cases, constraints and assumptions (5-10 mins):

- How many times this application will be used
- Who going to use it? (user or system!)
- How they gonna use it (technologies)?
- How many users are we talking about?
- How much data is the application/service using?
- What is the expected read to write ratio?
- How can the data be found?
- What are the main features?
- How can they solve the problem in small case (MAYBE)?
- Are we tracking analytics/personal information somehow?
are we showing the user these anayltics?

### Step 2: Define user stories (Like jira) (5 mins):
Example of Functional requirements:
- "As a user, I would like to access diagrams via apk"
- "User is able to login in and see list of recommendation songs"
- "User is not annoymous : storing basic information"

Example of Non-Functional requirements:
- "Service is highly available"

- Reliability
- Availability (when should application be available (consistent))
- CAP Theorem
- Latency (time dependant applications, how much time can be utilised before interaction in the app),
- Scalability (how many people, how much interaction with the application)

**Reinstate** functional and non-functional requirements.

### Step 3: Define additional requirements
- Security, Cost, Human Resources available, Deadline, other business requirements

### Step 4: Estimating capacity and defining constraint

In order to plan for failure you must know the following:

1. What is the Read to write ratio?
2. Traffic (what does scalability mean for traffic? Think about load balancers (sits between client and web server)
What data is getting transferred (In terms of data types)? How many versions,
Maybe use HTTP which depends TCP and UDP, maybe use websockets TCP)
5. Storage (Database Normalisation (including redundant data in db), Binary storage, sql, no sql, Metadata(usually no sql),
Database partitioning)
6. Memory (Do we need to cache? when should it get invalidated between database and application layer) and CDN (frontend caching system content delivery network)
7. Asynchronous Processing & Queues (for writes that tale a long time)
8. Bandwidth: (to support/requirement —> related to latency: The maximum data that can be transferred in of time)
9. Throughout: The actual amount of data transferred at a given time

### Step 5: Design core components! Start writing down the components
- Ask if you should do high level design, or discuss API or focus on database design/ data model
- Define high level design with important components
- Tiers:
  - Presentation tier 
  - Web tier 
  - Business tier 
  - Data tier
- Draw Arrows on the diagram and describe what is happening (API request pull html file to machine)

- the activity changes (Engines encapsulate this volatility in business rule)
- the sequence changes (Managers are meant to capture this volatility)

## How to break down system: DETAILED: Layers when VBD'in (Top to bottom)
![image info](./SystemDesignPrimer.png)

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
  - Main functions:
    - Bike part retrieval (wheels, frame)
    - Maintenance service (Oiling chains, tire pressure checks, break pad erosion checks)
    - Security (bell, breaks, lights)
    
### Create system that can do regression testing
- test subsystems and interactions between them

## Design Techniques/Processes
- Axes of volatility
  - Give system to the **same customer** over time, how will **system change**? (will they be happy over time with this?)
    - Example: Same customer over time when building a house: Furniture volatility, Appliances volatility, 
    Occupants volatility, Appearance volatility (change wallpaper, color, add bedroom), Utility volatility
    - Example: Same customer over time with ride-sharing app: Location Volatility (User Location),
    Destination Volatility (Where User is going), Car-Type-Request Volatility (Car for Airport Differnt for party, differnt for work),
    Journey Volatility
  
  - **Freeze system** and give it to current customers, how will customers change? (are they all the same?)
    - Example: Same time, different customers when building a house (e.g House now in LA instead of NY): Structure volatility, 
    Neighbour volatility, City volatility
    - **Volatility in customers often change how customers interact with the system** (through mobile, desktop), as well as 
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


## How to break down system: DETAILED: Layers when VBD'in (Top to bottom)
![image info](./Template System decomposition.png)

### Client

- Can be a user or another system (Think about who is going to use it?)
- Advocates single point of entry
- Encapsulates different type of clients, the technologies they use and how the information is transported to them
  - How many users are there?

### Business

- Encapsulates the volatility in the changes of the required behaviour of the system
- Required behaviours when define should be as immutable to change as possible
- Capture use cases: series of required behaviours
- Although the required behaviour of system is liable to change, there is only two ways the use case (a sequence of activities) can change:
  - the activity changes (Engines encapsulate this volatility in business rule)
  - the sequence changes (Managers are meant to capture this volatility)

### Resource access

- Encapsulate volatility to resource access
- Make as high level when describing so that the underlying resource can be swapped if needed.
- Use atomic business verbs (verbs used to describe action in certain field e.g credit, debit account).

### Resource

- Physical resources (File, queues, database)

### Utilities

- Utilities common to all services (e.g security, logging)

## Architecture Validation

- Architecture must satisfy all use cases
  - Present and future
  - Known and unknown
- Volatility decreases top down on layer VBD

# TODO
- Think about all the design patterns and what type of volatility they are encapsulating e.g pub/sub pattern encapsulating
publisher, subscriber transport volatility


