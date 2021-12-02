# <ins> General overview of types of ML problems </ins>

---
 
| Word | Definition|
|:----:|:---------:|
|Hyper parameter| Tunable variable that affects how well models fit to the data provided|
|Class Imbalance| If one class has a lot of data, this affects the accuracy of the distributing data |
|Over-fitting| When performance on the training dataset is low but high on the test dataset |
|Under-fitting| When performance on the testing dataset is low but high on the train dataset |
|Bias (common amongst all models) | Related to accuracy somewhat, how much predicted differs from actual |
|Variance (common amongst all models) | Spread of (predicted) data points when given similar input from same population|

## Overview - Regression

### Linear Regression
[KagglePractice](https://www.kaggle.com/faressayah/linear-regression-house-price-prediction)

*Definition*: Used to predict continuous variables

The hypothesis function for a regression model for a univariate linear regression is given by 

$$
H_{\theta}(x) = \theta_{i} + \theta_{j}x
$$

This is used to estimate the real model.

Cost function (also called the error function) used to see if regression model is viable! A common cost function tends to be
least squared error, which is given by the following:

$$
J(\theta_{i}\theta_{j}) = \frac{1}{2}\sum_{i=1}^{m}\left ( \left ( \theta_{0} + \theta_{1} x^{(1)} \right ) - y \right ) ^2
$$

where *m* = dataset size.

The problem is, **given X and Y, what is the value of the weight in the cost equation that can give the minimum value.**

As the cost function learns weight, in this case, it is linear in respect to weight not variable.

We are trying to minimise the amount of errors in our model, hence we need to reduce the cumulative error in the model.
This is why we say we need to *minimise the error function*. To do so, we take the derivative of the error function
and set this to zero to find the minima. The least squares equation is convex which means there is always a minima. 

**But what about if we have non-linear algorithms that we want to minimise? Can't use least squares!**
Instead we must use numerical approximation to optimisation to give us a close solution to ordinary least squares solution.

### Gradient Descent

*Definition*: Used to numerically approximate minimising cost function.

We start with an initial weight and use the following to update the weights:

$$
\theta_{j + 1} = \theta_{j} - \alpha\frac{\partial J (\theta_{i}\theta_{j})}{\partial \theta_{j}}
$$

Where the gradient is shown below:

$$
\frac{\partial J (\theta_{i}\theta_{j})}{\partial \theta_{i}} = -\frac{x}{M}\sum_{i=1}^{m}\left ( \left ( \theta_{i} + \theta_{j} x^{(1)} \right ) - y \right )
$$

The update comprises the gradient and step value, when the gradient (derivative in regards
to the weight) is negative, we know we are heading in the right direction to the minima as the second term is added to the weight in the
previous iteration because we need to increase the value of the weight to get closer to it (and vice versa)

**Always ensure you choose the correct value for alpha! :smile:**

---

## Overview - Feature Selection/ Dimension reduction

[KagglePractice](https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection)
[KagglePractice](https://www.kaggle.com/kanncaa1/feature-selection-and-data-visualization)

Feature engineering refers to both adding new features from constructing them from available data, and selecting features 
from the data already given. 

An easy way to see if features are correlated to each other is first to check correlation matrix. A heatmap (visualisation of
correlation matrix) is the most powerful to use.

### Feature construction

Constructing new features allows these features to be checked against target to see if these combined features have a higer
correlation to the target or nah.

**Usage**
Some examples of this listed below. 

- **Polynomial Features** : Simply add powers to the features already given, or multiply variables together
  - easy way of seeing how features interact with each other to influence the end goal.
- **Domain Knowledge Features** : Using expert knowledge to create features that are likely to be useful.
- **Backward Selection** : train classifier on all features, remove one, see the improvement to the model (Find better model,
more expensive than forward).
- **Forward Selection** : train classifier on one feature, add one, see the improvement to the model.

**Pros**
- Good to use when you need to reduce the dimensions of the data but still keep relevant information.
- Use on any model

**Cons**
- Have to train validation data on subset of features to see which ones are the best to choose. This is costly.

### Feature reduction

**Usage**

Each feature created is assigned a score and top *X* picked:

- **Principal Component Analysis** :
- **Chi squared Test** : Test can be used to select features which heavily dependent on the target/response (not independent)
- **Domain Knowledge Features** : Using expert knowledge to select features that are likely to be useful.
- **Decision Tree** : Best performing features kept as close to the root of the tree as possible
- **L1,L2,L0 regularizer** : (In built feature selection)

**Pros**
- Good to use when you need to reduce the dimensions of the data but still keep relevant information.
- Fast and simple enough to use for any algorithm
- (With Decision Tree) Irrelevant attributes never chosen.

**Cons**
- Doesn't take feature dependency on other features.

---

## Overview - Classification - UNFINISHED
[KagglePractice](https://www.kaggle.com/dansbecker/classification)

Classification can be split into two sub categories:

*Classification task*:
The process of predicting discrete, finite, categorical class labels in supervised manor for new data.

*Learning Algorithm*:
Created classifier by using datasets. Commonly used classifiers include: decision tree induction, k-nearest neighbours,
support vector machine etc.

### Nearest neighbour
*Definition* Check **k** nearest neighbours (usually done through euclidean distance but can use other similarity/distance measures)
Here **k** is the hyper-parameter. 

**Usage**:
Best used when you need to predict categorical class labels with discrete data.

**Pros**:
- Robust to outliers
- Scalable
- Speed
- Size

**Cons**

### Performance of classifiers 
To check the performance of this classifier, can use the following metrics:

- Accuracy : Which describes which data points have been classified correctly. This is not always great to use due to class imbalance.
    
    $$ 
    \frac{N_{tp} + N_{tn}}{N} 
    $$

- Sensitivity (Recall) : True positive rate. When it's positive, how often does it predict positive?
- Specificity : True negative rate. When it's negative, how often does it predict negative?
- Precision : Percentage labelled as positive that are actually positive

  $$
  \frac{N_{tp}}{N_{tp} + N_{fp}}
  $$

- Recall :  Percentage of actual positives labelled as actual positives (also known as completeness). *High recall* means
confidence in detecting positive observations.

$$
\frac{N_{tp}}{N_{tp} + N_{fn}}
$$

- F1 score : Measure a models' accuracy. Having a high F1 value is a high accuracy model

$$
\frac{N_{tp}}{N_{tp} + \frac{(N_{fp} - N_{fn})}{2}}
$$

OR

$$
\frac{ 2 x precision x recall }{ precision + recall }
$$

- Error rate : miscalculation rate

$$
\frac{N_{fp} + N_{fn}}{N}
$$

To describe the performance the following can be used:
- ROC : A graph drawn to detect the best threshold value that is a good trade off between true positive rate and false
  positive rate. TPR = Sensitivity = TP/P. FPR = FP/N = 1 - specificity. Area under curve gives success rate of model.
  - High threshold = low sensitivity (low true positive rate), High specificity (high true negative rate)
  - Low threshold = high sensitivity, low specificity
  
- Confusion matrix

---

## Overview - Density estimation

[KagglePractice]()

Kernel density estimation is a method for visualizing the distribution of observations in a dataset.

---

## Overview - Logistic Regression

[KagglePractice](https://www.kaggle.com/mnassrib/titanic-logistic-regression-with-python)
[KagglePractice](https://www.kaggle.com/parulpandey/deep-dive-into-logistic-regression-for-beginners)

TYPE: Classification

Logistic regression is an extension of linear regression, where linear regression deals with continuous variable 
prediction, Logistic regression deals with categorical (nomial/ordinal) variable prediction. It predicts the probability 
of the outcome variable.

It has a similar formula to linear regression but calculates the logistic of the result so that the output value is always
between 0 and 1

$$
Put logistic equation in here

Where
\sigma (t) = \frac{1}{1 + \exp(-t)}
$$

Positive values lead to higher chance the class will be predicted 1

Negative values lead to higher chances the class will be predicted 0

Classes predicted on the p == 0.5 threshold (more than or equal == 1, less than == 0)
**Algorithm**
**Usage**
**Pros**
**Cons**
**Performance**
Confusion matrix

---

## Overview - Ensemble/Boosting

[KagglePractice](https://www.kaggle.com/yassineghouzam/titanic-top-4-with-ensemble-modeling)
[KagglePractice](https://www.kaggle.com/arthurtok/introduction-to-ensembling-stacking-in-python)

Ensemble methods involve predictive models to achieve a better accuracy and model stability.

*Can also combine **different** models!*

**Algorithm**
- *Bagging*
  - Take sub-samples of dataset (N samples) with replacement
  - Train classifiers on sub-samples. 
  - Combine classifiers 
- *Boosting*
- *Stacking*

**Usage**
- Ideal for regression and classification

**Pros**
- Higher number of models will always give better performance (reduce original variance by 1/n, where n: number of classifiers)
- (Bagging)

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

Can be supervised or unsupervised due to the ability to 

**Algorithm**
- Take sub-sample of dataset (N samples) with replacement
- Out of M attributes, pick a number m < M at each node (constant for the whole tree while we grow it)
- Pick m attributes at node at random every time. The best of these m (one that optimises split) is used to split the node (sub nodes etc)
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

**Cons**
- 
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

### Decision Tree:

- The area of the predictive space is split/segmented into regions known as terminal nodes or leaves of the tree
- Decision trees are drawn upside down
- Supervised

**Algorithm**
- Determine how regions will be split: minimise Residual sum of squares (create high dimensional boxes)
  - Gini
  - Chi-Square (Higher is better)
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

---

## Overview - Deep Learning
[KagglePractice](https://www.kaggle.com/kanncaa1/deep-learning-tutorial-for-beginners)
[KagglePractice](https://www.kaggle.com/c/ann-and-dl-image-classification/overview)

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
