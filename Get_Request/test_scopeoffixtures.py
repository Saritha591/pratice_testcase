import pytest
import json
from datetime import datetime

@pytest.fixture()
def test_only_used_once():
    with open("app.json") as f:
        config = json.load(f)
    return config

@pytest.fixture()
def test_light_operation():
    return "I'm a constant"

@pytest.fixture()
def test_need_different_value_each_time():
    return datetime.now()