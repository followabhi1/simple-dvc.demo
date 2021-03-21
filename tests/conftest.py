import pytest
import yaml
import os
import json


@pytest.fixture
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def schema_in(schema_path = "schema_in.json"):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
    return schema
