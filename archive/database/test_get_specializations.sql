-- SELECT first_name, last_name, skill, peopleskills_specializations.level as SpecLevel, specialization 

-- FROM people, peopleskills, skills, specializations, peopleskills_specializations 

-- WHERE peopleskills.people_id = people.id 
--  AND peopleskills_specializations.level >= 0
--  AND peopleskills.skill_id = peopleskills_specializations.skill_id
--  AND peopleskills

SELECT DISTINCT first_name, skill, specialization

FROM people, skills, specializations, peopleskills_specializations

WHERE people.id = 123
  AND skills.id = peopleskills_specializations.skill_id
  AND specializations.id = peopleskills_specializations.specialization_id
--  AND people.id in ( SELECT people_id FROM peopleskills_specializations )
--  AND skills.id in ( SELECT skill_id FROM peopleskills_specializations )
;
