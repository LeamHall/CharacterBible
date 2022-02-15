# name:     view/person.py
# version:  0.0.2
# date:     20220214
# author:   Leam Hall
# desc:     Formatting data for various output types.

## CHANGELOG
#   20220214  Working on a link for html output.

def make_name(data):
  name = ''
  if data.first_name:
    name += data.first_name + ' '
  if data.middle_name:
    name += data.middle_name + ' '
  if data.last_name:
    name += data.last_name
  return name.strip()
 
def make_gender(data): 
  if data.gender:
    return data.gender.upper()
  else:
    return ''

def to_csv(data):
  string = (
    f"{data.idx}|{data.last_name}|{data.first_name}|{data.middle_name}|"
    f"{data.gender}|{data.birthdate}|{data.plot}|{data.temperament}|"
    f"{data.notes}"
  )
  return string

def to_text(data):
  name    = make_name(data)
  gender  = make_gender(data)
  string  = (
    f"{data.idx} {name} [{gender}]\n"
    f"Birthdate: {data.birthdate}\n"
    f"Plot: {data.plot}\n"
    f"Temperament: {data.temperament}\n"
    f"Notes: {data.notes}\n" 
  )
  return string

def to_html(data, idx):
  name    = make_name(data)
  gender  = make_gender(data)
  if idx:
    string  = (
      f"<p>{data.idx} {name} [{gender}]</p>\n"
      f"<p>Birthdate: {data.birthdate}</p>\n"
      f"<p>Plot: {data.plot}</p>\n"
      f"<p>Temperament: {data.temperament}</p>\n"
      f"<p>Notes: {data.notes}</p>\n"
    )
  else:
    string = f"<p><a href=\"people/{data.idx}\">{data.idx}</a> {name} [{gender}]</p>"
  return string

#def char_string(data, output_type = 'text'):
def char_string(data, output_type, idx):
  if output_type    == 'html':
    out_str = to_html(data, idx)
  elif output_type  == 'text':
    out_str = to_text(data)
  elif output_type  == 'csv':
    out_str = to_csv(data)
  else:
    raise ValueError("Unknown output type")
  return out_str

