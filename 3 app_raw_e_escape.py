# raw - string inside of block raw is not modifying (ex.: not insert variable)

# e - filter for escaping (экранирование) of a string or special symbols

from jinja2 import Template
from markupsafe import escape

data = '''
Module JINJA instead
of variable {{ name }}
insert appropriate value
'''

tm = Template(data)
msg = tm.render(name='Serg')
print(msg)

data = '''{%raw%}
Module JINJA instead
of variable {{ name }}
insert appropriate value
{%endraw%}
'''

tm = Template(data)
msg = tm.render(name='Serg')
print(msg)


# at html tags link will be modified for link, to avoid it filter 'e' should be used
data = '''At HTML document links attributed (определяются) in following way
<a href="#">link</a>'''

tm = Template(data)
msg = tm.render()
print(msg)

print()
# example
# at html tags link will be modified for link, to avoid it filter 'e' should be used
data = '''At HTML document links attributed (определяются) in following way
<a href="#">link</a>'''

tm = Template('{{ data | e }}')
msg = tm.render(data=data)
print(msg)

print()
# simplify escaping (screening) using escape
msg = escape(data)
print(msg)
