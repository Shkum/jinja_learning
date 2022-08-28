from jinja2 import Template

persons = [
    {"name": "Alex", "old": 18, "weight": 78.5},
    {"name": "Serg", "old": 20, "weight": 83.7},
    {"name": "Nik", "old": 33, "weight": 94.0}
]


html = '''
{% macro list_users(list_of_user) -%}
<ul>
{% for u in list_of_user -%}
<li>{{u.name}}
{%- endfor %}
</ul>
{%- endmacro %}
{{list_users(users)}}
'''



tm = Template(html)
msg = tm.render(users=persons)

print(msg)
