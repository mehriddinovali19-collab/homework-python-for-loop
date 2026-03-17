start = int(input("start: "))
stop = 15
step = 1
if start > stop:
    step = -1
    for i in range(start, stop-1, step):
        print(i)
else:
    for i in range(start, stop +1, step):
     print(i)
    