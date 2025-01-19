## Common issues Machine Learning engineers face

- Data quality issues
- Overfitting
- Underfitting
- Lack of interpretability
- Lack of scalability


## Data typing/validation in python

Think of validation as a unit test for your dataframe!

## Pandera

Validation of tabular data (not only dataframes!).

Can generate dataframes on the fly with test `schema.example)`

Many people use pandera which is a validating type framework which asserts properties of the data at runtime via schemas

you can create classes from extending pandera base classes (e.g pa.DataFrameModel) and specifying what constraints each field has

```python
import pandera as pa
from pandera.typing import Series

def is_alpha_string(value: str) -> bool:
    return value.isalpha()

class ValidateCustomers(pa.DataFrameModel):
    id: Series[int] = pa.Field(gt=0, coerce=True)
    name: Series[str] = pa.Field(checks=is_alpha_string, element_wise=True)
```

and then use in code:

```python
@pa.check_types(lazy=True)
def transform_data(data: DataFrame[ValidateCustomers]):
    ...
```

you can also catch schema errors when function is called:

```python
try:
    transform_data(invalid_data)
except pa.errors.SchemaErrors as exc:
    print(exc.failure_cases)
```

## Different types of schemas
There are two types of schemas:
- `DataFrameSchema`(object-based, enables dynamic updating of schema)
- `DataFrameModel`(class-based API, similar to dataclasses)


## Testing

hypothesis

## Explainability - XAI

> Definition:
> Set of methods to explain the results/output of models/algorithms and its biases

It is a core component of fairness in AI.

This takes into account three main methods:

**Prediction accuracy (most popular is LIME):**
Compare XAI output to results to training data set.

**Traceability (common is DeepLIFT):**
Can include setting up rules and restrictions on features to ensure outcome is explainable.
Depending on the algorithm, this could be modified. With DeepLIFT, activation energy for neurons are compared to reference neuron
and dependancies links explained.

**Decision understanding:**
Human factor, learning to trust the results of the machine and work with it.

ML models often are explained as a black box (method we have no interpretibility of the model), 
which means bias (on race, gender, location) can pose a risk to how well we can trust the model.
That alongside drift and general degradation also affects the validity of the model. Explainable AI 
helps add trust.

> [!TIP]
> See XAI as traceability methods for each part of the ML process!
> See AI as the output of a ML algorithm (where we do not know how algo reached that answer)

> [!WARNING]
> INTERPRETABILITY IS NOT EXPLAINABLITY!
> Interpretabilty involves understanding the cause and link behind the output of the AI model (
> How well a human can also predict the output of a model given the same input). Explainablity is 
> how the algorithm got there.

## Interpretability methods:

Model agnostic methods to understand what a model used to get to its outcome.

**Partial Dependance plot**

PROS:
- Good to see how 1/2 features varying values change the predictive value. 

CONS:
- Does show heterogeneous effects

## Scaling AI

To scale a model, the following is important to track:

- Drift
- Deployment status
- fairness
- Data/model quality
- Model risk

______

GPU
Conda 
Pip

which is best for machine project?





