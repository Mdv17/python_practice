months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
bday = input("Write your birthday in this format 'DD-MM-YYYY' : ")
index = int(bday[3:5]) - 1

print("You were born in", months[index])
