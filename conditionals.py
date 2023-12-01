data_valid = False
while data_valid == False:
    grade1 = input("Type the grade of the first test: ")
    try:
        grade1 = float(grade1)
    except:
        print("Invalid number")
        continue
    if grade1 < 0 or grade1 > 10:
        print("Grades can't be less than zero and greater than ten")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    grade2 = input("Type the grade of the second test: ")
    try:
        grade2 = float(grade2)
    except:
        print("Invalid number")
        continue
    if grade2 < 0 or grade2 > 10:
        print("Grades can't be less than zero and greater than ten")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_classes = input("Type the total number of classes: ")
    try:
        total_classes = int(total_classes)
    except:
        print("Invalid number")
        continue
    if total_classes <= 0:
        print("Total classes shouldn't be less or equal to zero")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    absences = input("Type the number of absences: ")

    try:
        absences = int(absences)
    except:
        print("Invalid number")
        continue
    if absences > total_classes:
        print("Abscences cant be less than the total_classes")
        continue
    else:
        data_valid = True


avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ",round(avg_grade,2))
print("Attendance rate: ", str(round((attendance * 100),2)) + "%")

if (avg_grade >= 6):
    if(attendance >= 0.8):
        print("The student has been approved.")
    else:
        print("The student has failed due to low attendance.")

elif (attendance >= 0.8):
    print("The student has failed due to low average grade.")

else:
    print("The student has failed due to not meeting the requirements")
