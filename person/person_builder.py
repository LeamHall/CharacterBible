# name:     person_builder.py
# version:  0.0.1
# date:     20211225
# author:   Leam Hall
# desc:     Build a person.

from person import Person

class PersonBuilder:

  def __init__(self, data = {}):
    self.person = Person()
    self.set_data(data)


  def set_data(self, data):
    self.person.physical      = data.get('physical',      self.gen_physical())
    self.person.mental        = data.get('mental',        self.gen_mental())
    self.person.first_name    = data.get('first_name',    self.gen_firstname(self.person.gender))
    self.person.last_name     = data.get('last_name',     self.gen_lastname())
    self.person.gender        = data.get('gender',        self.gen_gender())
    self.person.birth_info    = data.get('birth_info',    self.gen_birthinfo()) 
    self.person.notes         = data.get('notes',         '')
    self.person.relationships = data.get('relationships', {})
    self.person.cultures      = data.get('cultures',      [])

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

