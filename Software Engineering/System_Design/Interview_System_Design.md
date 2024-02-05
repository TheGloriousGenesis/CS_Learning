# Steps to answering System Design Interview

Depending on the domain in which the system design question is being asked, the 
architecture discussed will be different. For a Software Engineer role the most basic 
structure is Client, Server, Database. Each of these require different 
requirements of the application.

## Step 1: Outline use cases, constraints and assumptions (5-10 mins):

Repeat the requirements to the interviewer and note them down to have a clear idea 
of the points that need to be covered.

- How many times this application will be used?
- Who going to use it? (user or system?)
  - How are they going to use it (technologies)?
- How many users are using the software?
- How much data is the application/service using?
- What is the expected read to write ratio?
- How can the data be discovered?
- What are the main features?
- How can the software be solved in small case (limited users, on a single PC for example)?
- Are analytics/personal information being tracked? How?
- Are analytics/personal information being shown to the user (think name or profile for a website)?

## Step 2: Define user stories (Like jira) (5 mins):

User stories are an end goal to a feature that you would need to implement in the software.
Think about the requirements of the user, both functional and non-functional.

Example of Functional requirements:
- "As a user, I would like to access diagrams via apk"
- "User is able to login in and see list of recommendation songs"
- "User is not anonymous : storing basic information"

Example of Non-Functional requirements:
- "Service is highly available"
- "Service is Reliable"
- "Service is Available/Consistent"
- "Service is Scalable" (how many people, how much interaction with the application)
- "Service is Fast/Low latency" (time dependant applications, how much time can be utilised before interaction in the app)

With generating user stories, it can be important to think about the CAP Theorem and
**reinstate** functional and non-functional requirements.

## Step 3: Define additional requirements
- Security, Cost, Human Resources available, Deadline, other business requirements

## Step 4: Estimating capacity and defining constraint

In order to plan for failure the following must known:

1. What is the Read to write ratio?
2. Traffic (what does scalability mean for traffic? Think about load balancers (sits between client and web server)
3. What data is getting transferred (In terms of data types)? How many versions,
4. Network Protocol Type: e.g HTTP which depends TCP and UDP, websockets TCP
5. Storage Type: 
   1. Database Normalisation (including redundant data in db),
   2. Binary storage, sql, no sql, 
   3. Metadata(usually no sql), 
   4. Database partitioning (Used to perform query performance - selective loading of only relevant partitions)
      1. Also think about indexing
6. Memory (Is a cache needed?) when should it get invalidated between database and application layer, application writes to cache if info retrieved from db)
and CDN (frontend caching system content delivery network)
7. Asynchronous Processing & Queues (for writes that tale a long time)
8. Bandwidth: (to support/requirement —> related to latency: The maximum data that can be transferred in of time)
9. Throughput: The actual amount of data transferred at a given time

## Step 5: Design core components! Start writing down the components
The minimum design in these interviews is usually a cilent -> web server -> database

- Ask if you should do high level design, or discuss API or focus on database design/ data model
- Define high level design with important components
- Tiers:
  - Presentation tier 
  - Web tier 
  - Business tier 
  - Data tier
- Draw Arrows on the diagram and describe what is happening (API request pull html file to machine)