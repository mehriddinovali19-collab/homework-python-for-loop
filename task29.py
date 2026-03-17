n = int(input("Enter number of sales points: "))

total = 0
for i in range (1, n+1):
  revenue = float(input(f"{i} - Enter revenue for sales point: "))
  total += revenue

average = total /n


print(f"Average revenue: {average}")