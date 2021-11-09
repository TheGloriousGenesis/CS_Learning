# Machine Learning

## Glossary

| Word | Definition|
|:----:|:---------:|
| Generalisation | The ability for the model to adapt itself to new unseen data |
| Recommendation Systems | Predict what the user might enjoy watching or buying |
| Association rule learning (Affinity Analysis) | Unsupervised learning technique that only works with categorical data |
| Support (Affinity Analysis) | The frequency of the pattern given by the rule |
| Confidence (Affinity Analysis) | The strength of an association rule relating to the likelihood of customer buying item A, given item B |
| Lift (Affinity Analysis) | The interestingness of a rule by checking the strength of rule over random co-occurrence if two items |
| Cost function | How best to best fit function to data |
| Overfitting | When the model fits to the training data better than the testing data. When the cost funciton ~ 0 but can't fit new data well |

[comment]: <> (## TLDR: Top tips for whole ML process)

[comment]: <> (- Obtain Data: State what you need and why. Get the data from the source)

[comment]: <> (- Explore Data: Looking at your comp)

[comment]: <> (- Prepare data: Clean data, Transform Data, Reduce Data)

## Building ML Project 
When you start a machine learning project, there should be specific steps that one should follow in order to ensure best 
practices. The following defines the steps:

###  Project Definition
1. Check if simple coded solution could work. If not, why? 
2. Check if ML needed, if ML needed, what type of ML problem is it (suggestions below!):

#### Typnasthe of Machine Learning Problems

| Problem | Definition| Examples| Computational Time |
|:-------:|:---------:|:--------|:------------------:|
|Supervised|Trends based on current data (labels provided) | <ul><li>Classification - one thing or another</li><li>Linear Regression - predict a number</li></ul>||
|Unsupervised|Find patterns in data (labels not provided)| <ul><li>Clustering - Grouping similar problems together </li><li> Expectation Maximisation - Soft cluster assignment </li><li>Association Analysis - pattern mining </li><li>PageRank - link analysis</li></ul>||
|Transfer Learning| Leverage machine learning models, use one model that knows A and tweak to know what B is| | |
|Reinforcement Learning| Perform action in define space and reward/penalise on actions| | |

#### Tip
- Neural networks are architectures that can be used in any type of machine learning problem, hence can fit into the supervised,
  unsupervised, semi-supervised problems.

### Data
- Does the data match the problem definition?
- Check type of data
  - Static (csv etc)
  - Streaming - constantly changed over time (trends in market etc)
  - Structured (columns, like excel spreadsheet)
  - Unstructured (like audio, pictures).

Later on think about how Data Engineers will need to clean and visual data to understand their model

>Take some insights from Studio app to how data is prepared

>Think about what questions to ask about Data when it is recieved

### Evaluation 
- Define what a successful end will be: 95% accuracy? 99.9% accuracy?

| Type | Examples | - | - |
|:--------------:|:----------:|:--------------:|:-------|
| Classification | Accuracy | Precision | Recall |
| Regression |Mean absolute error (MAE) | Mean squared error (MSE) | Root mean squared error (RMSE) |
| Recommendation |Precision at K | - | - |

>Look at the most popular evaluation metrics for machine learning problems

This value and evaluation metric could change as the project progresses but always good to have a goal.


### Feature Engineering
When a model and evaluation techniques have been decided, what parts of the data will be used? How will it be used?
One must decide which features to use for your model and how can these features influence the model.

How to best choose features
- Pick features that most of the samples have!
- Pick features that have majority non null elements
- Pick features that are not redundant
- 
#### Feature reduction
- Very important to reduce features due to redundancy as well as improving computational time. This is because more 
features can lead to overfitting issues.

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


It is important during training that we try to avoid overfitting.

>Find out the best ways to minimise training time in a model as well as prediction time in a model (production)

#### Tune model
Adjust hyperparameters for models on training and validation sets. Not on test set!

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