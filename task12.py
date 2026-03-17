start = int(input("start: "))
stop =int(input("stop: "))
total = 0
for i in range(start, stop+1):
    total += i **3
    print(f'{i}: {total}')