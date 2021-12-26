# name:     test_person_builder.py
# version:  0.0.1
# date:     20211225
# author:   Leam Hall
# desc:     test person_builder


from person import Person
from person.person_builder import PersonBuilder

def test_create_basic():
  pb  = PersonBuilder()
  p   = pb.return_person()
  assert isinstance(p, Person)

def test_basic_person(person_base):
  assert person_base.physical       == [ 'tall, dark haired, etc' ]
  assert person_base.mental         == { 'plot': 'success' }
  assert person_base.first_name     == 'John'
  assert person_base.last_name      == 'Dough'
  assert person_base.gender         == 'm'
  assert person_base.birth_info     == { 'year': 1234, 'day': 56 }
  assert person_base.notes          == ''
  assert person_base.relationships  == {}
  assert person_base.cultures       == []
