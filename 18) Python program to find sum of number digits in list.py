a = [12,23,34,65,43,32,82]
b = []
for i in range(len(a)):
    ts = 0
    while a[i] != 0:
        rem = a[i] % 10
        ts = ts + rem
        a[i] = a[i]//10
    b.append(ts)
print(b)
