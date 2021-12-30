# name:     person_builder.py
# version:  0.0.1
# date:     20211225
# author:   Leam Hall
# desc:     Build a person.

from person import Person

class PersonBuilder:

  def set_data(self, person, data = {}):
    person.idx        = data.get('idx',         -1)
    person.gender     = data.get('gender',      '')
    person.first_name = data.get('first_name',  '')
    person.last_name  = data.get('last_name',   '')
    person.birth_info = data.get('birth_info',  0)
    person.notes      = data.get('notes',       '')
    return person

  def gen_data(self, person, data = {}):
    person.gender        = data.get('gender',        self.gen_gender())
    person.first_name    = data.get('first_name',    self.gen_firstname(person.gender))
    person.last_name     = data.get('last_name',     self.gen_lastname())
    person.birth_info    = data.get('birth_info',    self.gen_birthinfo()) 
    person.notes         = data.get('notes',         '')
    return person

  def gen_firstname(self, gender):
    return 'John'

  def gen_lastname(self):
    return 'Dough'  

  def gen_birthinfo(self):
    return {'year' : 1234, 'day': 56 }

  def gen_gender(self):
    return 'm'

  def return_person(self):
    return self.person

