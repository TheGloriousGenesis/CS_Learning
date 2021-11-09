# AWS Cloud Practitioner

Lunch time - 7h30am 

Tea break - 10am

Additional Learning:
- [Skill builder](https://explore.skillbuilder.aws)

Definition:
On demand delivery of IT resources and applications through the internet 

## Module 1: Introduction to Amazon Web Services

Previously required people to maintain and setup data centers and architecture for different environments 
(hardware engineers, network engineer).

AWS (started in 2006), solution to offload the maintenance of datacenters, whilst maintaining control over pricing and
only using what you need.

### Services
Over 200+ services to use!
*Core Services*
- Compute
- Networking and content delivery
- Storage
- Database
- Security and Identity and compliance
- Management and governance

Some commonly used services:
- S3 - data storage
- Macie - Report on security issues on S3, helps check compliancy
- Security - Each service has security specific features as well as there being security services as well (must whitelist ports on app for these)
- EC2 - Virtual servers
- Lambda - Serverless compute

### [Availablity Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
To see what the availablity of services and number of datacenteres Amazon has
Not all services are launched in all the regions at the same time
Check if it is available in region before deploying there!

Each region has AWS Edge network locations, usually heavily used. These are Content Distribution Network (CDN) for the 
whole world. This is done to deliver low latency, high throughput content to end users. Done through 
[AWS CloudFront](https://aws.amazon.com/cloudfront/features/?p=ugi&l=na&whats-new-cloudfront.sort-by=item.additionalFields.postDateTime&whats-new-cloudfront.sort-order=desc).
- Has more 'Points of Presence'
- Caches content closer to the user
- Some Edge locations have a secondary cache

### [Deployment models](https://docs.aws.amazon.com/en_us/sdk-for-net/v3/ndg/gs-cloud-deployment.html)
- Full Cloud (all cloud)
- On premises (private cloud)
- Hybrid (part cloud, part local dc) : For GDPR reasons or learning curve reasons

### Scale 
Can spin up and break down servers at a given moment cheaply due to economy of scale (DCs everywhere), in a PAYG model.
Allows deployment closer to user, hence lower latency, better output for customers.

## Module 2 Compute in the Cloud

### [EC2 Instances](https://aws.amazon.com/ec2/?ec2-whats-new.sort-by=item.additionalFields.postDateTime&ec2-whats-new.sort-order=desc)
EC2 instances are virtual machines running int AWS Datacenters. Self configured and self controlled.
Over 400+ different instances types and sizes to spin up [Click here to see](https://aws.amazon.com/ec2/instance-types/)!
Different EC2 instances have different use cases [stated here](https://aws.amazon.com/ec2/instance-types/). Example, NVMe - 
ephermal storage (transient, good for temp files)

Don't know what instance to choose? Or services? use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/). 
Uses ML to analyse previous use of workload and recommends services.

*Cost is **not** the same for all the regions* e.g Spot, most unreliably but cheapest (up for 6 hrs max)

Helpful web app to view price differences for EC2 per region etc [here](https://ec2types.io/home)

Optimised for different purposes
General - Balance of compute memory and networking resources
Memory - Ideal for high-performance databases
Accelerated - Offers high-performances processors
Storage - Suitable for data warehousing applications (data held for long time)

### Pricing
- On-Demand - Consistent
- Spot - If available can use it, up to 6 hours. Any workload that can be spun up when abruptly stopped
- Reserved - (discount on On-demand, require 1-3 year term commitment)
- Compute Saving Plans - (discount on On-Demand for consistent compute usage, require 1-3 year term commitment)

### Dedicated computing
- Dedicated Instance : EC2 instance that runs in a VPC on hardware (taxi)
- Dedicate Host: Physical server with EC2 instance (personal car)

### Elasticity - Auto Scaling
- Auto Scaling
  - Launch/Tear down server when needed (auto-scaling/ workload increases)
  - Automatically adjusts the number of amazon EC2 instances to match demand
- Elastic Load balancer 
  - Distribute traffic to other servers depending on demand
  - Providing a single point of contact for traffic into the auto-scaling group

### AWS Messaging Service
Monolithic
- Single component application
Microservices
- Decoupled component, allows scaling and development independent of other components

**Simple Notification Service - NOTIFICATIONs**
- Create topic. Have publishers and subscribers to topic
- Push service - Messages automatically pushed to publishers. Limited retries. If publisher don't recieve it, message lost

**Simple Queue Service - QUEUING**
- Send, store and recieve messages (message stored for max 14 days)
- Consumer looks to queue to pick up messages
- Polling service (pull service)

**AWS Lambda - serveless**
- Run code (functions) without provisioning or managing servers
- Pay only for compute time while code is running, how many times code is trigger
- Can have concurrent code running
- Use other AWS service to auto trigger code
- CON - timeout : 15 mins. If more than this, break function to smaller bits or use EC2
  - Can use AWS Step function to create state machine (to create workflow) to orchestrate lambda functions

### Containers
One host with multiple containers
Isolated processes running on a server

To orchestrate multiple containers use:
- Amazon ECS 
- Amazon EKS 
Can also install own kubernetes to deploy and manage by using EC2 and installing software

AWS Fargate
- Serverless compute engine for serverless container orchestration

## Module 3: Global Infrastructure and Reliability

### Region
Important for latency reason
- Check compliance with data governance and legal requirements
- Proximity to your customers
- Available services within a Region
- Pricing
Every region has availability zones (1 OR MORE). Launch EC2 instances across multiple regions just in case zone goes down! 1 availability 
zone belongs to 1 region **only**

### Amazon CloudFront 
EC2 instance --> Edge location (cache) --> customer

Edge location **not** equal to availability zones. Availability zones have 200+ services whereas edge locations have few services
mainly for caching CloudFront data

### AWS Outposts

Extend AWS infrastructure and services to your on-premises data center (like having a starbucks on site!)
- runs instead your datacenter (allows high level of control over data)

Can access role
- Dynamic role generation - AssumeRole

Can access amazon services through CLI, sdk, or through management console UI.

Who can assume roles can be decided by policy to that role


## Module 4: Networking

### Amazon Virtual private Cloud
Private network inside software account.

Inside VPC, launch servers inside it. Some have internet access others do not. There should be subnets which deal with 
that: Public subnet, Private subnet. 

In subnet, there are EC2 instances. 

The VPC--> public subnet: needs internet gateway to connect to internet and receive requests. 
The VPC --> private subnet: needs private internet gateway to connect over VPN to own data

AWS Direct connect : Establish a dedicated connection between on-premises data center and the VPC

### Firewall
Have to set up firewalls! Set up firewalls on subnet level via network access control list (network ACL) and on a 
EC2 level via security group.

**Subnet**
By default, allows all traffic, stateless firewall. Put rules for inbound and outbound traffic.
**EC2**
By default, outbound open, inbound blocked, all traffic, stateful firewall.
Rules for incoming reflect outbound traffics too and EC2 level (security group)

### Route 53
Maintains domain name systems (DNS) records and translates domain name to IP address (domain resolution).

Routes user to internet applications (return IP address of EC2 instance the application running on)

Client --> Route 53 --> Application load balancer

## Module 5: Storage and Databases
Supports 15 databases.

**Block storage**: EBS, single block read/write. Example, laptop memory? block
  - EBS volume - persistent
  - EBS ephemeral - transient
  - EBS snapshots - incremental backup
  - Store data in 1 availablility zone

**Object storage: S3**, each object consists of data, metadata and a key. S3 not publicly accessibly (can expose). 
No size limit for bucket (per file - 5T)
  - S3 Standard - frequently accessed, minim stored in 3 availability zones
  - S3 Standard-IA - infrequently accessed data, minim 3 zones, retrieval more expensive than normal
  - S3 One Zone-IA - stores data in single availability zone (best keep easily regenerate data here)
  - S3 Intelligent Tiering - Monitor how often data accessed. Dynamically move data depending on access
  - S3 Glacier (Archive data, retrieval 3-5 hrs)
  - S3 Glacier Deep Archive (Archive data, retrieval up to 12 hrs)
  
Can run select query on S3
**File storage**: EFS
- Stores data across multiple availability zones


### Databases
Types: Relational (access through SQL, joins etc), non relational

Amazon Relational Database Service (In private subnet)
Engines supported (6):
- Aurora 
  - Also has serverless option for potential non-relational db work
  - Natively relational
  - (keeps 6 copies of data, consistently being backed up, 3 times faster than MySQL, and 5 times faster than PostgresSQL)
- PostgreSQL
- MySQL
- Microsoft

Amazon DynamoDB (for non-relational db)
- Serverless 
- Amazon prime day runs on this!

Analyse and query data from across data warehouses? use Amazon Redshift

## Module 6: Security

Security is a shared responsibility!

Customer responsible for:
- Configuring security groups on amazon ec2 instances
- Patching software on amazon EC2 instances
- Permissions for Amazon S3 

### IAM
User permissions created. Can also be created on DB side or SSO.

Policy is a collection of permissions

IAM role is an identity that you can assume to gain temp access

Multi-factor authentication: provides extra layer of protection for AWS accounts

### AWS Organizations
- create hierarchy of roles and service control policies to control number of roles that can be granted. Main accounr called 
root, 
- A collection of accounts is what is organised 
- User, group and role is inside the account,

### AWS Artifact
- Access AWS compliance reports on-demand
- Review, accept and manage agreements with AWS

### Customer compliance center
Information you need to know to check AWS compliance

### AWS waf
- Create rules for firewall

### AWS shield 
- Protection against DDoS attacks in real time

### AWS Inspector
- Allows you to perform security assessment checks

### AWS KMS
- Used for encrypting data at rest (create cryptographic keys)

### Amazon GuardDuty
- Intelligent threat detection for AWS products and services

## Module 7: Monitoring and Analytics

### AWS CloudTrail event
- Keeps metrics of application in single dashboard
- Monitor your resource usages

### AWS Trusted Advisor
Inspects AWS config and gives real time recommendations based on best practices.
- Uses dashboard to inform: Performance, cost optimization, security, fault tolerance, service limit
- Checking for open access permissions

## Module 8: Pricing and Support

PAYG model, pricing different for each region

Pay less when you reserve and when you bulk buy

Pricing model for serverless different: pay for what you are using

Consolidated billing - combine usage across accounts to receive volume pricing discounts

Cost explorer - Visualise graphs of expenditure

AWS Budget - receive alerts when there service usage exceeds user defined limits

AWS TAM - only for enterprise, offers point of contact support

## Module 9: Migration and Innovation

Cloud adoption framework: gives advice on migration. Based on 6 perspectives:
- Business
  1. Business
     1. Ensures IT aligns with business needs
  2. People
     1. Supports dev of org whilst change management strategy for cloud migration
  3. Governance
     1. similar as above
- Technical
  1. Platform 
     1. Patterns to implement cloud practices
  2. Security
     1. Ensure org meets security objectives
  3. Operations

### Migrating strategies
6 strategies
- Rehost: Move app from on premise to eC2
- Replatform: Tinker then move (shift notification service to SNS)
- Refactor/Rearchitect: As name suggests
- Repurchase: Change licensing/pricing to move to cloud
- Retain: Do not migrate
- Retire: Tear down application (not used)

For migration, AWS can ship storage to help with the data process

**AWS Snow Family**
- AWS Snowcone:
  - small rugged, secure edge computing and data transfer
  - 8TB
- AWS Snowball devices:
  - Edge storage optimized, Edge Compute optimized
  - 80 TB
- AWS Snowmobile:
  - For crazy large amounts of data (a whole truck!)
  - 100 PB

Serverless migration takes less time

### AWS Well-Architected Framework Pillars
- Cost optimization
- Operational excellence
- Performance efficiency
- Reliability

## Module 10: AWS Certified Cloud Practitioner Basics
[Exam prep](https://aws.amazon.com/certification/certification-prep/)
[Free webinars and learning](https://pages.awscloud.com/traincert_alwayslearning_virtualevents.html)
[Practice Labs](https://wellarchitectedlabs.com/)
[Cloud practitioner AWS prep](https://aws.amazon.com/certification/certified-cloud-practitioner/)

Domains covered
- Cloud Concepts
- Security and Compliance
- Technology 
- Billing and Pricing

Logistics
- 90 min exam
- Multi choice 
- No negative marking 
- Flag question for review 
- Unanswered questions are scored as incorrect

Strategies
- Read full question
- Predict answer before looking at options
- Don't skip questions
- Max mark 1000, pass 700


## Misc
IAM Role : Permissions, getting access key to allow code to speak to other AWS services.

### EC2 configuration setup:
Linux - bash script
Windows - Powershell
Can run script on first spin up of the server
(put software needed to run on server in this script)

Can not add ephemeral storage, given based on EC2 instance

Can connect to EC2 using pem or SSH command


[Protect sensitive data](https://aws.amazon.com/blogs/big-data/create-a-secure-data-lake-by-masking-encrypting-data-and-enabling-fine-grained-access-with-aws-lake-formation/)
[Data lakes](https://aws.amazon.com/blogs/big-data/create-a-secure-data-lake-by-masking-encrypting-data-and-enabling-fine-grained-access-with-aws-lake-formation/)