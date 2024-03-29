# name:     test_person_builder.py
# version:  0.0.1
# date:     20211225
# author:   Leam Hall
# desc:     test person_builder

import pytest

from app.person import Person
from app.person.person_builder import PersonBuilder


def test_create_basic():
    b = Person()
    pb = PersonBuilder()
    p = pb.gen_data(b)
    assert isinstance(p, Person)


def test_basic_person():
    boy = Person()
    pb = PersonBuilder()
    b = pb.gen_data(boy)
    assert isinstance(b, Person)
    assert b.idx == -1
    assert b.first_name == "John"
    assert b.last_name == "Dough"
    assert b.gender == "m"
    assert b.birthdate == 1234056
    assert b.notes == ""


def test_generated_person():
    girl = Person()
    data = {
        "first_name": "Jane",
        "last_name": "Dont",
        "gender": "f",
        "birthdate": 1236056,
        "notes": "calm",
    }
    pb = PersonBuilder()
    g = pb.gen_data(girl, data)
    assert g.first_name == "Jane"
    assert g.last_name == "Dont"
    assert g.gender == "f"
    assert g.birthdate == 1236056
    assert g.notes == "calm"


def test_existing_person_data():
    girl = Person()
    data = {"first_name": "Susie", "last_name": "Dont", "idx": 867}
    pb = PersonBuilder()
    g = pb.set_data(girl, data)
    assert g.idx == 867
    assert g.first_name == "Susie"
    assert g.last_name == "Dont"
