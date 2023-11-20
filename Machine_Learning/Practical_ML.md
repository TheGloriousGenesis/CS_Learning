## Common issues Machine Learning engineers face

- Data quality issues
- Overfitting
- Underfitting
- Lack of interpretability
- Lack of scalability


# Data typing/validation in python

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

### Different types of schemas
There are two types of schemas: 
- `DataFrameSchema`(object-based, enables dynamic updating of schema) 
- `DataFrameModel`(class-based API, similar to dataclasses)


### Testing

hypothesis

