n = 5
total = 0
for i in range(1, n+1):
    age = float(input(f'{i} - age of student in class: ' ))
    total += age
    average_age = total/5

print(average_age)