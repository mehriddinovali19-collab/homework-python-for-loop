N = int(input("How many products: "))

total = 0
for i in range(1, N+1):
    price = float(input(f'{i}- price of product:' ))
    discount_price = price * 0.9
    total += discount_price

print("After the discount price: ", total)
