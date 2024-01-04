people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "RavenClaw"},
    {"name": "Draco", "house": "Slytherin"}
]

# lambda input: output
people.sort(key=lambda person: person["name"])

print(people)