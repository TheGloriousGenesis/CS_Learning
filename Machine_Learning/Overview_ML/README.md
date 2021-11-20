# General overview of types of ML problems


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

The problem is basically, **given X and Y, what is the value of the weight in the cost equation that can give the minimum value.**

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

The update section of the equation (the $$ \delta\theta $$) holds the gradient and step value, when the gradient (derivative in regards
to the weight) is negative, we know we are heading in the right direction to the minima as the second term is added to the weight in the
previous iteration because we need to increase the value of the weight to get closer to it (and vice versa)

**Always ensure you choose the correct value for alpha!**





## Overview - Feature Selection/ Dimension reduction
[KagglePractice](https://www.kaggle.com/willkoehrsen/introduction-to-feature-selection)
[KagglePractice](https://www.kaggle.com/kanncaa1/feature-selection-and-data-visualization)

## Overview - Classification
[KagglePractice](https://www.kaggle.com/dansbecker/classification)

## Overview - Density estimation
[KagglePractice]()

## Overview - Logistic Regression
[KagglePractice](https://www.kaggle.com/mnassrib/titanic-logistic-regression-with-python)
[KagglePractice](https://www.kaggle.com/parulpandey/deep-dive-into-logistic-regression-for-beginners)

## Overview - Ensemble/Boosting
[KagglePractice](https://www.kaggle.com/yassineghouzam/titanic-top-4-with-ensemble-modeling)
[KagglePractice](https://www.kaggle.com/arthurtok/introduction-to-ensembling-stacking-in-python)

## Overview - Deep Learning
[KagglePractice](https://www.kaggle.com/kanncaa1/deep-learning-tutorial-for-beginners)
[KagglePractice](https://www.kaggle.com/c/ann-and-dl-image-classification/overview)

## Overview - Clustering
[KagglePractice](https://www.kaggle.com/fazilbtopal/popular-unsupervised-clustering-algorithms)


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
