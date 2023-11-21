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


Slide 21
- Supervised falls into: Binary, multi-class, regression

Slide 24
- Unsupervised falls into :
- Spot outliers or indicator anomalies


Slide 32
- Deep learning is also divided into supervised and unsupervised
- CNN/ANN

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

Slide 9
- Regression problems linked to numeric outputs

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

Slide 8-9
Collect/find data from anywhere (data lakes, database, etc). Permissions and entitlements required to obtained here.

Data Lake has centralised location to store structured, unstructured and semi structure data.

Data is cataloged (metadata: where it is stored, serialised deserialize).

Data swamp (uncataloged)


Slide 10
S3 acts as storage for data lake

Create catalog in glue and lake foundation in data lake

You can row level/ column level permission in data lake if you want to restrict info from being retrieved

Slide 11
data and algo downloaded onto ec2 instance (which is created by amazon sagemaker when trianing job is created)

container image (ECR) contains algorithm/ model

when trained the model is uploaded as artifact in `tar.gz` to s3 again or to amazon elastic file system

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

Slide 

