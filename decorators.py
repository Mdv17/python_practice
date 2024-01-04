# Decorators are a way of taking a function and modifying a fuction. Adding some additional behavior to that function
# Decorators take function as input and returns a modified version of the function as output

# A function that modifies a function by announcing that the function is about to run and is done runnning

def announce(f):
    def wrapper():
        print("about to run the function..")
        f()
        print("Done with the function")
    return wrapper


@announce
def hello():
    print("Hello, World")

hello()