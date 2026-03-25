#A-C
grades = []
total = 0
grades.append(92)
grades.append(51)
grades.append(83)
grades.append(37)   
grades.append(72)

print(grades)
#D
for i in range(len(grades)):
    total += grades[i]
print("The total of the grades is", total )

#E-F
print("The average grade is", sum(grades) / len(grades))   

grades.pop(1) #removes the second grade (51)
grades.remove(37) #removes the grade 37
print("Updated list", grades)
print("The new average grade is", round(sum(grades) / len(grades), 2))




