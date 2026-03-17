n = 7
total = 0
for i in range(1,n+1):
    age = int(input(f'{i} - Enter age of student:'))
    if age < 21:
        total += 1

print("Your age under than 21:", total)
