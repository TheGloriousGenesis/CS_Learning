# Machine Learning

## Glossary

|                     Word                      |                                                                      Definition                                                                   |                                                                                                                                                       Example                                                                                                                                                        |
|:---------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                Generalisation                 |                                             The ability for the model to adapt itself to new unseen data                                          |
|            Recommendation Systems             |                                                 Predict what the user might enjoy watching or buying                                              |
| Association rule learning (Affinity Analysis) |                                        Unsupervised learning technique that only works with categorical data                                      |
|          Support (Affinity Analysis)          |                                                    The frequency of the pattern given by the rule                                                 |
|        Confidence (Affinity Analysis)         |                        The strength of an association rule relating to the likelihood of customer buying item A, given item B                     |
|           Lift (Affinity Analysis)            |                        The interestingness of a rule by checking the strength of rule over random co-occurrence if two items                      |
|                 Cost function                 |                                                        How best to best fit function to data                                                      |
|                  Overfitting                  |            When the model fits to the training data better than the testing data. When the cost funciton ~ 0 but can't fit new data well          |
|                  Supervised                   |                                                    Trends based on current data (labels provided)                                                 |                    <ul><li>Classification - binary (yes or no with probability for given class) or multi-class (class A or B with probability)</li><li>Linear Regression - predict a number (continous) </li> <li>Random trees</li><li>Support vector machines</li> <li>ANN, CNN, RNN</li> </ul>                     |
|                 Unsupervised                  |                                  Trends based on current in data (labels not provided). Spot outliers or anomalies                                | <ul><li>Clustering - Grouping similar problems together </li><li> Expectation Maximisation - Soft cluster assignment </li><li>Association Analysis - pattern mining </li><li>PageRank - link analysis</li><li>Principle component analysis</li> <li>Gaussian Mixture Models</li> <li>Boltzmann autoencoder</li></ul> | 
|               Transfer Learning               |                               Leverage machine learning models, use one model that knows A and tweak to know what B is                            |                                                                                                                    <ul><li> Natural Language processing - </li><li>Computer vision -  </li></ul>                                                                                                                     |
|            Reinforcement Learning             |                                            Perform action in define space and reward/penalise on actions                                          | 
|                Neural network                 |  Architectures that can be used in any type of machine learning problem, hence can fit into the supervised, unsupervised, semi-supervised problems. |
|                  Static data                  |                                                                       csv etc                                                                     |                                                                                                                                 
|  Streaming data constantly changed over time  |                                                                 trends in market etc                                                              |
|                Structured data                |                                                         columns, like excel spreadsheet etc                                                       |
|               Unstructured data               |                                                               Like audio, pictures etc                                                            |
|                 Feature store                 |                                            Localises commonly used features for reuse in future ml models                                         |
|                    Feature                    |                                                                Measurable phenomenon                                                              |
|                 Deep learning                 |                                          Based on neural networks. Divided into supervised and unsupervised                                       |                                                                                                                                              <ul><li>CNN/ANN</li></ul>                                                                                                                                               |
|                  Perceptron                   |                                                                                                                                                   ||
|                 Training set                  |                                                        To train model to see patterns in data                                                     ||
|                Validation set                 |                            Gives you an estimate of how the model will perform and to check performance with other models                         ||
|                  Testing set                  |                                             To evaluate the predictive performance of the trained model                                           ||
|                     Epoch                     |                                                       Single pass through through all dataset                                                     ||
|                    Iterate                    |                                                       Single pass over subset of epoch (batch)                                                    ||
|                  Batch size                   |                                                     number of datasets in subset of main dataset                                                  ||
|                    Weights                    |                     Determines the strength of connection between any two neurons in neural network. Updated after epoch/ batch                   ||
|                  Evaluation                   | After each iteration, pass evaluation to training (good to keep model on track to stop divergence) is the model doing what i expect after each epoch ||
|                   Hold-out                    |                                       Split data into test and training using given percentage (usually 80:20)                                    |                                                                                                                      Good for very large dataset or starting out. One way to reduce overfitting                                                                                                                      |
|               Cross-Validation                |                                                         Dataset randomly split into k groups                                                      ||
|            Hyper-parameter tuning             |                  Tunes the model (before training model) so that it is well generalised to both training and future predictions                   ||


[comment]: <> (## TLDR: Top tips for whole ML process)

[comment]: <> (- Obtain Data: State what you need and why. Get the data from the source)

[comment]: <> (- Explore Data: Looking at your comp)

[comment]: <> (- Prepare data: Clean data, Transform Data, Reduce Data)

## Building ML Project 
When you start a machine learning project, there should be specific steps that one should follow in order to ensure best 
practices:

### 1: Project definition
1. Check if simple coded solution could work. If not, why?

> For example, a business comes to you to try and determine the likelihood of customers 
> leaving their company within the next 6 months. This data isn't readily available, 
> it must be generated by mathematically looking at how the data the business has currently
> can help predict that likelihood. So must use ML here.

2. Check if ML needed, if ML needed, what type of ML problem is it: Supervised, Unsupervised, Transfer learning, Reinforcement Learning, Semi-supervised etc

<span style="color:green">todo: Find out the computational time (relative) for each of these problem types and what factors into that </span>

<span style="color:green">todo: Find out examples of transfer learning and reinforcement learning techniques</span>

<span style="color:green">todo: Find better description for neural network </span>

### 2: Check data
1. Does the data match the problem definition? Check type of data you have available and what you can get. 4 main types are **Structured, Unstructed, Streaming, Static**.
2. How is the data updated? The frequency of this update?
3. How can we extract data from the system? E.g db connection, xml etc
4. Checks for consistency, completeness, accuracy

### 3: Define what success looks like via evaluation metrics
1. Define what a successful end will be: 95% accuracy? 99.9% accuracy? This will depend on the [ML problem decided](#1-project-definition)

> For different use cases different levels of successes could also apply. For example, when workingin pharma for a client who deals with new drugs for patients, you will want near 100% accuracy as possible

|        Type         |                                         Examples                                         | 
|:-------------------:|:----------------------------------------------------------------------------------------:|
|   Classification    |                         Accuracy, Precision, Recall, F1, AUC/ROC                         |
|     Regression      | Mean absolute error (MAE), Mean squared error (MSE), Root mean squared error (RMSE), R^2 | 
|   Recommendation    |                                      Precision at K                                      |
| Unsupervised models |         elbow method (k-means etc) (BUT no structured methods to test accuracy)          |


<span style="color:green">todo: Look at the most popular evaluation metrics for machine learning problems. 
Create separate table to note them down and remove from here</span>

> N.B: Evaluation metric could change as the project progresses but always good to have a goal.

### 4: Choose model


### 5: Feature Engineering

> N.B: You can view profile of data to see what you are working on and create a report for it!

1. What parts of the data will be used? How will it be used? How will feature influence the model?

> How to best choose features
> - Pick features that most of the samples have!
> - Pick features that have majority non-null elements
> - Pick features that are not redundant

<span style="color:green">todo: Find out how hypothesis are tested (like the ones stated in studio) </span>

<span style="color:green">todo: What comes first? Feature selection or feature engineering? </span>

### 6: Feature Selection

Decision Trees
- internal feature selection
- Only selects important ones
- L1 norm (removal of unimportant features)

Filtering
- Use given feature score does not take into account relationship between pick those that are correlated with output. 
Dependance label

#### Feature reduction
- Very important to reduce features due to redundancy as well as improving computational time


### Outlier detection
- SVM -> Classical, K means
- Statistical modes -> check if data point within distribution

### Modelling

#### Sets
Most important is to decide how to split the data between train, validation and test sets.
- Train - to create model (70-80%)
- Validate - to tune model (10-15%)
- Test - to test and compare model (10-15%)

The split in dataset is done to improve generalisation.



#### Choose model
Based on problem and <span style="color:green">**data**</span>, what model should we use?

Some algorithms work better with specific types of data.
- Structured data?
  - Decision Tree
  - Gradient boost algorithms (e.g XGBoost, CatBoost etc)
- Unstructured data?
  - Deep learning
  - Transfer Learning

>Find out the best type of algorithms to work with specific data types, fill out this list

Also think about the optimisation techniques for the models. Popular choice is gradient descent.

#### Train model
Input (x) --> predict (y)

The biggest goal is to minimise the time spent training the model. We can do this through:
- Training on a smaller set first then see how it goes
- Use a simpler model first then build 


It is important during training that we try to avoid over-fitting.

>Find out the best ways to minimise training time in a model as well as prediction time in a model (production)

#### Tune model

Adjust hyper-parameters for models on training and validation sets. Not on test set!

- Cross Validation 
  - Split train into K subsets. Train data on K-1 folds K times. Average performance. Do this for different model settings
  - **Good** : If you know vague place on where to start searching for best parameters

- Random Search
  - Using the hyper-parameter, get a range in which you would need to search over and search (in grid like)
- Bayesian optimisation
  - Build probabilistic model of the object function and use it to smartly select hyper-parameters to evaluate
  - **Good** : If your function is complex, non-linear or expensive to evaluate

#### Test Data

Evaluate model on this data! In general model should perform well for train, validate and test models.

Ensure no over-fitting or under-fitting! To fix under-fititng the following things can be used:
- Try more advanced model
- Increase model hyper-parmeters
- Reduce amount of features
- Train longer

To fix over-fitting:
- Collect more data
- Try a less advanced model

#### Compare Model
- Compare the same inputs with the same outputs for the models.
- When comparing accuracy ensure factors like the speed to make that prediction
- Be basic in comparison, it doesn't have to be advanced analysis!

### Experimentation

How could we improve/what can we try next?

## Common algorithms used for different problems

|Problem| Algorithm| Evaluation | Pros | Cons |
|:-----:|:--------:|:---------:|:----:|:----:|
|Classification| Random Forest | Score (Accuracy),  | Fast | |


## Predictive model
Are black box usually. This encompasses neural network methods. 
**Pros**
- Better at prediction accuracy

**Cons**
- No expandability of the features used in prediction

**Optimisation**

When optimisation techniques are needed for this model the following are really helpful:
- Bayesian Optimization: perfect for global optimization of noisy black box functions

## Explanatory model
Not usually black box, relationships between features and output should be easily explained

**Decision Trees**
**Pros**
- Understandable relations between features and the desired output

**Cons**
- TODO

**Optimisation**

Usually hyper-parameters are optimised for this model. The following can be used:
- Bayesian optimisation: This can be used for this case as it can build a probabilistic model of the mapping between 
hyper-parameter and objective evaluated on a validation set
- Cross Validation:  




## Data Quality

- Where it is stored
- Time span of the data
- Do we have documentation
- Is data centralised
- How to know if data has quality issues?
  - Completeness: Missing data? like name in a customer record
  - Consistency: With data types that are common (date shown as timestamp, date time stamp) compare to other datasets
  - Accuracy: incorrect input values (birthday), really crazy outputs
  - Timeseries: NOT SURE
- How to deal with **class imbalance**
  - Measuring performance of imbalance classes?
  - ROC curve, confusion matrix?



## Hypothesis Testing
Do you basically state what you think might be indicator of target

-TODO: Testing done for categorical, data types
- Read (chi square, test for normality)

Extra Calculate the:
- Impact:
  - How will hypothesis affect the performance metric the client wants? Will it give quantifiable value
- Actionability
  - How easy will it be to implement the changes need in this hypothesis
- Testability
  - Does the datasource exist to implement the hypothesis
- TODO

## Interview prep

- **DO NOT LEARN** deep learning and neural networks (if it is not needed)
- Understand the question very well and ask questions
- Do not make assumptions about anything (even if you think you understand the english ask about the english words!)
- It's ok if you spend most of the time trying to solve the question
- Most likely to be between a Predictive model and an Explanatory model (see above for difference)

- Think about what are the steps whilst on a **client project**:
  - Why are we doing the project (Pros/Cons)
    - Benefits for all those involved (money saved, time saved, risks concerned, shift of control)
  - Question (questionaires), sample data on current situation of recieving party

  - Datasources:
    - Where I can get the datasources
    - What datasets do i need? what is available for this problem? 
      - What is the Schema
      - Who owns the data (do we have the details of this contact)
      - Data quality issues?
      - How are we extracting this data (static? CSV, DB connection, streaming)
      - Documentation (metadata or general)
      - Restrictions with data
  - Data ingestion: connecting all the data structures into one place and formatting it so that we can get to hypothesis testing
    - Can we request a sample of the data to see
    - Getting access
  - View the data landscape (like diagrams, entities, connections between data)
- State 'Unit of analysis':
  - Once trained what circumstances will the model not work on?
- Hypothesis testing (see above)
- Feature Engineering
- State model plus assumptions behind it

- Model:
  - Testing Accuracy
  - Hyperparameter optimisation
  - Bayesian optimisation
- How i would deal with classifier with 100% accuracy
  - Class could be of accuracy 100% due to a class imbalance issue. If classifier has been trained on data where the occurence of a class
is small, it will always predict any new data point as the predominate class. 
  - Fix class imbalance in the following way
    - Resampling:
      - Undersample majority class, Over sample (add samples) from minority class
        - Oversamploing minority class can be as easy as duplicating records randomly (**CON** if you do this too much overfishing, overfitting issues)
        - **CON** Undersampling can lead to loss of information, could pick bias data
      - Use `imblean` module to do sophisticated under/over sampling (cluster then pick from cluster to reduce information loss for oversampling, add randomness to undersampling)


- Get an interview coach in ML
- Do Leetcode questions
- write code in text editor and explain solution
- READ UP ON SYSTEM DESIGN, especially for MLE:
  - grokking system design : educative
  - System design book: Alex Xu's
  - Designing data intensive applications
  - Spend a lot of time doing one type of topic then switch when you understand

- Responsible for client transcation data (optimising data warehouse)
- Third party data? How will that be shared?

- Client senior analyst - working for the bank 
- Explain Number of customized dashboards
  - Marketing insights
  - operations planning
  - activity heat map
- Understand 


