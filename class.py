# Creating our own data type like tuples, dictionary and lists
# a class is a template for a type of object

class Point():
    # self is for storing data inside itself
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(p.x)
print(p.y)