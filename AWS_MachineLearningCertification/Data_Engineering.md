
## Prepare data
Seven steps to prepare your data:
1. gather your data (what data do you need for your problem? where are your sources of data from? are we pulling from a database etc, scrapping?)
2. handle missing data (how should missing data be handled? should columns be deleted, values inputted etc)
3. feature extraction (what features can you extract from your data? This is regarding ensuring dimensions make sense for the model (too many, too little, need new ones) or the columns make sense)
4. decide which features are important (which features do you need to prove your hypothesis? validate through methods like PCA, rank, confusion matrix)
5. encode categorical values (models can't deal with human language, they deal with numerics. Converting and transforming features into computer useful values)
6. numeric feature engineering (sometimes even numerical features are not useful in their current state so they too need to be converted, not on the same scale, binning to reduce range of data etc)
7. Split data between test and training

> [!TIP]
> The difference between [3](#prepare-data) and [4](#prepare-data) is that feature extraction != feature selection

## Types of data:
- Ground truth data - labelled by human labelers or machine learning algorithms


### Handle missing data
There are many methods that can be used to handle missing data:

1. Do nothing: Allow the algorithm to fill or ignore the null values in your algorithm ([XGBoost](../Machine_Learning/MLTheory/README.md#overview---ensembleboosting) good at this)
2. Remove records: See if the record even makes sense and remove if not pivotal
3. Replace the record:
   4. Categorically : Either the mode, or using algorithm (below)
   5. Numerical : Mean, median, other statistical methods
4. Model based imputation:
   5. Use models/algorithms to replace values:  [K nearest neighbours](../Machine_Learning/MLTheory/README.md#nearest-neighbour), [Regression](../Machine_Learning/MLTheory/README.md#linear-regression), [Deep Learning](../Machine_Learning/MLTheory/README.md#overview---deep-learning)
6. Interpolation/extrapolation
7. Forward filling/ Backward filling
