import os

import pandas as pd
import requests

from config import MODEL_VERSION_URI


def create_tf_serving_json(data):
    return {
        "inputs": {name: data[name].tolist() for name in data.keys()}
        if isinstance(data, dict)
        else data.tolist()
    }


def score_model(data):
    headers = {"Authorization": f'Bearer {os.environ.get("DATABRICKS_TOKEN")}'}
    data_json = (
        data.to_dict(orient="records")
        if isinstance(data, pd.DataFrame)
        else create_tf_serving_json(data)
    )
    response = requests.request(
        method="POST", headers=headers, url=MODEL_VERSION_URI, json=data_json
    )
    if response.status_code != 200:
        raise Exception(
            f"Request failed with status {response.status_code}, {response.text}"
        )
    return response.json()


def convert_dtype(data):
    for index, values in enumerate(data.dtypes.values):
        if values == "int64":
            data[data.dtypes.index[index]] = data[data.dtypes.index[index]].astype(
                "int32"
            )
        if values == "float64":
            data[data.dtypes.index[index]] = data[data.dtypes.index[index]].astype(
                "float32"
            )
    return data
