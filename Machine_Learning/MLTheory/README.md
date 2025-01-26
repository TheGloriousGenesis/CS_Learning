# <ins> General overview of types of ML problems </ins>

---
 
|                 Word                 |                                     Definition                                     |
|:------------------------------------:|:----------------------------------------------------------------------------------:|
|           Hyper parameter            |       Tunable variable that affects how well models fit to the data provided       |
|           Class Imbalance            | If one class has a lot of data, this affects the accuracy of the distributing data |
|             Over-fitting             |    When performance on the training dataset is low but high on the test dataset    |
|            Under-fitting             |    When performance on the testing dataset is low but high on the train dataset    |
|   Bias (common amongst all models)   |                  Tendancy to learn the wrong thing (underfitting)                  |
| Variance (common amongst all models) |      changes in model when using different portions of the training data set       |
|               Support                |        The number of actual occurences of the class in a specified dataset         |

> [!NOTE]
> Regarding Model performance: In any problem, it is not possible to create perfect model. This is due to bayes error rate,
> minimal error that the model can have, latent variables factors we can't measure, noise in physical process of obtaining data etc.
____

## Overview - Regression

### Linear Regression

> Definition: Used to predict continuous variables

#### Kaggle Practice
- [House price prediction](https://www.kaggle.com/faressayah/linear-regression-house-price-prediction)

#### Usage:
- Can be used as imputation method, where values for missing data can be predicted by training a model on best features 
correlating to target (features decided by correlation matrix first)

#### Pros:

#### Cons:
- Sensitive to outliers 

#### Algorithm

> [!NOTE]
> Assumptions:
> - Errors of the residuals follow normal distribution
> - Relationship between X and Y is linear, (observations are independence of each other).
> - For any value X, Y is normally distributed

[//]: # (Hyperparameter : $\sigma_{j}$, $\sigma_{i}$)

The hypothesis function for a regression model for a univariate linear regression is given by 

$$
H_{\theta}(x) = \theta_{i} + \theta_{j}x
$$

Where the theta values are chosen based on values that minimise the squared distance between the dataset and line of best fit

This is used to estimate the real model.

Cost function (also called the error function) used to see if regression model is viable! A common cost function tends to be
least squared error, which is given by the following:

$$
J(\theta_{i}\theta_{j}) = \frac{1}{2}\sum_{i=1}^{m}\left ( \left ( \theta_{0} + \theta_{1} x^{(1)} \right ) - y \right ) ^2
$$

where *m* = dataset size.

The problem is, *given X and Y, what is the value of the weight in the cost equation that can give the minimum value.*

As the cost function learns weight, in this case, it is linear in respect to weight not variable.

We are trying to minimise the amount of errors in our model, hence we need to reduce the cumulative error in the model.
This is why we say we need to *minimise the error function*. To do so, we take the derivative of the error function
and set this to zero to find the minima. The least squares equation is convex which means there is always a minima. 

> [!TIP]
> You can not use least squares if you want to minimise Non-linear algorithms. Instead, use numerical approximation for 
> optimisation to obtain a close solution to ordinary least squares solution.
____
## Overview - Optimisation

### Gradient Descent

> Definition : Used to numerically approximate minimising cost function by following the negative gradient of a cost function.

#### Usage

#### Pros

#### Cons

#### Algorithm

We start with an initial weight and use the following to update the weights:

$$
\theta_{j + 1} = \theta_{j} - \alpha\frac{\partial J (\theta_{i}\theta_{j})}{\partial \theta_{j}}
$$

Where the gradient is shown below:

$$
\frac{\partial J (\theta_{i}\theta_{j})}{\partial \theta_{i}} = -\frac{x}{M}\sum_{i=1}^{m}\left ( \left ( \theta_{i} + \theta_{j} x^{(1)} \right ) - y \right )
$$

The update comprises the gradient and step value, when the gradient (derivative in regard to the weight) is negative, we know we are heading in the right direction to the minima as the second term is added to the weight in the
previous iteration because we need to increase the value of the weight to get closer to it (and vice versa)

> [!IMPORTANT]
> Always ensure you choose the correct value for alpha! :smile:

**Momentum** builds inertia in a direction of search space, speeding up convergence, minimizing noisy gradients and avoiding local minima.

____

## Overview - Regularisation

> Definition : Used during the training of a model, when you want to keep features but reduce complexity of model by 
> reducing the magnitude of weighting. Commonly used is **L1** and **L2** norm.

The amount of reduction attained in the model is determined by the *regularisation rate*. During training, the model is trying to
minimise the following:

$$
loss = minimize(loss + \lambda complexity)
$$

where $\lambda$ is regularisation rate. A high regularisation rate reduces chances of overfitting. Model weights will follow
a normal distribution with mean weight 0. A low regularisation rate increasing changes of overfitting. Model weights will follow
flat distribution.

>[!IMPORTANT]
> Learning rate and regularisation rate pull the weights in the opposite direction! Make sure
> you balance it! High learning rate often pulls weights away from zero.

### L1

> Definition : Lasso regression. Sum of absolute value. Pushes weights to 0 (can be 0, which removes feature - feature selection).

#### Usage
- Low multi-collinearity.
- If the possibility of removing features is an ok.

#### Pros
- Keeps information (compared to removing features)
- Introduces sparsity (due to heavy penalisation on small weights)

#### Cons
- Does not work well with multi-collinearity (if there are many features related to one another, this method will remove one of the features in the model.
- High lambda will remove features and underfit model

### L2

> Definition : Sum of squares. Encourages weights toward 0 (never actually reaches).

#### Usage
- Reduce complexity of model during training when you know there aren't outliers

#### Pros
- Can handle features that are high correlated with each other.

#### Cons
- Large lambda can have big effect, adding too much weight and lead to underfitting.

#### Algorithm
$$
L_{2} regularization = w_{1}^2 + w_{2}^2 + ... w_{n}^2 
$$

----

## Overview - Feature engineering

> Definition: Feature engineering refers to both adding new features from constructing them from available data, and selecting features 
from the data already given.

*Curse of Dimensionality*

The importance of below is related to ensuring your model can execute inference to the best of its ability. One problem 
that can occur in a dataset is having too many features (or dimensions, as that refers to the number of features in dataset)
in comparison to the number of observations. This can cause **some** (not all) algorithms to train effectively. It is also very hard
to visualise higher dimension datasets (over 4D you can imagine it is hard!).

To resolve this curse of dimensionality you can use the following two options: [feature selection](#feature-selection) or 
[feature extraction](#feature-extraction--creation)

### Feature Extraction / Creation

> Definition: Create new features out of raw data. Smaller set of features. e.g From a photo: Detecting edges, corners, or colors.

#### Usage
- PCA (Principal Component Analysis)
- Polynomial Features : Simply add powers to the features already given, or multiply variables together
  - easy way of seeing how features interact with each other to influence the end goal.

#### Pros
- Good to use when you need to reduce the dimensions of the data but still keep relevant information.

#### Cons
- Requires data to be standardised (mean 0, std 1)
- Doesn't take feature dependency on other features.

### Feature Selection

> Definition: Select which raw features should and shouldn't be used. Removes features. Example: From a photo: edge feature, pixel count.

#### Kaggle Practice
- [Intro into feature selection](https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection)
- [Feature selection and visualisation](https://www.kaggle.com/kanncaa1/feature-selection-and-data-visualization)

#### Usage
- Chi squared Test : Test can be used to select features which heavily dependent on the target/response (not independent)
- Decision Tree : Best performing features kept as close to the root of the tree as possible
- L1,L2,L0 regularizer : (In built feature selection)
- Backward Selection : train classifier on all features, remove one, see the improvement to the model (Find better model,
more expensive than forward).
- Forward Selection : train classifier on one feature, add one, see the improvement to the model.
- A correlation matrix can be used to determine features are that are correlated to each other and then remove ones that are.

#### Pros
- (With Decision Tree) Irrelevant attributes never chosen.
- Most are Fast and simple enough to use for any algorithm

#### Cons
- Requires data to be normalised
- (Backward selection / Forward selection) Have to train validation data on subset of features to see which ones are the best to choose. This is costly.

### Feature abstraction

> Definition: Feature abstraction creates higher concept features/ patterns from extracted features. 
> Does not deal with raw features/data. Example: - From a photo: Combining edges and corners to detect shapes like "circle" or "triangle."

#### Usage
- Domain Knowledge Features : Using expert knowledge to create features that are likely to be useful.
- Non-Linear transformations such as binning numeric variables into categories which can then relate linearly to target variable.
binning is done to numerical values when there is not a linear relationship between the feature and binning could expose it e.g age vs book buying. age group is better indicator.


#### Pros

#### Cons

---

## Overview - Classification - UNFINISHED

> Definition : Supervised machine learning model that tries to predict data label.

Classification can be split into two sub categories:

*Classification task*:
The process of predicting discrete, finite, categorical class labels in supervised manor for new data.

*Learning Algorithm*:
Created classifier by using datasets. Commonly used classifiers include: decision tree induction, k-nearest neighbours,
support vector machine etc.

#### Kaggle Practice
- [Classification](https://www.kaggle.com/dansbecker/classification)

### Nearest neighbour
> Definition: Check **k** nearest neighbours (usually done through euclidean distance but can use other similarity/distance measures)
Here **k** is the hyper-parameter.

#### Usage:
- Predict categorical class labels with discrete data.
- In imputation, to replace missing values using feature similarity e.g if the feature missing value
is close to other features, can impute with the average of those values

#### Pros:
- Robust to outliers
- Scalable
- Speed
- Size

#### Cons
- Need to manually choose number k (can use methods to find this or hyper parameter tune)

#### Algorithm

#### Performance

To check the performance of this classifier, can use the following metrics:

- Accuracy : Which describes which data points have been classified correctly. This is not always great to use due to 
class imbalance.
    
  $$ 
  \frac{N_{tp} + N_{tn}}{N} 
  $$

- Sensitivity (Recall) : (Out of all actually positives - whether labelled correctly or not), which are labelled positive). True positive rate. When it's positive, how often does it predict positive?

  $$
  \frac{N_{tp}}{N_{tp} + N_{fn}}
  $$

- Specificity : True negative rate. When it's negative, how often does it predict negative?
- Precision : (Out of all positives (false or true) in model which is actually true positive) Percentage labelled as positive in the model that are actually positive

  $$
  \frac{N_{tp}}{N_{tp} + N_{fp}}
  $$

- Recall :  (Out of all positive in dataset which positive) Percentage of actual positives labelled as actual positives (also known as completeness). *High recall* means
confidence in detecting positive observations.

  $$
  \frac{N_{tp}}{N_{tp} + N_{fn}}
  $$

- F1 score : Measure a models' accuracy. Having a high F1 value is a high accuracy model. This is often used when data is unbalanced as it looks at balancing precision and recall on the positive class instead of correct classifications of both negative and positive observations

  $$
  F1 = \frac{2 * Precision * Recall}{Precision + Recall}
  $$

- Error rate : miscalculation rate

  $$
  \frac{N_{fp} + N_{fn}}{N}
  $$

To describe the performance the following can be used:
- ROC :
  - Likelihood of model to distinguish observations between two classes
  - A graph drawn to detect the best threshold value that is a good trade off between true positive rate and false
    positive rate. TPR = Sensitivity = TP/P. FPR = FP/N = 1 - specificity. Area under curve gives success rate of model.
  - High threshold = low sensitivity (low true positive rate), High specificity (high true negative rate)
  - Low threshold = high sensitivity, low specificity
  
- Confusion matrix
  - Elements on the diagonal should be high valued and correctly identified
  - Good to find other metrics: Precision, Recall, F1 Score

----

## Overview - Logistic Regression

> Definition : Supervised algorithm for classification. Logistic regression is an extension of linear regression, where 
> linear regression deals with continuous variable prediction, Logistic regression deals with categorical 
> (nomial/ordinal) variable prediction. It predicts the probability of the outcome variable.

#### Kaggle Practice
- [Titantic prediction](https://www.kaggle.com/mnassrib/titanic-logistic-regression-with-python)
- [Logisitic regression for beginners](https://www.kaggle.com/parulpandey/deep-dive-into-logistic-regression-for-beginners)

#### Usage

#### Pros

#### Cons

#### Algorithm

> [!NOTE]
> Assumptions:
> - Features not have to have a linear relationship 
> - If binary logistic regression, input must be binary data, likewise for ordinal
> - Must have large sample size (> 10)

It has a similar formula to linear regression but calculates the logistic of the result so that the output value is always
between 0 and 1 

$$
\sigma (t) = \frac{\exp^{b_{0} - b_{1}x}}{1 + \exp^{b_{0} - b_{1}x}}
$$

Positive values lead to higher chance the class will be predicted 1

Negative values lead to higher chances the class will be predicted 0

Classes predicted on the p == 0.5 threshold (more than or equal == 1, less than == 0)

$$
Odds = \frac{P(Event)}{P(!Event)}
$$

#### Performance
- Confusion matrix

----
## Overview - Ensemble/Boosting

> Definition: Ensemble methods involve using multiple weak predictive models combined to achieve a better accuracy and
> model stability. Theses are black box methods!


#### Kaggle Practice
- [Titanic Ensemble](https://www.kaggle.com/yassineghouzam/titanic-top-4-with-ensemble-modeling)
- [Ensemble stacking in python](https://www.kaggle.com/arthurtok/introduction-to-ensembling-stacking-in-python)

#### Usage
- Ideal for regression and classification

#### Pros
- Higher number of models will always give better performance (reduce original variance by 1/n, where n: number of classifiers)
- (Bagging)
- (Boosting) reduces BIAS as the model trains to fix classification errors so reduce this.

#### Cons

#### Algorithm
- *Bagging*
  - Take sub-samples of dataset (N samples) with replacement
  - Train classifiers on sub-samples. 
  - Combine classifiers 
- *Boosting*
  - Hyper-parameter : Number of tres, weights of trees, learning rate
  - Start with weak learners
  - Classify all classes with learners. Increase focus on misclassifed classes
- *Stacking*

**Pros**

**Cons**
- (All) Similar bias to single model 
- (Bagging) Small sample size give worse models but more diversity
- (Bagging) Big sample size give better models but less diversity (how is diversity measured)
  - increase diversity by:
    - randomising subspace that model trained in
    - randomising anything you can think of (local minima convergence methods start different locations)

**Performance**
- Use Ensemble learning to execute bias/variance trade off analysis

### Random Forest
Type of ensemble method where multiple trees are grown. Each tree classifies data point and provides a vote for that class.
The classification of the data point is then chosen by gathering votes.

Theses are black box methods!

Can be supervised or unsupervised due to the ability to 

**Algorithm**
- Hyper-parameters : No. of trees
- Take sub-sample of dataset (N samples) with replacement
- Out of M attributes, pick a number m < M at each node (constant for the whole tree while we grow it)
- Pick m attributes at node at random every time. The best of these m (one that optimises split - makes resultant as different from each other as possible) is used to split the node (sub nodes etc)
  - *N.B* the picking of subsets of features decreases the correlation between trees grown and increases the randomisation, leading to a drop in the test set error. **Also stops the strongest feature always appearing**
- Grow without pruning. Stop when user predefines it
- Predict by aggregating votes:
  - *Regression*
    - Average output.
  - *Classification*
    - Most votes of the trees

**Usage**
- Can be used for dimensionality reduction 

**Pros**
- When you can't think of an algorithm, use Random Forest!
- Can perform both classification and regression
- Can handle large datasets with higher dimensionality
- Model outputs importance of variable!
- Can estimate missing data
- Maintains accuracy when a large section of data missing
- Reduce variation because the trees are trained by a subset

**Cons**
- Too many trees can be overly complex
**Performance**

---

## Overview - Tree Based Methods
- Can be used for regression and classification

|Word|Definition|
|:---:|:--------:|
|Root node| Define the whole population|
|Splitting| Process of dividing into subnodes|
|Decision node| Actual subnode |
|Pruning| Removing subnodes of decision nodes |
|Entropy (category variable)| How homogenous the node is (zero entropy == pure node, one entropy == impure node) |
|Information Gain|1 - Entropy|
|Cross Entropy|High if predicted probability diverges form actual label vice versa|

### Decision Tree:

- The area of the predictive space is split/segmented into regions known as terminal nodes or leaves of the tree
- Decision trees are drawn upside down
- Supervised

**Algorithm**
- Determine how regions will be split (at a given node, how will we 'decide' how the data should be split): minimise Residual sum of squares (create high dimensional boxes). This in turn minimises the intra difference between nodes.
  - Gini impurity: The probability of an element in a set (node) being labeled incorrectly if label was picked out randomly from the distribution of the labels in that given set. This will tend to zero when set becomes more unified.
  - Chi-Square (Higher is better)
  - Entropy: 
- Divide predictor space (all space occupied by each data point) into J distinct non-overlapping regions
- Decision tree splits on all available variables
  - *Regression*
    - For every data point observed, check if it falls into region. If it does then we make same prediction : mean of values of
    data points into region
  - *Classification*
    - For every data point observed, check if it falls into region. If it does then we make same prediction : mode of values of
      data points into region

**Usage**

**Pros**
- Easier to interpret, nice graphical representation
- Helpful in exploratory due to :
  - Easier to identify significant variables and relations between features
- Map non-linear relationship well
- Works on very large datasets
- Works for categorical and continuous input/output variables
- Creates the best similar sets (where in the set it is different)
- Better than linear if data complexity relation high and need easily explain model

**Cons**
- Oversimplification of relationship between features
- Over fitting
- Not for continuous variables as data can be loss
- 
**Performance**
Can avoid over-fitting in decision tress:
- Setting constraint on tree size
- Tree pruning


#### Segmentation Tree
Description: Splits data into specific segments based on some sort of criteria

ML type: Unsupervised/semi-supervised 

Nodes represents subset of data, with the root node containing the whole dataset

Algorithm:
- Similar to decision tress, but if it's a clustering tree segmentation, could use clustering metrics like distance or variance between data in set/node
- Output instead of predicting a variable (in regression the mean, in classification the mode), the leaf nodes represents the actual subset that has been created with the highest similarity (Homogeneity) for a given criterion.

Usage:
- Marketing: Customers grouped based on behaviours
- Medical diagnostics: Patients with similar symptoms grouped to make diagnosis and treatment easier.

Pros:
- Interpretability: Easy to know where the output has come from as set rules in place for each node and decisions can be traced
- Scalability: Decision tress can handle large datasets easily
- Do not need specific dataset distribution to work 

Cons:
- Can overfit if data is not pruned
- Sensitive to type of decision splitting algorithm chosen

---

## Overview - Deep Learning

> Definition : 

#### Kaggle Practice
- [KagglePractice](https://www.kaggle.com/kanncaa1/deep-learning-tutorial-for-beginners)
- [KagglePractice](https://www.kaggle.com/c/ann-and-dl-image-classification/overview)

#### Usage
- Can be use for imputation, both on categorical and numerical features

#### Pros

#### Cons
---

## Overview - Clustering
[KagglePractice](https://www.kaggle.com/fazilbtopal/popular-unsupervised-clustering-algorithms)


---

## Overview - Recommendation

- Driven by Industry need
- Top 10 websites in internet retailer 500 use it.

## Applications

- Amazon : Track purchase habits of products
- Ticket merchants : Tracks movies/theatres seen
- Social : Tracks blogs you've read and suggest threads,
- Professional Social : Uses current job role to recommend roles

### Types of Recommendation Systems

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

Common real-time analytics + machine learning u

amazon sagemaker - built to make mL more accessible


### Overview - Natural Language processing

## n - grams
An n-gram is a collection of n successive items in a text document that may include
words, numbers, symbols, and punctuation.

## Text embeddings

When working with text you must convert text to numerical representations so that the models can understand relations between words.
This is called vectorisation, and the most common form is called bag of words OR CountVectorizer. It will populate one tally for each word in a sentence.

Bag of words
Pros:
- Easy analysis, simple to implement

Cons:
- Doesn't work well with sparse matrix
- Words can show up in every document
  - Issue with over populous words in the english language e.g 'the' 'is' 'a'

A slightly better approach is to use Term Frequency Inverse Document Frequency. It determines the importance of the word to the document
and takes into account extremely frequent words that may have no meaning to the actual document/corpus (such as 'the' 'is' etc)




Test assumptions regarding analysing text data with GloVe first then move onto more sophisticated models like FastText, BERT 
or any transformer (as they require a little more work)

____
## Large language model
Made of two parts:

Encoders: Maps inputs to smaller vector space by grouping similar words (hence similar outputs) and changing them into vectors (hidden state)

Decoders: Tells you which word should come next. takes input of encoder and output word that activates the highest.

> [!TIP]
> Very similar to zipping and unzipping a file! Just zipping and unzipping a word

The reason why decoders know the right word to choose is because when the difference between expected output and actual output (loss) is calculated,
it uses back propagation to make changes to the decoder and the encoder so that different encodings is made next time that word is seen.

The encoder usually compromises, as its converts large input to smaller vector space, so some words will have similar if not the same vector representation

There are some LLM that have to predicted masked words (miss a word in a sentence). Generative models are auto-regressive masked models. They have the mask 
at the end of the sentence (so it's predicting the last word and using that to predict the next word).

These models tend to be self-supervised (you dont need a seperate training/test data, you can use the output of the model and compare to input)

### GPT
GPT stands for Generative Pre-trained Transformer.

Generative - can continue predicting words based on input

Pre-trained - Model is trained on a very large corpus

Transformer - Deep learning model (encoder/decoder) that is tailored for language modelling. Basically: normal encoder encoding -> dot.product -> self attention encoding (relation between words)

### Architecture

Ingest multiple documents
have two db's: 
- vector db to store vectors

### LLM Issues
- They can hallucinate: create fake information that can sound formal
- Data poisoning: by prompts, docs, api responses etc. It can target corrupting training data and/or labels OR even during deployment stage, by
analysing api responses and combine info to learn LLM specific inputs

### LLM Solutions to Issues
- Validate data quality
- Quality filtering 
  - (using classifier-base filtering/ heuristic) to distinguish between high and low quality content
- Remove duplication (sentence, document, dataset) - this aids training the model, reduces skewness of metrics
- Remove PII
- Convert raw text to tokens (string into individual elements e.g character, word, sentence) to then into vector (convert to string/sequence to vector)
