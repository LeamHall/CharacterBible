# name:     test_person_view.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Test Person output templates.

import pytest

from person import person
from view import person as person_view

def test_have_data(person):
  expected_first_name  = 'Alba'
  assert person.first_name == expected_first_name

def test_to_csv(person):
  actual_string   = person_view.to_csv(person)
  expected_string = '123|Domici|Alba||f|1416146|||Trail Rat'
  assert actual_string == expected_string

def test_to_text(person):
  actual_string   = person_view.to_text(person)
  expected_string = "123 Alba Domici [f]"
  assert actual_string == expected_string

def test_to_html(person):
  actual_string   = person_view.to_html(person)
  expected_string = "<p>123 Alba Domici [f]</p>"
  assert actual_string == expected_string

def test_bad_output_type(person):
  with pytest.raises(ValueError):
    person_view.char_string(person, 'xml')

def test_char_string_text(person):
  actual_string   = person_view.char_string(person, 'text')
  expected_string = "123 Alba Domici [f]"
  assert actual_string == expected_string

def test_char_string_html(person):
  actual_string   = person_view.char_string(person, 'html')
  expected_string = "<p>123 Alba Domici [f]</p>"
  assert actual_string == expected_string

def test_char_string_csv(person): 
  actual_string   = person_view.char_string(person, 'csv')
  expected_string = '123|Domici|Alba||f|1416146|||Trail Rat'
  assert actual_string == expected_string

