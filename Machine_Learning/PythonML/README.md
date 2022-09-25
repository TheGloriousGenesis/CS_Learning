## Environment set up

- Use miniconda not anaconda (anaconda has a lot of overhead)
- Create project folder and put everything in one place
- Type command to create the env folder in current folder
  `conda create --prefix ./ml_course/env pandas numpy scikit-learn jupyter matplotlib`
- Environment created will be named in the form `<absolute path to where command is run>/ml_course/env`.
  > Unfortunately can not use `--name ml_course` to rename the env with the same
- Activate environment with `conda activate <environment name>`

## Jupyter Notebook
To activate jupyter notebook using conda, type `jupyter notebook`
To avoid training a model to learn patterns based on the order in which data is recorded (exception time series etc),
it is best practice to randomise the indexes of the data given. This can be done in python:
`dataframe.sample(frac=AMOUNT_YOU_WANT_TO_SHUFFLE_FRACTION)`. 

# Pandas
## Questions:
- How to replace the nans/zeros in a column with the average of another row based on conditional grouping of values in that row?

`df.groupby('GROUP_COLUMN')['NAN_COLUMN'].transform(lambda x: x.fillna(x.mean()))`

# Numpy



