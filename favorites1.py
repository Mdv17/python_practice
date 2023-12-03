import csv

with open("favorites.csv", "r") as files:
    reader = csv.reader(files)
    for row in reader:
        favorite = row[1]
        print(favorite)