Exam
- Unanswered questions are scored as incorrect; there is no penalty for guessing. 
- 50 questions in exam that affect score
- You need 750/1000 to pass
- Includes 15 unscored questions that do not affect your score


Exam is split into 4 domains
  - Data engineering - 20%
  - Exploratory Data Analysis - 24%
  - Modelling - 36%
  - Machine Learning Implementation and Operations - 20%

### Domain 1: Data Engineering - Architecting

#### Create data repositories for ML

- Identify data sources (for example, content and location, primary sources
such as user data).
- Determine storage mediums

Storage:
- Amazon Elastic Block Store (Amazon EBS)
- Amazon Elastic File System (Amazon EFS)
- Amazon FSx
- Amazon S3

Database:
- Amazon Redshift

> MAYBE: General database stuff

#### Identify and implement a data ingestion solution - Ingestion/Collection.
- Identify data job styles and job types (for example, batch load, streaming).
- Orchestrate data ingestion pipelines (batch-based ML workloads and
streaming-based ML workloads).
- Schedule jobs. 

Analytics:
- Amazon Athena
- Amazon EMR
- AWS Glue
- Amazon Kinesis
- Amazon Kinesis Data Firehose
- Amazon Kinesis Data Streams
- Amazon Managed Service for Apache Flink
- Amazon QuickSight


#### Identify and implement a data transformation solution - ETL, processing

- Handle ML-specific data by using MapReduce.
- Transform data in transit

Analytics:
- Amazon EMR ([Apache Hadoop](https://aws.amazon.com/emr/features/hadoop/), [Apache Spark](https://aws.amazon.com/emr/features/spark/), [Apache Hive](https://aws.amazon.com/emr/features/hive/))
- AWS Glue

Compute:
- AWS Batch

### Domain 2: Exploratory Data Analysis

#### Sanitize and prepare data for modeling

- Identify and handle missing data, corrupt data, and stop words.
- Format, normalize, augment, and scale data.
- Determine whether there is sufficient labeled data. 
  - Identify mitigation strategies. 
  - Use data labelling tools. 

Machine Learning:
- Amazon Mechanical Turk
- Amazon SageMaker Ground Truth

#### Perform feature engineering

- Identify and extract features from datasets, including from data sources
such as text, speech, image, public datasets.
- Analyze and evaluate feature engineering concepts (for example, binning,
tokenization, outliers, synthetic features, one-hot encoding, reducing
dimensionality of data). 

> ADD list of feature engineering concepts and links to places within the repo

#### Analyze and visualize data for ML


Build
- Data analysis/visualization
- Model training
- Model deployment/inference

Deploy

Optimize
- Perform basic hyperparameter optimization 
  - Understand the correct type of hyperparameter optimization technique for the right ML problem

Train

Tune

Maintain ML using Cloud
- Scalable
- Cost-optimized 
- Reliable
- (Security) Secure ML
- Operationalizing ML

Problem formulation (Identification and justification)
- ML types (including deep learning)
  - Understanding the intuition behind basic ML algorithms

AWS services matching to ML solutions
Analytics:
- Amazon Athena
- Amazon EMR
- AWS Glue
- Amazon Kinesis
- Amazon Kinesis Data Firehose
- Amazon Kinesis Data Streams
- Amazon Managed Service for Apache Flink
- Amazon QuickSight
Compute:
- AWS Batch
- Amazon EC2
- AWS Lambda
Containers:
- Amazon Elastic Container Registry (Amazon ECR)
- Amazon Elastic Container Service (Amazon ECS)
- Amazon Elastic Kubernetes Service (Amazon EKS)
- AWS Fargate


Internet of Things:
- AWS IoT Greengrass 
Machine Learning:
- Amazon Comprehend
- AWS Deep Learning AMIs (DLAMI)
- AWS DeepLens
- Amazon Forecast
- Amazon Fraud Detector
- Amazon Lex
- Amazon Mechanical Turk
- Amazon Polly
- Amazon Rekognition
- Amazon SageMaker
- Amazon Textract
- Amazon Transcribe
- Amazon Translate
Management and Governance:
- AWS CloudTrail
- Amazon CloudWatch
Networking and Content Delivery:
- Amazon VPC
Security, Identity, and Compliance:
- AWS Identity and Access Management (IAM)


ML and deep learning frameworks

Model training best practices

Deployment best practices

Operational best practices

____
Out of scope:

Extensive or complex algorithm development
- Extensive hyperparameter optimization
- Complex mathematical proofs and computations
- Advanced networking and network design
- Advanced database, security, and DevOps concepts
- DevOps-related tasks for Amazon EMR
- AWS Data Pipeline
- AWS DeepRacer
- Amazon Machine Learning (Amazon ML)
