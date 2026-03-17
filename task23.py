N = int(input("How many phones: "))

total = 0

for i in range(1, N+1):
    price = int(input(f'{i} - price of phone: '))
    if price % 5 ==0:
        total += price
print("Sum:", total)
