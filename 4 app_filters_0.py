# sum - get sum of collection
# sum(iterable, attribute=None, start=0)
from jinja2 import Template

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17000},
    {'model': 'Volvo', 'price': 44000},
    {'model': 'Volkswagen', 'price': 21000}
]

tpl = "sum price for all cars is {{ cs | sum(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)


tpl = "max price for all cars is {{ cs | max(attribute='price') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)


tpl = "max price for all cars is {{ (cs | max(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)


tpl = "min price for all cars is {{ (cs | min(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

tpl = "random price for all cars is {{ cs | random }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)


tpl = "Replace o to O: {{ cs | replace('o', 'O') }}"
tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)
