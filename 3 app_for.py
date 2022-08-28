# {%for <expression>}}
# <loop code>
# {%endfor%}


from jinja2 import Template

cities = [{'id': 1, 'city': 'Berlin'},
          {'id': 4, 'city': 'Hanover'},
          {'id': 6, 'city': 'Odessa'},
          {'id': 8, 'city': 'Munich'},
          {'id': 9, 'city': 'Frankfurt'}]


link = '''<select name='cities'>
{% for c in cities %}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor %}
</select>
'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)

print('#'*100)

# -%} minus remove all unnecessary spaces and tabs in the template:
link = '''<select name='cities'>
{% for c in cities -%}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor -%}
</select>
'''

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
