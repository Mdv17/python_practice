people = dict()
#you can also do it like this ~ people = {}
#Same as lists you can do it like this: people = list()

people = {
    "Carter": "+27610226642",
    "David": "+2634666777"
}

name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")