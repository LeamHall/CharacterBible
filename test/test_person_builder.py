# name:     test_person_builder.py
# version:  0.0.1
# date:     20211225
# author:   Leam Hall
# desc:     test person_builder


from person import Person
from person.person_builder import PersonBuilder

def test_create_basic():
  b = Person()
  pb  = PersonBuilder()
  p   = pb.set_data(b)
  assert isinstance(p, Person)

def test_basic_person():
  boy         = Person()
  pb          = PersonBuilder()
  b = pb.set_data(boy)
  assert isinstance(b, Person)
  assert b.physical       == [ 'tall, dark haired, etc' ]
  assert b.mental         == { 'plot': 'success' }
  assert b.first_name     == 'John'
  assert b.last_name      == 'Dough'
  assert b.gender         == 'm'
  assert b.birth_info     == { 'year': 1234, 'day': 56 }
  assert b.notes          == ''
  assert b.relationships  == {}
  assert b.cultures       == []

def test_built_person():
  girl  = Person()
  data  = { 'physical' : ['short'], 'mental' : { 'plot': 'career' },
          'first_name' : 'Jane', 'last_name' : 'Dont', 'gender' : 'f', 
          'birth_info' : { 'year': 1236, 'day': 56 },
          'notes' : 'calm', 'relationships' : { 'sister': 'Susie'}, 
          'cultures' : ['rural'] }
  pb    = PersonBuilder()
  g     = pb.set_data(girl, data)
  assert g.physical       == [ 'short' ]
  assert g.mental         == { 'plot':'career' }
  assert g.first_name     == 'Jane'
  assert g.last_name      == 'Dont'
  assert g.gender         == 'f'
  assert g.birth_info     == { 'day': 56, 'year': 1236 }
  assert g.notes          == 'calm'
  assert g.relationships  == { 'sister': 'Susie' }
  assert g.cultures       == [ 'rural' ]
