# name:     conftest.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Shared data for tests.

import pytest

@pytest.fixture()
def person_data():
  data = dict(who = "Alba", whom = "Wilbur")
  return data


