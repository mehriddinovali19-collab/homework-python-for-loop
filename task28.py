score = int(input("1 - score of student: "))

min_score = score
max_score = score 

for i in range(2, 6):
    score = int(input(f'{i} - score of student: '))
    if score > max_score:
        max_score = score
    if score < min_score:
        min_score = score
print(f'Maximum: {max_score}, Minimum: {min_score}')
