# AWS Cloud Practitioner

Break time - 7h30am 

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
- Security - Each service has security specific features as well as there being security services as well
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


Elasticity
Load balancer

## Module 3: Global Infrastructure and Reliability

## Module 4: Networking

## Module 5: Storage and Databases

## Module 6: Security

## Module 7: Monitoring and Analytics

## Module 8: Pricing and Support

## Module 9: Migration and Innovation

## Module 10: AWS Certified Cloud Practitioner Basics