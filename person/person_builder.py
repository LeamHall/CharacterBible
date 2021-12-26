# name:     person_builder.py
# version:  0.0.1
# date:     20211225
# author:   Leam Hall
# desc:     Build a person.

from person import Person

class PersonBuilder:

  def set_data(self, person, data = {}):
    person.gender        = data.get('gender',        self.gen_gender())
    person.physical      = data.get('physical',      self.gen_physical())
    person.mental        = data.get('mental',        self.gen_mental())
    person.first_name    = data.get('first_name',    self.gen_firstname(person.gender))
    person.last_name     = data.get('last_name',     self.gen_lastname())
    person.birth_info    = data.get('birth_info',    self.gen_birthinfo()) 
    person.notes         = data.get('notes',         '')
    person.relationships = data.get('relationships', {})
    person.cultures      = data.get('cultures',      [])
    return person

  def gen_firstname(self, gender):
    return 'John'

  def gen_lastname(self):
    return 'Dough'  

  def gen_birthinfo(self):
    return {'year' : 1234, 'day': 56 }

  def gen_mental(self):
    mental = { 'plot':'success'}
    return mental

  def gen_physical(self):
    return ['tall, dark haired, etc']

  def gen_gender(self):
    return 'm'

  def return_person(self):
    return self.person

