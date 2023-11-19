# name:     test_person_view.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Test Person output templates.

import pytest

from app.person import person
from app.view import person as person_view

def test_have_data(person):
  expected_first_name  = 'Alba'
  assert person.first_name == expected_first_name

def test_to_csv(person):
  actual_string   = person_view.to_csv(person)
  expected_string = '123|Domici|Alba||f|1416146|||Trail Rat'
  assert actual_string == expected_string

def test_to_text(person):
  actual_string   = person_view.to_text(person).split("\n")
  expected_string_1 = "123 Alba Domici [F]"
  expected_string_2 = "Birthdate: 1416146"
  expected_string_3 = "Plot: "
  expected_string_4 = "Temperament: "
  expected_string_5 = "Notes: Trail Rat"
  assert actual_string[0] == expected_string_1
  assert actual_string[1] == expected_string_2
  assert actual_string[2] == expected_string_3
  assert actual_string[3] == expected_string_4
  assert actual_string[4] == expected_string_5

def test_to_html_without_idx(person):
  #actual_string   = person_view.to_html(person).split("\n")
  actual_string   = person_view.to_html(person, idx = False)
  actual_string   = actual_string.strip()
  expected_string = "<p><a href=\"people/123\">123</a> Alba Domici [F]</p>"
  assert actual_string == expected_string

def test_to_html_with_idx(person):
  actual_string   = person_view.to_html(person, idx = True).split("\n")
  #actual_string   = person_view.to_html(person, idx = True)
  #actual_string   = actual_string.strip()
  expected_string_1 = "<p>123 Alba Domici [F]</p>"
  expected_string_2 = "<p>Birthdate: 1416146</p>"
  expected_string_3 = "<p>Plot: </p>"
  expected_string_4 = "<p>Temperament: </p>"
  expected_string_5 = "<p>Notes: Trail Rat</p>"
  assert actual_string[0] == expected_string_1
  assert actual_string[1] == expected_string_2
  assert actual_string[2] == expected_string_3
  assert actual_string[3] == expected_string_4
  assert actual_string[4] == expected_string_5

def test_bad_output_type(person):
  with pytest.raises(ValueError):
    person_view.char_string(person, 'xml', idx = False)

def test_char_string_text(person):
  actual_string   = person_view.to_text(person).split("\n")
  expected_string_1 = "123 Alba Domici [F]"
  expected_string_2 = "Birthdate: 1416146"
  expected_string_3 = "Plot: "
  expected_string_4 = "Temperament: "
  expected_string_5 = "Notes: Trail Rat"
  assert actual_string[0] == expected_string_1
  assert actual_string[1] == expected_string_2
  assert actual_string[2] == expected_string_3
  assert actual_string[3] == expected_string_4
  assert actual_string[4] == expected_string_5

def test_char_string_html(person):
  actual_string   = person_view.to_html(person, idx = True).split("\n")
  expected_string_1 = "<p>123 Alba Domici [F]</p>"
  expected_string_2 = "<p>Birthdate: 1416146</p>"
  expected_string_3 = "<p>Plot: </p>"
  expected_string_4 = "<p>Temperament: </p>"
  expected_string_5 = "<p>Notes: Trail Rat</p>"
  assert actual_string[0] == expected_string_1
  assert actual_string[1] == expected_string_2
  assert actual_string[2] == expected_string_3
  assert actual_string[3] == expected_string_4
  assert actual_string[4] == expected_string_5

def test_char_string_csv(person): 
  actual_string   = person_view.char_string(person, 'csv', idx = False)
  expected_string = '123|Domici|Alba||f|1416146|||Trail Rat'
  assert actual_string == expected_string

