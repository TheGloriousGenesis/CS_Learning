# Data mining

## Glossary
|             Term             |                                      Definition                                       |
|:----------------------------:|:-------------------------------------------------------------------------------------:|
|       Series (Pandas)        |                           Similar to a column of data (1D)                            |
|      Dataframe (Pandas)      |                           A collection of series data (2D)                            |
|     Attribute (Jupyter)      |                       gives information about the data at hand                        |
|      Function (Jupyter)      |               Executes code to manipulate or obtain insights from data                |
|           Dataset            |                              Collection of data objects                               |
|         Data object          |                   A record, data point, event, observation, sample                    |
|          Attribute           | A characteristic of a data object that can vary, also called variable, field, feature |
|         Observations         |                            Observed values of an attribute                            |
| Buffer data (data streaming) |            Temporarily hold data in memory until its time to be processed             |

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
- **Mode**: Best used for data type that is not numerical (Categorical).
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

### Overview - Data Streaming

Data streaming has the following architecture:

- Stream producers: Software component that creates the data (stream name, data value, sequence id) for streaming and sends it to processor to buffer/group
- Stream consumers: Software component that consumes data and processes the data in the processor. Consumers offer analytic capabilities

> [!IMPORTANT]
> - There is a many-to-many relation between streams and consumers.
> - There must also be a storage layer and processing layers. The stream producers create the data that sits in the buffer/storage, and the stream consumers sit in the processing layers consuming data from storage, processing data, then notifying storage layer to delete data if no longer needed.
> - Data streaming is different to batch processing as batch processing is focused on complex analytics and queries over most of the dataset, whereas streaming queries over data withing a rolling time window. or just the most recent one

Data streams have the following characteristics:
1. Chronologically significant (all elements include timestamps). 
2. Continously flowing (no Alpha or Omega XD)
3. Unique 
4. Imperfect (hard for data to be consistent across stream as their might be intermitent errors at source resulting in damaged or missing elements)
5. Non-homogenous (could be coming from multiple source formats)
6. Usually very large amounts of data (needs storing in a record ordering and consistent storage where you can read/write fast and reliably for the cheap cheap)

Common usecases include:
- Data analytics - reporting, monitoring, analysis
- IoT - monitor performance, sensors on items
- Real time recommendations - e.g geolocation
- Media and gaming - analyse player-game interactions

> [!CAUTION]
- Availability (must have low latency, high availablity, high reliability), Scalability (have peak/low loads) and Durability (have fault tolerant) are top concerns when working with streaming data
