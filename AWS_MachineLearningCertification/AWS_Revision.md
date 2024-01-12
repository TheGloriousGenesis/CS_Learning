[//]: # (Clean up is always important [here]&#40;https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-ex-cleanup.html&#41;)

# AWS Revision

## What does the exam entail?
- Unanswered questions are scored as incorrect; there is no penalty for guessing. 
- 50 questions in exam that affect score
- You need 750/1000 to pass
- Includes 15 unscored questions that do not affect your score

> [!CAUTION]
> Practice feature engineering

Exam is split into 4 domains
  - Data engineering - 20%
  - Exploratory Data Analysis - 24%
  - Modelling - 36%
  - Machine Learning Implementation and Operations - 20%

## Domain 1: Data Engineering - Architecting

### Create data repositories for ML

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

### Identify and implement a data ingestion solution - Ingestion/Collection.
- Identify data job styles and job types 
  - batch load
  - streaming
  - hyperparameter
  - training
  - etc
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

### Identify and implement a data transformation solution - ETL, processing

- Handle ML-specific data by using MapReduce.
- Transform data in transit

Analytics:
- Amazon EMR ([Apache Hadoop](https://aws.amazon.com/emr/features/hadoop/), [Apache Spark](https://aws.amazon.com/emr/features/spark/), [Apache Hive](https://aws.amazon.com/emr/features/hive/))
- AWS Glue

Compute:
- AWS Batch

## Domain 2: Exploratory Data Analysis

### Sanitize and prepare data for modeling

- Identify and handle missing data, corrupt data, and stop words.
  - Can be handled by common [preprocessing steps](../Machine_Learning/Data_Mining/README.md#preprocessing)
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

- Create graphs (for example, scatter plots, time series, histograms, box
plots).
- Interpret descriptive statistics (for example, correlation, summary statistics,
p-value).
- Perform cluster analysis (for example, hierarchical, diagnosis, elbow plot,
cluster size).

> ADD list of analysis techniques and the best time to use them for

### Domain 3: Modeling 

#### Frame business problems as ML problems - Problem formulation

- Identify when to use and when not to use ML.
  - ML has the power to:
    - Leverage large amount of data 
    - Analyzed data for patterns that are too complicated to decipher individually
    - Scale predictions
    - Be utilised in a non-deterministic way
- Know the difference between ml types [definition of machine learning types](../Machine_Learning/README.md#Glossary)
  - supervised
  - unsupervised learning
  - deep learning
  - reinforcement
- Select from among classification, regression, forecasting, clustering, and
recommendation models
- Justify model selection 

#### Select the appropriate model(s) for a given ML problem 

- XGBoost, logistic regression, k-means, linear regression, decision trees,
random forests, RNN, CNN, ensemble, transfer learning
- Express the intuition/understanding behind basic ML algorithms.

> ADD list of other types of ml models

#### Train ML models
- Parameters for model set in training job (weight and bias). Hyperparameter set before and outside of job

- Split data between training and validation (for example, cross validation).
  - Splitting data only applicable to supervised learning 
  - Purpose of each part of data slice is mentioned [here](../Machine_Learning/README.md#Glossary)
  - 70-80% Training 
  - 10-15% Evaluation (Pass to algo at time at training)
  - 10-15% Testing (Accuracy, precision, Recall, performance metrics) (Not passed to algorithm)
  - dataset should be greater than 1000 

- Understand optimization techniques for ML training (for example, gradient
descent, loss functions, convergence).
  - [gradient descent](../Machine_Learning/MLTheory/README.md#gradient-descent)
- Choose appropriate compute resources (for example GPU or CPU,
distributed or non-distributed).
  - Choose appropriate compute platforms (Spark or non-Spark).
- Update and retrain models. 
  - Batch or real-time/online
- Creating a job training in AWS Sagemaker:
  - Must specify:
    - S3 bucket for input data
    - S3 bucket for output data
    - Compute resources for training
    - Code in Amazon Elastic Container Registry path

> ADD different types of splitting dataset methods
> ADD different optimization techniques
> ADD Different types of compute resources/platform for problem
> ADD inf- on how to update and retrain models and aws services that can be used to d- so
> ADD Model training best practices

> Amazon SageMaker workflow for training jobs 
> Running a training job using containers 
> Build your own containers 
> P3 instances (GPU instance)
> Components of an ML training job for deep learning

#### Perform hyperparameter optimization
Hyperparameter tuning is done to increase prediction power via influencing the learning 
process.

- Three types of hyperparameters:
  - Model parameters (to do with model)
  - Optimizer parameters (gradient, stochastic, ADAM)
  - Data parameters (to do with data, usually if there isn't enough)
- Understand the correct type of hyperparameter optimization technique for the right ML problem
  - Manually (with domain knowledge)
  - Grid search  - Not available on Sagemaker (it is [now](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-automatic-model-tuning-now-supports-grid-search/#:~:text=With%20Amazon%20SageMaker%20automatic%20model,%2C%20Grid%20search%2C%20and%20Hyperband.))
    - Inefficient but thorough
  - Random search
  - Bayesian search
  - Hyperband (bandit based approach)

Random search and bayesian methods leave smaller unexplored regions than grid searches

- Perform regularization.
  - Drop out
  - L1/L2
- Perform cross validation.
  - Increases computational load
  - Validation:
    - K-fold 
      - K usually between 2 < K < 10
      - for datasets between 10,000 - 100, 000, use K < 8
      - K value inversely proportional to dataset
    - Stratified K-fold
      - For imbalanced datasets
    - Leave on out (small datasets)
- Initialize models.
- Understand neural network architecture (layers and nodes), learning rate,
and activation functions.
- Understand tree-based models (number of trees, number of levels).
- Understand linear models (learning rate). 


> [!IMPORTANT]
> - Scikit learn API optimization is NOT available on Sagemaker
> - Hyperparameters are set OUTSIDE of training jobs
> - Hyperparameter tuning jobs can be stopped and the underlying resources deleted, but the jobs themselves cannot be deleted.


> [!TIP]
> - Perform hyperparameter tuning for XGBoost (supervised machine learning)

#### Evaluate ML models
- Avoid overfitting or underfitting.
  - Detect and handle bias and variance.
- Evaluate metrics (area under curve [AUC]-receiver operating characteristics
[ROC], accuracy, precision, recall, Root Mean Square Error [RMSE], F1 score).
- Interpret confusion matrices.
- Perform offline and online model evaluation (A/B testing).
- Compare models by using metrics (for example, time to train a model,
quality of model, engineering costs).
- Perform cross validation. 

> ADD more understand

### Domain 4: Machine Learning Implementation and Operations 

#### Build ML solutions for performance, availability, scalability, resiliency, and fault tolerance. 

- Log and monitor AWS environments.
  - Build error monitoring solutions.
- Deploy to multiple AWS Regions and multiple Availability Zones.
- Create AMIs and golden images.
- Create Docker containers.
- Deploy Auto Scaling groups.
- Rightsize resources (for example, instances, Provisioned IOPS, volumes).
- Perform load balancing.
- Follow AWS best practices. 

Management and Governance:
- AWS CloudTrail
- Amazon CloudWatch

Storage:
- Amazon Elastic Block Store (Amazon EBS)

Containers:
- Amazon Elastic Container Registry (Amazon ECR)
- Amazon Elastic Container Service (Amazon ECS)
- Amazon Elastic Kubernetes Service (Amazon EKS)

Compute:
- AWS Batch
- Amazon EC2
- AWS Lambda

Networking and Content Delivery:
- Amazon VPC

> ADD aws best practices
> ADD what is a golden image

#### Recommend and implement the appropriate ML services and features for a given problem.

- ML on AWS (application services)
  - Amazon Polly
  - Amazon Lex
  - Amazon Transcribe
- Understand AWS service quotas.
- Determine when to build custom models and when to use Amazon
  - SageMaker built in algorithms.
    - Linear Learner
    - XGBoost
    - K-Nearest Neighbour 
    - Decision trees
    - Random forest
    - Image classification
    - Object detection
    - Semantic segmentation
    - (NLP) Blazing Text
    - (NLP) Sequence2Sequence
    - (NLP) Object2Vec
  - When to choose training algorithm
    1. Built in sagemaker
    2. Apache spark with Amazon Sagemaker
    3. Submit code to train model via deep learning framework (Tensorflow/ApacheMXNet)
    4. Use custom code and put code together in Docker image
    5. Subscribe to algorithm in Marketplace
- Understand AWS infrastructure (for example, instance types) and cost
considerations.
  - Use Spot Instances to train deep learning models by using AWS
  Batch.


#### Apply basic AWS security practices to ML solutions

- AWS Identity and Access Management (IAM)
- S3 bucket policies
- Security groups
- VPCs
- Encryption and anonymization 

Storage
- Amazon s3

Networking and Content Delivery:
- Amazon VPC

Security, Identity, and Compliance:
- AWS Identity and Access Management (IAM)


#### Deploy and operationalize ML solutions
- Scalable
- Costooptimized 
- Reliable

- Expose endpoints and interact with them.
- Understand ML models.
- Perform A/B testing.
- Retrain pipelines.
- Debug and troubleshoot ML models.
  - Detect and mitigate drops in performance.
  - Monitor performance of the model. 

> ADD Deployment best practices
> ADD Operational best practices
> Add how to identify and fix drops in performance

### Overview - AWS services matching to ML solutions

#### Analytics:
- Amazon Athena
- Amazon EMR
- AWS Glue

- Amazon Kinesis

Amazon Kinesis is a platform for [streaming data](../Machine_Learning/Data_Mining/README.md#overview---data-streaming) in AWS.

- Amazon Kinesis Data Firehose
  - Deals with streaming data to http endpoints and storage solutions (S3/Redshift).
  - Config based (do not need to set up an application, just state where the data is and where you want it to go)

- Amazon Kinesis Data Streams
- Amazon Managed Service for Apache Flink (Amazon MSK)
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

Database:
- Amazon Redshift - [Data warehouse](../Machine_Learning/Data_Mining/README.md#data-warehouse)

Analyses data using SQL in real time for AI/ML applications. Allows ingesting of data across different storage solutions in an easy way.
  - Parallel processing architecture
  - Using no ETL (users use their own ETL tools)
  - Serverless
  - High [concurrency](../Core_Java_and_Optimisation_techniques/README.md#concurrency)
  
As it uses SQL to analyse data, data must be structured or semi-structured
> [!CAUTION]
> I still do not know what concurrency is. I need a visual. MAKE ONE.

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

Storage:
- Amazon Elastic Block Store (Amazon EBS)
- Amazon Elastic File System (Amazon EFS)
- Amazon FSx
- Amazon S3 
__________________


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
