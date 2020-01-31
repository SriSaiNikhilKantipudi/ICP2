n = int(input("Enter n value:"))
list = []       #initialized a list
i = 0
for i in range(n):
    x = int(input("Enter weight of student in lbs:"))
    list.insert(i, x)               #insert every student weight in lbs into list created
    list[i] = list[i] *0.45         #converted weight into kgs
print("Weight of students in kgs:", list)