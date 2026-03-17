
start = 1 
stop = int(input("stop: "))
step = +1
if start > stop:
    step = -1
total = 0
for i in range (start, stop, step):
    kv = pow(i, 2)
    total += kv


print(total)
