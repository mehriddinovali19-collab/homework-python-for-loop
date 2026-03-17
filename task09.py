total = 0
start = 2 
stop = 20
for i in range(start, stop+2, 2):
    total += i
    print(f'{i}: {total}')