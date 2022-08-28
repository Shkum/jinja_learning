from jinja2 import Template

name = 'Serg'
age = 28


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


per = Person('Serg', 42)

tm = Template("My name is {{p.name}} and and Im {{p.age}} years old - using class")
msg = tm.render(p=per)

print(msg)

tm = Template("My name is {{p.getName()}} and and Im {{p.getAge()}} years old - using getter")
msg = tm.render(p=per)

print(msg)


per = {'name': 'Serg', 'age': 43}

tm = Template("My name is {{p.name}} and and Im {{p['age']}} years old - using dict")
msg = tm.render(p=per)
print(msg)



