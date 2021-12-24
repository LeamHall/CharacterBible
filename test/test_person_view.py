# name:     test_person_view.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Test Person output templates.

import pytest

from view import person as person_view

def test_have_data(person_data):
  expected_who  = 'Alba'
  expected_whom = 'Wilbur'
  assert person_data['who'] == expected_who
  assert person_data['whom'] == expected_whom

def test_to_text(person_data):
  actual_string   = person_view.to_text(person_data)
  expected_string = "Alba kissed Wilbur"
  assert actual_string == expected_string

def test_to_html(person_data):
  actual_string   = person_view.to_html(person_data)
  expected_string = "<p>Alba really kissed Wilbur!</p>"
  assert actual_string == expected_string

def test_bad_output_type(person_data):
  with pytest.raises(ValueError):
    person_view.char_string(person_data, 'xml')

def test_char_string_text(person_data):
  actual_string   = person_view.char_string(person_data, 'text')
  expected_string = "Alba kissed Wilbur"
  assert actual_string == expected_string

def test_char_string_html(person_data):
  actual_string   = person_view.char_string(person_data, 'html')
  expected_string = "<p>Alba really kissed Wilbur!</p>"
  assert actual_string == expected_string

  
