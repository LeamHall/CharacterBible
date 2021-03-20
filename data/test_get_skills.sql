SELECT DISTINCT skill, level
FROM skills, peopleskills
WHERE peopleskills.skill_id = skills.id
  AND peopleskills.people_id = 123

;
