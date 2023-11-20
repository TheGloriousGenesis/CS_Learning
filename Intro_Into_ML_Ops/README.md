# Intro into ML Ops practitioners

## Understanding ML Process
1. Data Preparation (Data engineering)
   1. Preparing the data to use from raw data to production ready data
2. EDA (Exploratory Data Analysis)
   1. Explore for any statistical patterns in the data, talk to stakeholders whilst you do this
   2. Best way to do this:
      1. Explore your target variable
      2. See how other columns of the data effect target variable through plots
         1. Understand the reason behind what is being showed and see if you can explain further with more analysis
3. Feature engineering
   1. Leverage domain knowledge to boost machine learning model performance.
   2. Clean and transform data to engineer features from data. 
      1. Split into training, testing and validation sets
4. Model Training
   1. Data scientists explore multiple algorithms and hyperparameter configuration. 
   2. Best performance model is chosen against predefined evaluation metrics.
5. Model Validation
   1. Ensure the model exceeds predefine minimum level of performance, business requirements, regulatory requirements before deployment.
6. Deployment
   1. ML engineer deploy model via 
      1. Batch
      2. Streaming
      3. Online serving
   Whatever the usecase requires
7. Monitoring
   1. Model


Data surrounding data pipelines
Workflow built on certain tools

Data stores?
Feature stores?
Model stores?
Evaluation stores?

AI is successful but comes with lots of risks. These risks are within the following environments:
MLOps refers to patterns and practices and technology to industrialize AI at scale. Treatment of ML as software.
Establishes key engineering patterns & practices across the full ML lifecycle

1. Regulatory
   1. Strict audit & privacy requirements
   2. Corporate fines
2. Reputation
   1. Explainability
   2. Fairness
3. Financial
   1. Limited return on investment
   2. Unstable model performance
4. Deployment
   1. Models fail in production (model degradation)

## ML Lifecycle (and tools)
- Data management
  - SnorkeJ (Automated data labelling solution)
- Development
  - mlflow (Model management solution)
- Deployment
  - mlflow (Model deployment)
- LiveOps
  - Prometheus & Grafana

Must enable the following to be more effective:
- Provisioning of environment tooling
- Governance
- Assertization


## How to 
