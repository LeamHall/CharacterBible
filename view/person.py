# name:     view/person.py
# version:  0.0.1
# date:     20211224
# author:   Leam Hall
# desc:     Formatting data for various output types.

from string import Template

def to_text(data):
  t = Template('$who kissed $whom')
  return t.substitute(data)

def to_html(data):
  t = Template('<p>$who really kissed $whom!</p>')
  return t.substitute(data)

def char_string(data, output_type = 'text'):
  if output_type    == 'html':
    out_str = to_html(data)
  elif output_type  == 'text':
    out_str = to_text(data)
  else:
    raise ValueError("Unknown output type")
  return out_str

