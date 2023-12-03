import csv

with open("favorites.csv", "r") as files:
    reader = csv.reader(files)
    for row in reader:
        print(row[1])