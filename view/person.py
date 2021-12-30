# name:     view/person.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Formatting data for various output types.

def to_text(data):
  string = "{} {} [{}]".format(data.first_name, data.last_name,
    data.gender.upper())
  return string

def to_html(data):
  string = "<p>{} {} [{}]</p>".format(data.first_name, data.last_name,
    data.gender.upper())
  return string
  
def char_string(data, output_type = 'text'):
  if output_type    == 'html':
    out_str = to_html(data)
  elif output_type  == 'text':
    out_str = to_text(data)
  else:
    raise ValueError("Unknown output type")
  return out_str

