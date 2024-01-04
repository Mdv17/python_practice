people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "RavenClaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)