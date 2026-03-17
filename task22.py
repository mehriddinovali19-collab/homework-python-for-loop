num = 5 
min_price = float("inf")
max_price = float("-inf")
for i in range(1, num +1):
    price = int(input(f'{i} - price of phone: '))
    if min_price > price:
        min_price = price 
    if max_price < price:
        max_price = price 
average_price = (max_price + min_price)/2
print(f'Minimum price of phone: {min_price}')
print(f'Maximum price of phone: {max_price}')
print(f'average price of min and max: {average_price}')
