# Data mining

## Environment set up
Hints:
- Use miniconda not anaconda (anaconda has a lot of overhead)
- Create project folder and put everything in one place
- use the following command to create the env folder in current folder
  `conda create --prefix ./ml_course/envs pandas numpy scikit-learn jupyter matplotlib`
- Unfortunately can not use `--name ml_course` to rename the env with the same

### Jupyter Notebook
Here are some general information surrounding objects that can be created in jupyter:

| Type | Description |
|:----:|:-----------:|
| Series | Similar to a column of data (1D)|
| Dataframe | A collection of series data (2D)|
| Attribute (Jupyter) | gives information about the data at hand |
| Function (Jupyter) | Executes code to manipulate or obtain insights from data |

To avoid training a model to learn patterns based on the order in which data is recorded (exception time series etc),
it is best practice to randomise the indexes of the data given. This can be done in python:
`dataframe.sample(frac=AMOUNT_YOU_WANT_TO_SHUFFLE_FRACTION)`. 
