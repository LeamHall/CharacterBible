#!/usr/bin/env python3

import random

def one_die(max):
  return random.randint(1,max)

def roll_stat():
  return one_die(6) + one_die(6) + one_die(6)

def make_char(stats, preferred, mins):
  rolls = []
  stat_list = list(stats.keys())
  for s in range(1,6):
    rolls.append(roll_stat())
  rolls.sort(reverse=True)
  for stat in preferred:
    stats[stat] = rolls.pop(0)
    stat_list.remove(stat)
  for stat in mins:
    stats[stat] = max(stats[stat], mins[stat])
    if stat in stat_list:
      stat_list.remove(stat)
  for stat in random.sample(stat_list, len(stat_list)):
    stats[stat] = rolls.pop(0)
    stat_list.remove(stat)
    
  return stats

# For a 3d6 OGL type game
stats = { 'Strength': 0, 'Intelligence': 0, 'Wisdom': 0, 'Dexterity': 0, 'Constitution': 0, 'Charisma': 0}

# Sample character class minimums
mins  = { 'Strength': 15, 'Wisdom': 15, 'Charisma': 15 }

# Sample preferred stats, in highest to lowest order
preferred = ['Charisma', 'Wisdom']

char_stats = make_char(stats, preferred, mins)
print(char_stats)
