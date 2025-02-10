Learn Machine learning pipeline E2E with amazon sagemaker. Super-charged jupyter notebook.

Do not take notes! Just note down questions about slides!

# Glossary

|     Name     |                                               Definition                                               |
|:------------:|:------------------------------------------------------------------------------------------------------:|
|    Model     |                                           Trained algorithm                                            |
|   Feature    |                                     Columns / attributes in table                                      |
|    Weight    | The importance we are giving to a feature, how much does feature affect the accuracy of the prediction |
|  Data Lake   |         A data lake is a repository that stores, processes, and secures large amounts of data          |
|  Supervised  |                       Identify patterns in data that have already been labelled                        |
| Unsupervised |                                   Machine uncovers labels by itself                                    |

# Course info

Puneet Sharma - Person to go to help with lab session

Timing:

Tea break: 2-2h25pm - 8:30-9:00
lunch break: 4-5pm - 10:30-11:30
short break? 6h30-6h45pm - 13:00-13:15

# Exam

- select ml approach
- identify if ml needed
- fine tune model

# Training

Flight delay - binary outcome is flight delayed

Fraud detection - detect fraud

# Module 1

Slide 4
- Easy compute and cloud capacity/resources has allowed each person to access ML
- ML thought to be pattern recognition.
  - ML also about deployment, monitoring, scalability
  
Slide 5
- change from manual rules to having the model create the rules from the data through algorithms
- 2022 150ZB data created 70% unstructured.
- For decision-making, you usually need structured data

Slide 10
- Features are columns / attributes in table
- weight is the importance we are giving to a feature
- How to assign weights to feature
  - Manual: With domain expertise info 
  - Statistically: scatter, correlation matrix etc
  
Silde 14
- Set threshold for recommendation problem (if more than x, recommend).

Slide 36
- Difference between ml and dl is features are created the machine (not manually or statistically)

Slide 41
- Uses ANN
- Can be trained on raw features

___

# Module 2 - Intro into Sagemaker

ML instances power jupyter notebooks which underpin sagemaker

Sagemaker is fully-managed service used to build, train and deploy ML models at any scale

- Capable of deployment scaling
- Distributed training
- Incremental training
- A|B testing 

Slide 6
- SageMaker can do everything apart from business and problem formulation

Can provide code for training algo in sagemaker builtin algos, the dependancies 
- Define estimator is used for training purposes (for model training and hosting)
  - execute `.fit()` to train
  - deploy model using `.deploy()`

> [!NOTE] 
> Instance that notebook is running is different from instance that training is happening.
> Hosting (inferences) is happening on separate server. Billing is seperate for each of this. For dev /POC you can put everything on same instance

Slide 9 
Instance types

Slide 10
Ground Truth - Only used for supervised learning
- Useful for completing incomplete data and adding labels to data where it can (mixture of automatic labelling and human labelers)

Slide 13
Inference
- Deploy online - always available any time (up all the time), generate one prediction at a time on demand
- Deploy batch - Only on demand (needed at this time for this long), generate a batch of predictions all at once (e.g imagine)

- If payload contains audio/images (use GPUs) if not (use CPUs)
- Elastic inference instead of GPU (fraction of GPU) attached to CPUs

## Sagemaker in action

### Prepare Sagemaker environment
To create your own notebook:
- Provide role `SagemakerAdmin`

Specify storage bucket (S3) and prefix the bucket for different versions of data. So you should have different prefix for model data, training, etc testing. Create IAM role for access to your buckets!

> [!IMPORTANT] 
> The S3 bucket used throughout the whole ML development should all be in the same region: Notebook instance, Training, Hosting

### Import data 

Either download data, connect to database or use local files

> [!TIP] 
> use `wget` to download files from links

### Exploration

Create initial hypothesis and analysis on dataset. 

Common analysis tools:
- `.describe()` - (use `include=object` in args to include categorical data)
- `pd.crosstab` - frequency count, convert categorical features to indicator values
- Histogram - View spread of data roughly
- Feature correlation metrics

- When you are deploying a model. 
  - Data in your notebook instance needs to first be converted into CSV string (because data is stored via CSV) by Serializer that encodes and decodes HTTP POST request /response
  - If using CSV format, Sagemaker XGBoost requires that data does not include the target variable
- You can use `Amazon CloudWatch` to analyse logs from model
- Always delete instance when you finish the notebook `sagemaker.Session().delete_endpoint(<endpoint_name>)`

### Preprocess

Sagemaker notebook instances can be used for preprocessing data. That is locally removing and getting the data to a good level before training and feature engineering

### Analyse

- Confusion matrix : Only for supervised learning

# Module 3 - Business problem / Problem formulation

Slide 8

- Specify business problem
- Specify goal
- Specify success metric (**quantify** the goal, have thresholds) <-- Defined by project/business managers product owners


Slide 12
- You can have multiple and different types of machine learning solutions in the same business problem

Slide 14
- Is my data collected over realtime, format, polarisation (bias in classes)
- parqet text format accepted (text based)

Slide 15
- You need a domain expert to know feature importance, and understand the landscape and the data that we need for the model (what is relevant)

Slide 16
- Evaluate quality of data

Slide 17
- Identity target (already known - have labelled column)
- Use data to see what algorithm to pick (supervised or unsupervised based on if target column available)

Slide 19
- If we dont have labels we need to create labels
  - 100 < x < 200 : can manually do this yourself
  - 10 million > : more of an issue!
    - Use Amazon sagemaker ground truth!

Slide 20
- Ground truth description on working
- Helped by Amazon mechanical turk

Slide 21
Type of workforce
- Use crowdsource for no confidential data
- For confidential data, create internal workforce
- Expertise labelling can be provided through third party vendors

> [!NOTE] 
> With GroundTruth, you can load images from S3 (No other resource location, must be S3!) and create task for autolabelling. You can also manually label with manifest file (somehow)


Slide 27 - 31
- Defining success

> [!NOTE] 
> When formulating a problem you must state why ml is appropriate (e.g to do with scale, complexity etc)

# Module 3 - Data Processing

Try: Explore the problem (in this case, explore your data)
Broken?: What is broken? (Do you see something wrong in your data)
Learn: Why is it wrong? (What is wrong with this data? How can you solve it?)
Fix: Fix the problem (What can I do to bring the wrong data to an acceptable solution?)

Slide 8-9
Collect/find data from anywhere (data lakes, database, etc). Permissions and entitlements required to obtained here.

Data Lake has centralised location to store structured, unstructured and semi structure data.

Data is cataloged (metadata: where it is stored, serialised deserialize).

Data swamp (uncataloged)


Slide 10
S3 acts as storage for data lake

Create catalog in AWS glue and lake foundation in data lake

You can row level/ column level permission in data lake if you want to restrict info from being retrieved

Slide 11
data and algo downloaded onto ec2 instance (which is created by amazon sagemaker when trianing job is created)

container image (ECR) contains algorithm/ model

when trained the model is trained it is uploaded as artifact in `tar.gz` to s3 again or to amazon elastic file system

EFS volume good for consistent retraining and reduce latency


Slide 13
Amazon FSx Lustre speeds up training jobs

Slide 14
Training data load times (training time of 1hr or less : EFS/FSx)

compute intensive : FSx 
dynmaically retrain : FSx
nerual networks: FSx
text: EFS

Slide 17-22

Slide 23
Scikit-learn good for using open source version of these algorithms

Slide 24
Numpy

Slide 25
Scikit learn

Slide 26
Matplotlib

Slide 27
Seaborn - more sophisticated visuals + 3d visuals

Slide 30 - 34
Examples of dirty data

# Module 4B - Data preprocessing: descriptive statistics
Descriptive statistics - used to create data quality report
- in pandas using `df.describe(include='all')`


Slide 7 
mean == median : symmetrical distribution
mean =/= median : skewed distribution

features should be normally distributed as much as possible



Slide 15
check missing values for column/row

2-5 % missing : delete row!

5% > missing : replace via medium/mode other means

standard derivation should be mean +- 2-3%

Slide 16
Find why missing values are missing

What is the underlying pattern for missing data

Are there things missing that I am not aware of

Slide 17
drop missing values
- don't drop column! (axis=1) unless i know its not useful or highly correlated to another feature

Slide 18
Dropping missing values risk (rows - overfitting) (columns - underfitting)

## Data Visualisation

Slide 23
Use bar charts to visualise categorical data

Slide 26 - 27
Use histograms to visualise numerical data (reasons why)

Slide 28
ALL can be used for outliers  and all for numerical features

Histogram: 

Density plot : type of histogram (smoother version)

Boxplot : visualising outliers, peaks

`df.V11.plot...`

Slide 29
Multi-variate relations
- Scatter matrix plot, correlation, contingency tables

Slide 31
Scatterplot matrix ignore the diagonals do not make sense so ignore  it (feature correlation with itself is always ignored)



Slide 33
Features who have strong correlation with target variable you KEEP

Features who have strong correlation with other features you DROP


## Data Wrangler

Used for cleaning purposes in GUI
- Create flow
  - Import data from many sources (mentioned)
  - You can create reports in the wrangler to determine quality of data
    - High anomaly score is good. low is bad
  - Can add transformations here as a flow


# Data processing Lab
```python
df.isnull().sum() / df.shape[0] # <-- if the percentage less than 5 you can drop
```

# Module 5: Model Training

Slide 7
If its supervised? go with XGBoost / Linear learner as first choice. 

During training can use multiple algorithms

Factorization machines is good for recommendation

Ranking order and SEO cases we use KNN 


Slide 8
When to use unsupervised learning

Object2Vec - text to data etc, 

Slide 9
what to use for text analyis

Slide 10 
What to use for image/video and time series

Slide 12

Use `.rec` and use in pipe modes 

two modes to provide data from s3 to model: file mode and pipe mode

file mode : all data from s3 into ec2 instance

pipe mode : stream data from s3 to ec2 instance (requires less storage capacity onto ec2 instance, less training time)

Slide 13
First column must be target if using inbuilt algorithms

Always convert csv --> rec as sagemaker has inbuilt helper functions to aid this


> Read FAQs for services (Sagemaker)
> 30% machine learning, 60% amazon, 5% miscellous (IAM)
> Passing 48-50/65 correct to clear 
> Skillbuilder sample exams

## Testing and validation

Slide 24
Data in specific order can lead to bias

Slide 26
K size and bias relationship equation

Slide 27
K fold with shuffling - randomize order of the data

Slide 29
Stratified K-fold

Slide 30
Scikit learn randomizes data before training in `train_test_split`

Slide 35
Iterate K-fold is better than normal K fold

## Model training
Slide 37
Model learns how to predict labels via minimising computed loss during learning (difference between predicted and actual)

Slide 40
Loss function : Objective function. Measure of error in model with given weights

Slide 41
RSME 

Slide 44
Optimization seeks to minimize loss function to minimise error

Gradient descent to try and find the minima of the obj function 

Slide 53
Draw backs of gradient descent

Slide 54
Stochastic descent : Every datapoint (every row) . When trying to move to global minima it become very erratic
takes mean error not squared
Curse of local minima

Slide 56
Gradient descent variations
- Gradient descent
- Stochastic gradient descent
- Mini batch gradient descent

Slide 59

Boto for communicating to s3
Python sdk for sagemaker API

Slide 62
24 built in algos, custom script


Slide 65
Difference between parameters and hyperparameters
- Each model has its own parameters to get it going

Slide 67 
inside training job

> [!NOTE]
> All algorithms hosted are on ECR containers (docker resgistry images) and they are different region to region

> [!NOTE]
> Inference images usually lightweight compared to training


# Module 6 : Model Evaluation
Slide 9
Uses test data to evaluate model

Slide 11
Defined Variance, Bias

High variance, Low bias : Overfitting

low variance, high bias:  Underfitting (model gives one likely area of output but it's not related to correct output)

High variance, high bias: Bad! add features, feature engineering, PCA, everything and retrain model

Slide 12
Bias vs variance graphs

Slide 13
Classical and regression metrics evaluation

Slide 27
AUC/ROC curve

Slide 28
High AOC == good performance


Slide 30


Slide 31
R^2 (Coefficient of determination) always between 0 and 1, better if closer to 1. will increase if more features added

Slide 32
Adjusted R^2 : to combat increasing R when more features are added. It only increases 
if the new variable has impact on the target variable

Slide 33
Highest R^2 not necessarily best model (can be sign of overfitting)

# Module 7: Feature Engineering

Slide 5 
Extract more information from your feature to help your model learn fast. Different types of features: Categorical and continuous (qualitative , quantitative)

Slide 7:
Components of feature engineering

Slide 8:
[Curse of dimensionality](../Machine_Learning/MLTheory/README.md#overview---feature-engineering)

Slide 9:
Feature selection a part of feature engineering - decrease features

Slide 15:
(eliminating irrelevant data - think about data as vectors, vectors that can be made out of other vectors can just be removed) - decrease features

Slide 16:
Feature creation and transformation increases number of features

Slide 18:
How to handle numerical data: (to reduce impact of extremities )

Slide 19
- Logarithmic transformation

Used when you want to remove right skew

Can not apply to 0 or negative values

Changes shape of feature

Used to reduce extreme polarity 

Slide  20
- Square root and Cube root 

High variance? apply

Cube root can be applied to 0 values (apply to cubed metrics)

Slide 21
- Binning

Slide 22 -25
- Scaling

Used when change intra one feature,

transformation techniques (Slide 25)

Slide 26
Pros of Mean-variance standardization 

Slide 27
MinMax Scaling

Slide 29
MaxAbs Scaling (Not recommeneded)

Silde 31
Robust Scaling

Slide 32
Categorical data needs to be converted into numerical data for the algo

Interval scaling
Ordinal scaling 
Nominal scaling

One-hot encoder

Slide 35
Note all categorical data should be converted into ordinal ranking 1,2,3 (model could learn weird behaviour if named like this)

Slide 36
Use one-hot encoding for nominal variables

pandas `get_dummies`


Slide 37 
One-hot encoding if there are too many columns that will be made

Group columns (logical) (thinking binning and then)


Slide 45


---



Slide 51
Sagemaker has hyperparameter tuning job

> [!IMPORTANT]
> Tunning doesn't always improve model!

Slide 53
Tuning best practices


# Module 8: Deployment

Slide 11
Production infrastructure

Slide 13
Unmanaged ML
- operating system manual deployments
- Deploy on EC2 instance by creating AMI

Slide 14 - 16
Deploy on Sagemaker

Slide 17
All traffic to one model : Standard traffic

Slide 19
Deploy model with minimum downtime - Canary API Gateway

Slide 21
Blue - green two production environments

User send to blue env (testing area)
some traffic goes to green 
delete blue

every 10 minutes increase traffic to green

A/B testing done with synthetic data but both this and canary similar elsewhere 

Slide 32
Initialvariantweight for each model is x / sum of all of them  (but you physically)

Slide 35
Types of inferences sagemaker supports

Asynchronous
- Maximum payload size of 1 GB 
- 30 sec - 2 mins of latency
- No server always running (serverless - created in max 30sec, around 10-15 secs)

Serverless
- Don't know traffic pattern
- Payload size KB
- Cold start  (serverless - created in max 30sec, around 10-15 secs)

Real Time

Slide 36
When to use batch transform

Slide 45
Inference vs Training

Slide 46
AWS AutoScaling

Slide 48
When to use GPU

Slide 47
Sagemaker instance types

Slide 52 - 53
Sagemaker inference pipelines

Slide 55
What to monitor in a model that has been deployed

Monitor model and monitor infrastrure

Check accuracy of model and check CPU, memory utilisation, number HTTPS requests

Infrastruture monitoring : Cloudwatch

Slide 57
Monitor API trail in AWS Cloudtrail (auditing)

Slide 58
Concept drift - performance declines over times in production (usually not more than 3 months models remain in tack)

Slide 59
Determines how often you should retrain

Configure cron job and retrigger remodel in Event page

Slide 61
Model Monitor / Sagemaker clarity for model monitor

Slide 63
ML on the edge (IoT use cases)

Slide 64
AWS IoT greengrass
Train in sagemaker (cloud) abd deploy on IOT device

>[!NOTE]
> Kinesis Data Analytics : data stream analysis serverless equivalent to spark streaming. Kafka

# Exam Readiness - AWS Certified Machine Learning Specialty

## Module 1 - Exam and test strategies
Slide 6
With at least one year of experience 

Slide 14
1: Identify type of ml problem
2. Identify appropriate aws service
   1. Know about supplementary services like (Know about their types, availability, rough storage capacicities)
      1. Kinesis family (data stream, firehose, analytics), 
      2. EMR, S3, EC2, EFS,FSX, 
      3. lambda, 
      4. AWS Data Pipeline, 
      5. Glue, 
      6. Data Lake
      7. Mechanical turk, Groundtruth
      8. DeepAR
      9. Amazon Textract
      10. Amazon Comprehend
   
3. Cost optimized solution (select appropriate storage etc) READ UP ON CLOUD FOUNDATION (GLACIER)

Slide 15
How exam questions are split

Slide 17
Exam logistics

Slide 27
Specialty apply knowledge (most correct - even if it feels incorrect, pick the best)

minimal management - serverless

Slide 35
What you won't be tested on (GenAI, pricing + performance metrics)

Slide 41
Exam strategies 


## Module 2: Data Engineering

Slide 47-48
What kind of services used to create data lake

Slide 49
You should know about the accessibility of each type of storage

IMAGE: S3 storage to reduce cost

- Store 
  - Standard : 1TB : $25

Slide 50
- Take model .tar.gz and create endpoint from it 
- s3 - sagemaker over internet (if you dont want to traverse over internet, use interface endpoint e.g secure data). data stays on AWS optic fibres

Slide 51
- Same storage mounted on 3 instances (no internet )

Slide 52
- mounted launch training without (no internet )

Slide 53
- Take into account load times of storage options

Slide 54
Storage options to know about

Slide 56
To use data for ML you need to ingest it into a service like S3

Slide 58
Batch processing raw (use Glue)

Slide 59
Stream processing (use Kinesis)

Slide 61
Kinesis family what is used in which usecase

Flink SQL can also be used

Slide 62
Know about Kafka what is used in which usecase

Slide 64

Data processing process

Slide 66

How to do batch processing using AWS - EMR

Apache Spark on EMS process large amount of data

EMR is Hadoop on AWS

Slide 67

Example for Glue / EMR 

Slide 68

Ad hoc sql query - Amazon athena (redshift spectrum)

Glue stores metadata catalog

Data has to be in specific format for Amazon athena (structured data) e.g csv, tsv, json, parquet, avro, tbl format

Slide 69

Services to learn in this subdomain 

## Module 2 - Explorartory Data Analysis
Slide 87

Know about basic statistics 

Slide 89

Types of attributes to understand shapes

Slide 90

Categorical stats identify frequency of values and class imbalances

Slide 91

Multivate stats - correlation, contingency tables, scattermatrix plot

Slide 96

Standardize language and grammar

Slide 97

Data on same scale

Slide 98

One feature in one column

Slide 99

Outlier

Slide 100

Dealing with missing values

- MICE (multivariate using chain equations)

Slide 101

Things to know in this sub domain


## Module 3: Feature engineering

Slide 105

Reduce number of features in dataset : PCA, T-DISTRIBUTED STOCHASTIC NEIGHBOR EMBEDDING

Slide 112

Don't encode nominal variables as numerical values

Slide 116

Common scaling techniques

Slide 117

Things to know in this sub domain

## Module 3: Visualisation

Slide 119

Helps understand features and relationships

Slide 123

Things to know in this subdomain


## Module 4 - Modelling

Slide 166

Choosing a training algorithm

Slide 167

Things to know in this subdomain

Slide 174

Learn about leave one out (small dataset - leaving one row out, rest for validation)

Slide 175

Create training job 

Take data -> ecr repo (training code) -> train model with container

Slide 176

Things to know in this subdomain

P3- image video


## Hyperparameter tunning

Slide 179
Hyperparmeters tuned before training

Slide 180
Different types of hyperparameters

Slide 184

Things to know in this subdomain

## Validation

Slide 188

Classification problems: confusion matrix (think accuracy, F1 etc)

Slide 194 - 197

Accuracy

Precisin

Recall / Sensitivity

1 - sensitivty = specitivity

Slide 198

Things to know in this subdomain

## Module 4 : ML implementation and operations

Slide 217

Amazon sqs good for loose coupling system to store images to get messages

Slide 218

Amazon Cloudwatch - monitor

Slide 220

Amazon CloudTrail - audit

Slide 227

Things to know in this subdomain


How to debug a ML problem



## Amazon Mechanical Turk

> Description: On demand human workforce service when human >> computer. 

### Usage
- When you need human in the loop
  - Identifying objects in photos
  - Crafting reviews for restaurants, movies, businesses.
  - Translating text into foreign languages
  - obtaining business center hours within in a hotel, etc

### Pros
- Manages the retrieval and compilation of work performed for the Requester
- Requester can add tests to ensure correct worker is chosen