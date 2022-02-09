select 
  p.f_name,
  p.l_name,
  (SELECT sl.skill FROM skill_list sl WHERE psl.skill_idx = sl.idx) as skill_name,
  psl.skill_level
  
from people p left outer join people_skill_level psl on p.idx = psl.people_idx;


