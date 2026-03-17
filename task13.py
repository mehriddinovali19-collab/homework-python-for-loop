q_num =int(input("Qavat:"))

total = 0
for i in range(1,q_num+1):
    balandlik = float(input(f"{i}-qavat balandligini kiriting (metrda): "))

    total += balandlik

    print(total)