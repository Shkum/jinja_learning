from jinja2 import Template

persons = [
    {"name": "Alex", "old": 18, "weight": 78.5},
    {"name": "Serg", "old": 20, "weight": 83.7},
    {"name": "Nik", "old": 33, "weight": 94.0}
]

tpl = '''
{%- for u in users -%}
{% filter upper %}{{u.name}}{% endfilter %}
{% endfor %}
'''

tm = Template(tpl)
msg = tm.render(users=persons)

print(msg)
