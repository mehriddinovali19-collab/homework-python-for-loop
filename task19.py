n = int(input("Nechta son kiritasiz? "))
max_num = None
for i in range(n):
    num = int(input(f'{i+1} - sonni kiriting: '))

    if max_num is None or num > max_num:
        max_num =num
print("The largest number: ", max_num )
        
        
    