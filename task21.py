N = int(input("Nechta son kiritasiz? "))

even_sum = 0
odd_sum = 0

for i in range(1, N+1):
   if i % 2 ==0:
    even_sum += i

   else:
    odd_sum += i
    
print(f"Even: {even_sum}, Odd: {odd_sum}")

    