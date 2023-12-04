#!/usr/bin/env python

from pydantic import BaseModel
from typing import Optional


class Team(BaseModel):
    designation: str  # 2/1/1 is 2nd Platoon, 1st Squad, 1st FireTeam
    size: str
    morale: Optional[int]
    members: list


class Member(BaseModel):
    rank: str
    f_name: str
    l_name: str
    nick: Optional[str] = None
    upp: str
    gender: str
    morale: int


class Unit(BaseModel):
    name: str
    co: Member
    xo: Member
    org: dict


def write_unit(u):
    unit_string = f"{u.name}\n"
    unit_string += f"CO: {write_member(u.co)}\n"
    unit_string += f"XO: {write_member(u.xo)}\n"

    for t in ["s2", "s6", "2_1_1"]:
        unit_string += f"\n{write_team(u.org[t])}"

    return unit_string


def write_member(m):
    f_string = f"{m.rank} {m.f_name} "
    if m.nick:
        f_string += f"'{m.nick}' "
    f_string += f"{m.l_name} [{m.gender.upper()}] {m.upp} Morale: {m.morale}"
    return f_string


def write_team(t):
    morale_total = 0
    members_string = ""
    for m in t.members:
        members_string += f" {write_member(m)} \n"
        morale_total += m.morale
    team_morale = round(morale_total / len(t.members))
    team_string = f"{t.size}: {t.designation} Morale: {team_morale}\n"
    team_string += f"{members_string}"
    return team_string


data = {
    "rank": "CPT",
    "f_name": "Jakob",
    "l_name": "Domici",
    "upp": "7ABC56",
    "gender": "m",
    "morale": 15,
}
jakob = Member(**data)
data = {
    "rank": "LT",
    "f_name": "Liv",
    "l_name": "Ellis",
    "upp": "777777",
    "gender": "f",
    "morale": 10,
}
liv = Member(**data)
data = {
    "rank": "SGT",
    "f_name": "Beauregard",
    "l_name": "Dawson",
    "nick": "Beau",
    "upp": "A78487",
    "gender": "m",
    "morale": 10,
}
beau = Member(**data)
data = {
    "rank": "PVT",
    "f_name": "George",
    "l_name": "Ginger",
    "nick": "George",
    "upp": "696673",
    "gender": "m",
    "morale": 10,
}
george = Member(**data)
data = {
    "rank": "PVT",
    "f_name": "Lovena",
    "l_name": "Arcman",
    "nick": "Love",
    "upp": "578898",
    "gender": "f",
    "morale": 10,
}
love = Member(**data)

data = {
    "rank": "CWO",
    "f_name": "Freya",
    "l_name": "Ingridsdottir",
    "upp": "777777",
    "gender": "f",
    "morale": 13,
}
freya = Member(**data)

data = {
    "rank": "COL",
    "f_name": "Frank",
    "l_name": "Cross",
    "upp": "777777",
    "gender": "m",
    "morale": 13,
}
frank = Member(**data)
data = {
    "rank": "LT",
    "f_name": "FNU",
    "l_name": "Voss",
    "upp": "777777",
    "gender": "m",
    "morale": 10,
}
voss = Member(**data)

s2_data = {"designation": "S2", "members": [liv], "size": "Section"}
s2 = Team(**s2_data)
s6_data = {"designation": "S6", "members": [freya], "size": "Section"}
s6 = Team(**s6_data)


jakob_team_data = {
    "designation": "2/1/1",
    "members": [jakob, beau, george, love],
    "size": "FireTeam",
}
jakob_team = Team(**jakob_team_data)

semc_org = {"2_1_1": jakob_team, "s2": s2, "s6": s6}
semc_data = {"name": "SEMC", "co": frank, "xo": voss, "org": semc_org}
semc = Unit(**semc_data)

print(write_unit(semc))
