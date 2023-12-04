#!/usr/bin/env python3

# name:     test_character_builder.py
# version:  0.0.2
# date:     20220212
# author:   Leam Hall
# desc:     Testing Character Builder
#
# CHANGELOG
#   20220212 Refactor to pytest

import pytest

from app.person import Person
from app.person import Character
from app.person import CharacterBuilder


def testCreation(cb):
    assert isinstance(cb, CharacterBuilder)


def testCreateName(amanda):
    assert amanda.first_name == "Amanda"
    assert amanda.last_name == "Lefron"


def testCreateStats(amanda):
    assert amanda.stats["soc"] == 12
    for s in amanda.stats.keys():
        assert amanda.stats[s] >= 2
        assert amanda.stats[s] <= 15
