person = {"name" : "John", "gender" : "male", "age" : 21, "address" : "17 mastiff, Johannesburg", "phone" : +27783490625}

key = input("What information do you want to know about the person? "). lower()

result = person.get(key, "This information is not available try something else")

print(result)
