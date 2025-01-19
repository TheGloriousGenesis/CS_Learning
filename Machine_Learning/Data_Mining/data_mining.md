# Data mining

## Glossary
|                      Term                       |                                      Definition                                       |
|:-----------------------------------------------:|:-------------------------------------------------------------------------------------:|
|                 Series (Pandas)                 |                           Similar to a column of data (1D)                            |
|               Dataframe (Pandas)                |                           A collection of series data (2D)                            |
|                     Dataset                     |                              Collection of data objects                               |
|                   Data object                   |                   A record, data point, event, observation, sample                    |
|                    Attribute                    | A characteristic of a data object that can vary, also called variable, field, feature |
|                  Observations                   |                            Observed values of an attribute                            |
|          Buffer data (data streaming)           |            Temporarily hold data in memory until its time to be processed             |
| MICE (Multiple Imputation by Chained Equations) |                 Predict missing values using machine learning models                  |

## Data types

There are two types of data:
- **Categorical**
- **Numerical**

In these categories they further break down into the follow sub-types:
- **Categorical** - Think qualitative
  - Nomial (think no order - nomial)
    - Binary (having only two possible values). This can be further split into the following
      - Symmetric (no importance on which outcome is 1 or 0)
      - Asymmetric (importance on outcome being 1 or 0)
  - Ordinal (Ordered in a meaningful way)

- **Number** - Think quantitative
  - Ratio (Have intrinsic zero point (like temperature). The ratios between values have meaning) 
  - Interval (equal units. Technically all ratio data is classified as interval, but interval *has no true zero point*)
  - Continuous
  - Discrete

### Test Question

1. What type of data is represented by the color of a car (e.g., red, blue, green)? 
   2. Categorical (nomial)
2. If a dataset contains the weight of individuals in kilograms, what type of data is this?
   3. Numerical(continuous, ratio, interval)
3. A survey asks respondents to rank their satisfaction on a scale from 1 to 5. What type of data is this?
   4. Categorical (ordinal)
4. The number of cars sold by a dealership each day. What type of data is this?
   5. Numerical (discrete)
5. The brand of a smartphone (e.g., Samsung, Apple, Google). What type of data is this?
   6. Categorical (nomial)
6. Temperature in degrees Celsius recorded every day. What type of data is this?
   7. Numerical (continous, ratio)
7. A column representing whether a product was purchased (Yes/No). What type of data is this?
   8. Categorical (nomial, binary, symmetrical)
8. What type of data represents the number of children in a household? 
   9. Numerical (ratio, discrete)
9. The education level of individuals (e.g., High School, Bachelor’s, Master’s). What type of data is this? 
   10. Categorical (ordinal)
10. Age of people in years in a dataset. What type of data is this? 
    11. Numerical (continuous, ratio)
11. Type of blood group (e.g., A, B, AB, O). What type of data is this? 
    12. Categorical (nomial)
12. The number of accidents occurring in a city each day. What type of data is this? 
    13. Numerical (discrete, ratio)
13. A dataset contains people's salary information. What type of data is this? 
    14. Numerical (continuous)
14. The type of fruit (e.g., apple, orange, banana) in a dataset. What type of data is this? 
    15. Categorical (nominal)
15. Movie ratings, ranging from 1 star to 5 stars. What type of data is this? 
    16. Categorical (ordinal)
16. Whether a user is a subscriber or not (True/False). What type of data is this? 
    17. Categorical (nomial, binary, symmetrical)
17. The distance traveled by cars in kilometers. What type of data is this?
    18. Numerical (continous, ratio)
18. The number of bedrooms in a house. What type of data is this? 
    19. Numerical (discrete, ratio)
19. What type of data is represented by ZIP codes (e.g., 94105, 10001)? 
    20. Categorical (nomial)  (this is not Numerical (discrete) as these numbers are considered labels or identifers)
20. The customer’s satisfaction rating (Very Unsatisfied, Unsatisfied, Neutral, Satisfied, Very Satisfied). What type of data is this?
    21. Categorical (nomial)

Data also falls into one of these three categories:
- **Record**: Collection of data objects
- **Graph**: Collection of data objects with relations stored between data objects
- **Ordered (Timeseries)**: Collection of data object ordered and related by time or space


## Data warehouse



## Overview - Data Streaming

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
> - Availability (must have low latency, high availablity, high reliability), Scalability (have peak/low loads) and Durability (have fault tolerant) are top concerns when working with streaming data

## Glossary

