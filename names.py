#Linear Search in Python
import sys

names = ["Biil", "Charlie", "Bob", "Mike", "Max", "Clara", "George"]

name = input("Name: ")

for n in names:
    if name == n:
        print("Found")
        sys.exit(0)

print("Not Found")
sys.exit(1)