from typing import Dict, Any

import pandas as pd
import pandera as pa
from pandera.typing import DataFrame, Series


class ValidateCustomer(pa.DataFrameModel):
    id: Series[int] = pa.Field(gt=0, lt=100, coerce=True)
    name: Series[str] = pa.Field(nullable=False)


# @pa.check_types(lazy=True)  <-- #myinfo: if you do not include this annotation is does no enforce the check.
def get_customer(data: Dict[str, Any]) -> DataFrame[ValidateCustomer]:
    return pd.DataFrame(data)


def test_pandera_throw_error_on_invalid_data():
    data = {
        'id': [14, 5],
        'name': ["Ana", None]
    }
    try:
        get_customer(data)
    except pa.errors.SchemaErrors as exc:
        print(exc.failure_cases)
