from jinja2 import Environment, FileSystemLoader

link = '''<select name='cities'>
{% for c in cities %}
    <option value="{{c['id']}}">{{c['city']}}</option>
{% endfor %}
</select>
'''

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('page.html')
msg = tm.render(domain="https://proproprogs.ru/", title="About JINJA")

print(msg)
