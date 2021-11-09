# Kedro
- Reproducible, maintable and modular data science.
- Open source python framework
- Used to ensure consistency building ML pipelines as well as producing production ready ML workflow
- Ships with CLI and UI for data visualizing and ML pipelines

## Glossary

| Word | Definition|
|:----:|:---------:|
| Node | Pure python function that has an input and output |
| Pipeline | Collection of nodes |
| Catalog | Manages the loading and saving of your data |
| Versioning | Saving run output |

## Details

- Kedro automatically sorts pipelines so it runs in order
- Kedro is good for:
  - Ingest Raw Data
  - Clean and Join Data
  - Feature Engineering
  - Train and Validate model
- Can run pipeline from certain nodes (better for development not production)
- Can execute SQL (better to use pyspark), but can not 
- Do not use CSVs! use (Apache) parquet (good data compression, optimisation)
- Make on virtual environment per model!

### Kedro project

Catalog can be defined using environments
- Local - shared amongst team members
- Base - only developer

Local>base if the keys are the same

- conf production, conf staging - used to set up environment specific config
- put packages used in product in requirements

- Kedro runners

|Command/Tag|Description|
|:---------:|:---------:|
|`kedro new`| Set up new kedro project |
|`kedro (in project)`| Commands increase in project |
|`kedro (outside project)`| Commands decrease outside project |
|`kedro install`| Goes through requirements.txt file and installs them |
|`catalog.load(<INSERT>)`| Loads data into workspace |
|`catalog.list()`| Shows list of data that you can load in (including parameters) |
|`kedro lint`| Lints code |
|`kedro test`| Runs test |
|`kedro pipeline`||
|`kedro run --pipeline "  "`| runs specific pipeline|
|`kedro build-docs`| Build documentations from python docstrings |

## Questions

- Can you define streaming data through the files? How to define connections to Dbs?


## Misc

- Sphinx - python documentation creator
- Use environment variables for credentials
- Apache airflow - production run Scheduling
- If you remove requirements.in file you will be asked for analytics use again
