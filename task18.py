start = 1
stop = int (input("stop: "))
step = 2
total = 0
for i in range(start, stop+1, step):
    total += i
    print(f'{i}: {total}')
