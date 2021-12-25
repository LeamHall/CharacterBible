# name:     conftest.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Shared data for tests.

import pytest
from person import Person

@pytest.fixture()
def person():
  p             = Person()
  p.first_name  = "Alba"
  p.last_name   = "Domici"
  p.gender      = "f"
  #p.physical    = "Short blond hair, raging blue eyes. Scar over right eyebrow." 
  return p 


