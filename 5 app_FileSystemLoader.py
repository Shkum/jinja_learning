from jinja2 import Environment, FileSystemLoader

persons = [
    {"name": "Alex", "old": 18, "weight": 78.5},
    {"name": "Serg", "old": 20, "weight": 83.7},
    {"name": "Nik", "old": 33, "weight": 94.0}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons)

print(msg)
