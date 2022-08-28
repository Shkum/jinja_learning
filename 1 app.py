from jinja2 import Template

name = 'Serg'
age = 28

tm = Template("Hello {{name}}")
msg = tm.render(name=name)
print(msg)

tm = Template("My name is {{a}} and and Im {{b}} years old")
msg = tm.render(a=name, b=age)
print(msg)
