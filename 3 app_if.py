# {% if <condition> %}
# <code if condition>
# {% endif %}

# {%for <expression>}}
# <loop code>
# {%endfor%}

from jinja2 import Template

cities = [{'id': 1, 'city': 'Berlin'},
          {'id': 4, 'city': 'Hanover'},
          {'id': 6, 'city': 'Odessa'},
          {'id': 8, 'city': 'Munich'},
          {'id': 9, 'city': 'Frankfurt'}]

# -%} minus remove all unnecessary spaces and tabs in the template (before or after code):
link = '''<select name='cities'>
{% for c in cities -%}
{% if c.id > 6 -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% else -%}
{{c.city}}
{% endif -%}
{% endfor -%}
</select>
'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)

