# Exploration
In order to work with the data, one must understand what value of data we can extra. This is exploring the characteristics
of the data. Key factors and solutions are:
- **Sparsity**: How asymmetric the data is, this is described by the imbalance in the values in the data set

- *Resolution**: The patterns extracted can be different at different sizes. Best to ensure that the features used are all normalized 
in the same way

- **Size**: Number of attributes available to use

- **Dimensionality**: How many features/attributes are present

Other factors one has to take into account is if the data is reliable, accessible, accurate, useful and complete (where possible).

To explore how the data is distributed, we can look at the central tendency of the data. These statistics can be used during *imputation* 
in order to fill in data:
- **Mean**: Sensitive to outliers (due to all values being added and divided by number of values). Can be fixed by excluding values.
- **Median**: Better fit if outliers are present
- **Mode**: Best used for data type that is not numerical (Categorical).
- **Variance**: Sensitive to outliers

In order to get the most out of the data, we must ensure we are only using data that gives the most importance in relation to the target variable 
and reduces redundancy. We must look at how similar/dissimilar attributes are.

### Similarity - Distance-Based Methods/similarity learning

https://www.datacamp.com/blog/what-is-similarity-learning

To determine meaningful relations between data points, we can use metrics to see how similar or how different data is within a set.
These methods often scored on a range from 0 to 1. 

For single attribute objects, similarity measured differently (refer to notebook).

Commonly used similarity checks for multi attribute objects are:
- **Supremum distance** (good for ????)
- **Minkowski distance** (good for ????)
- **Simple matching coefficent** (good for binary data)
- **Jaccard coefficent** 
- **Cosine similarity** (good for )
- **Chi-squared**

____

The resolutions with come in the form of [data preprocessing](data_preprocessing.md)