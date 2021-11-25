# Data mining

## Glossary
| Term|Definition|
|:----:|:-----------:|
| Series (Pandas) | Similar to a column of data (1D)|
| Dataframe (Pandas) | A collection of series data (2D)|
| Attribute (Jupyter) | gives information about the data at hand |
| Function (Jupyter) | Executes code to manipulate or obtain insights from data |
| Dataset | Collection of data objects |
| Data object | A record, data point, event, observation, sample |
| Attribute | A characteristic of a data object that can vary, also called variable, field, feature |
| Observations | Observed values of an attribute |


## Environment set up
Hints:
- Use miniconda not anaconda (anaconda has a lot of overhead)
- Create project folder and put everything in one place
- use the following command to create the env folder in current folder
  `conda create --prefix ./ml_course/envs pandas numpy scikit-learn jupyter matplotlib`
- Unfortunately can not use `--name ml_course` to rename the env with the same

## Jupyter Notebook
To avoid training a model to learn patterns based on the order in which data is recorded (exception time series etc),
it is best practice to randomise the indexes of the data given. This can be done in python:
`dataframe.sample(frac=AMOUNT_YOU_WANT_TO_SHUFFLE_FRACTION)`. 

## Data types
There are two types of data:
- **Categorical**
- **Numerical**

In these categories they further break down into the follow sub types:
- **Categorical**
  - Nomial (Having no intrinsic order)
    - Binary (having only two possible values)
      - Symmetric (no importance on which outcome is 1 or 0)
      - Asymmetric (importance on rare outcome being 1 or 0)
  - Ordinal (Having intrinsic order)
- **Number**
  - Interval (Have equal unit section)
  - Ratio (Have intrinsic zero point (like temperature))

Data also falls into one of these three categories:
- **Record**: Collection of data objects
- **Graph**: Collection of data objects with relations stored between data objects
- **Ordered (Timeseries)**: Collection of data object ordered and related by time or space

## Exploration
In order to work with the data, one must understand what value of data we can extra. This is exploring the characteristics
of the data. Key factors are:
- **Sparsity**: How asymetric the data is, this is described by the imbalance check below in preprocessing
- **Resolution**: The patterns extracted can be different at different sizes. Best to ensure that the features uses are all normalized 
in the same way
- **Size**: Number of attributes available to use

Other factors one has to take into account is if the data is reliable, accessible, accurate, useful and complete (where possible).

To explore how the data is distributed, we can look at the central tendency of the data. These statistics can be used during *imputation* 
in order to fill in data:
- **Mean**: Sensitive to outliers (due to all values being added and divided by number of values). Can be fixed by excluding values.
- **Median**: Better fit if outliers are present
- **Mode**: Best used for data type that is not numerical.
- **Variance**: Sensitive to outliers

In order to get the most out of the data, we must ensure we are only using data that gives the most importance and reduces
redundancy. We must look at how similar/dissimilar attributes are.

### Similarity
Often scored on a range from 0 to 1. For single attribute objects, similarity measured differently (refer to notebook).
Commonly used similarity checks for multi attribute objects are:
- **Supremum distance** (good for ????)
- **Minkowski distance** (good for ????)
- **Simple matching coefficent** (good for binary data)
- **Jaccard coefficent** 
- **Cosine similarity** (good for )
- **Chi-squared**

## Preprocessing
There are 4 steps commonly used in preprocessing:

### Imputation (filling in missing values)

`df.isna().sum()` and `df.isnull().sum()` will do the same thing! Can use any of it.

### Outlier Detection (identifying what the outliers)

### Imputation (fill missing data)

### Normalisation



### Visualisation

## Data warehouse



