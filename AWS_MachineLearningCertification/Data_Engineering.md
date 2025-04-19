## Prepare data
Seven steps to prepare your data:
1. [Gather your data](#gather-your-data)
2. [Handle missing data](#handle-missing-data)
3. [Feature extraction](#feature-extraction)
4. [Decide which features are important](#feature-selection)
5. [Encode categorical values](#encoding-categorical-values)
6. [Numeric feature engineering](#numerical-feature-engineering)
7. Split data between test and training

> [!TIP]
> The difference between [3](#prepare-data) and [4](#prepare-data) is that feature extraction != feature selection

## Types of data:
- Ground truth data - labelled by human labelers or machine learning algorithms

## Gather your data

> Description: Retrieval of raw data into machine learning pipeline input.

What data do you need for your problem? where are your sources of data from? Are we pulling from a database etc, scrapping?

> [!IMPORTANT] Understand when to use the following AWS services to gather data:
> - Amazon Data pipeline
> - AWS Glue 
> - AWS Database Migration Service (DMS)
> - Amazon SageMaker
> - Amazon Athena

## Handle missing data

> Description: The replacing (or leaving alone) of missing data

(how should missing data be handled? Should columns be deleted, values inputted etc? There are many methods that can be 
used to handle missing data:

>[!TIP]
> Ensure you understand when to use these and when not too

1. Do nothing: Allow the algorithm to fill or ignore the null values in your algorithm ([XGBoost](../Machine_Learning/MLTheory/README.md#overview---ensembleboosting) good at this)
2. Remove records: See if the record even makes sense and remove if not pivotal
   3. Can risk losing data points with values
3. Replace the record:
   4. Categorically : Either the mode, or using algorithm (below)
      5. Most frequent can introduce bias
   5. Numerical : Mean, median, other statistical methods
      1. Fails to consider relation of feature to other features when calculating average
      2. Configure, fit, transform and ravel. Ensure column or columns are pd.DataFrames and not series/arrays
4. Model based imputation:
   5. Use models/algorithms to replace values: 
      1. [K nearest neighbours](../Machine_Learning/MLTheory/README.md#nearest-neighbour),
      2. [Regression](../Machine_Learning/MLTheory/README.md#linear-regression),
      3. [Deep Learning](../Machine_Learning/MLTheory/README.md#overview---deep-learning)
6. Interpolation/extrapolation
7. Forward filling/ Backward filling
8. Hot deck imputation

## [Feature Extraction](../Machine_Learning/MLTheory/README.md#feature-extraction--creation)

> Description: Create new features in your data. 

What features can you extract from your data? This is regarding ensuring dimensions make sense for the model (too many, too little, need new ones) or the columns make sense

## [Feature Selection](../Machine_Learning/MLTheory/README.md#feature-selection)

> Description: Removing unimportant features from your data. 

Which features do you need to prove your hypothesis? Validate through methods like PCA, rank, confusion matrix.

## [Encoding Categorical values](../Machine_Learning/MLTheory/README.md#encoding)

> Description: Converting human to computer representations of data

Models can't deal with human language, they deal with numerics. Converting and transforming features into computer useful values

## [Numerical Feature Engineering](../Machine_Learning/MLTheory/README.md#encoding)

> Description: Simplifying numerical input to help the model learn better

Sometimes even numerical features are not useful in their current state so they too need to be converted, not on the same 
scale, binning to reduce range of data etc. 