import csv

with open("favorites.csv", "r") as files:
    reader = csv.reader(files)
    next(row)   #This line will cause to omit the header file 
    for row in reader:
        print(row[1])