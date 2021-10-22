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

## TLDR: Top tips for whole ML process
- Obtain Data: State what you need and why. Get the data from the source
- Explore Data: Looking at your comp
- Prepare data: Clean data, Transform Data, Reduce Data

## Environment set up
Hints:
- Use miniconda not anaconda (anaconda has a lot of overhead)
- Create project folder and put everything in one place
- use the following command to create the env folder in current folder 
 `conda create --prefix ./ml_course/envs pandas numpy scikit-learn jupyter matplotlib`
- Unfortunately can not use `--name ml_course` to rename the env with the same

### Jupyter Notebook
Here are some general information surrounding objects that can be created in jupyter:

| Type | Description |
|:----:|:-----------:|
| Series | Similar to a column of data (1D)|
| Dataframe | A collection of series data (2D)|
| Attribute (Jupyter) | gives information about the data at hand |
| Function (Jupyter) | Executes code to manipulate or obtain insights from data |

To avoid training a model to learn patterns based on the order in which data is recorded (exception time series etc), 
it is best practice to randomise the indexes of the data given. This can be done in python:
`dataframe.sample(frac=AMOUNT_YOU_WANT_TO_SHUFFLE_FRACTION)`. 

## Data Modelling - Building ML Project 

###  Project Definition
- Check if simple coded solution works
- Check if ML needed
- If ML needed, what type of ML problem is it?:
  - Supervised - Trends based on current data (labels provided)
    - Classification - one thing or another 
    - Regression - predict a number
  - Unsupervised - Find patterns in data (labels not provided)
    - Clustering - grouping similar problems together
  - Transfer Learning - leverage machine learning models, use one model that knows A and tweak to know what B is
  - Reinforcement Learning - perform action in define space and reward/penalise on actions

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

### Features
Deciding which features to use for your model. How can these features influence the model?

- Pick features that most of the samples have!

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

#### Train model
Input (x) --> predict (y)

The biggest goal is to minimise the time spent training the model. We can do this through:
- Training on a smaller set first then see how it goes
- Use a simpler model first then build 

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

## Overview - Scikit Learn
Scikit Learn is the most popularly used standard in data science and machine learning professionally and worldwide.


## Overview - Regression
Hypothesis function, which is used to estimate the real model is given by:

$$
H_{\theta}(x) = \theta_{i} + \theta_{j}x
$$

Cost function (also called the error function) used to see if regression model is viable!:

$$
J(\theta_{i}\theta_{j}) = \frac{1}{2}\sum_{i=1}^{m}\left ( \left ( \theta_{0} + \theta_{1} x^{(1)} \right ) - y \right ) ^2
$$

where <em>m</em> = dataset size.

We are trying to minimise the amount of errors in our model, hence we need to reduce the cumulative error in the model.
This is why we say we need to <em> minimise the error function </em>. To do so, we take the derivative of the error function
and set this to zero to find the minima. This is called <strong> Gradient Descent</strong>. The derivative is shown below:

$$
\frac{\partial J (\theta_{i}\theta_{j})}{\partial \theta_{i}} = -\frac{x}{M}\sum_{i=1}^{m}\left ( \left ( \theta_{i} + \theta_{j} x^{(1)} \right ) - y \right )
$$

## Overview - Recommendation 

- Driven by Industry need
- Top 10 websites in internet retailer 500 use it.

## Applications

- Amazon : Track purchase habits of products
- Ticket merchants : Tracks movies/theatres seen
- Social : Tracks blogs you've read and suggest threads, 
- Professional Social : Uses current job role to recommend roles

## Types of Recommendation Systems

A system that recommends for sales purposes is different to one that recommends for education purposes.
System type can be driven by experts or by different users. Personalisation level of the algorithm
can appear in the following way:
- <em><strong>Generic</strong></em> (all users get same recommendation)
- <em><strong>Targeted</strong></em> (based on type of category the user falls into e.g age, income ..)
- <em><strong>Transient</strong></em> (based on recent tracked behaviour of user)
- <em><strong>Persistent</strong></em> (based on long term tracked behaviour - preferences)

Recommendation systems have dependencies and in order to utilise the systems. 
- Availability of data (The strength of the system depends on the amount of data that can be used for the prediction)
- Privacy Issues (Sometimes we do not want to collect data on multiple devices or whilst doing additional activities)
  - Personal Information and identity
  - Purpose of collection information
  - Security
- Trustworthiness (Systems can be made to sell items that are more profitable, or reduce the recommendations on items they know you will pick anyways)
  - Incentives
  - Biases
  - Manipulation

### Type 1: Non-Personalized: Association Rule Learning

- Works well with small datasets, small customer 
- Find patterns between items that occur together
- Capture patterns in the form:
  - If <strong><span style="color:red">antecedent</span></strong>, then <strong><span style="color:green">consequent</span></strong> <br>
   Example: If (customer buys) <strong><span style="color:red"> tortillas and jalapenos </span></strong> then customer buys <strong><span style="color:green"> beans and avocados</span></strong>
- Metrics used : Support

This is calculated by:

$$
s(A \Rightarrow B) = P (A\ \cap \ B) = s(B \Rightarrow  A)
\\
s(A \Rightarrow B) = \frac{no. \ transactions \ with \ A \ and \ B}{no. \ total \ transactions}
$$

The higher the support the more popular item bundle is and vice versa. Low support should not be used unless need to know 
item frequency


- Metrics used : Confidence
  - used to see the strength of relations between items in groups. Does not work for high frequency items as those items are not
    necessarily linked to each other (e.g buying sugar and phone credit at tesco doesn't mean sugar will be used for credit). Better
    used for low occurring items.
- Metrics used : Lift
  - A lift > 1 means items A and item B appear more often together than expected (positive association)
  - A lift < 1 means items A and item B appear less often than together expected (negative association)
  - A lift ~ 1 means items A and item B appear almost as often together as expected (no link)

- Use Metrics with caution