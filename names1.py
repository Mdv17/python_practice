#Linear Search in Python
import sys

names = ["Biil", "Charlie", "Bob", "Mike", "Max", "Clara", "George"]

name = input("Name: ")

if name in names:
    print("Found")
    sys.exit(0)
print("Not Found")
sys.exit(1)