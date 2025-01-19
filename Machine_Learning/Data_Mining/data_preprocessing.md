## Preprocessing
There are 4 steps commonly used in preprocessing:

1. Imputation (filling in missing values)

`df.isna().sum()` and `df.isnull().sum()` will do the same thing! Can use any of it.

2. Outlier Detection (identifying what the outliers)

Outliers can be determined with domain knowledge or statistically. With domain knowledge,
really think outloud! Does that data make sense for that column type? Even include bias in your thinking to see if you can spot an outlier!

There are two types of outliers

- Natual outlier (should keep and resolve via taking natural log or use mean)
- Artificial outlier (delete)

To resolve outliers you can either use a standard imputer or MICE


3. Normalisation