n = int(input("Nechta son kiritasiz? "))
min_num = float("inf")
max_num = float("-inf")
for i in range(n):
    num = int(input(f'{i+1} - Enter number: '))
    if min_num > num:
        min_num = num 
    if max_num < num:
            max_num = num 
average = (max_num + min_num)/2
print(f'Minimum number:   {min_num}')
print(f'Maximum number:   {max_num}')
print(f'Average of min and max:{average}')