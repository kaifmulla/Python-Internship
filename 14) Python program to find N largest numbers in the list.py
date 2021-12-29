a = [12,78,32,893,234,10,894,677]
n = int(input("How many largest no do you want from the list"))
x = 0
fl = 0
while x < n:
    fl = 0
    for i in a:
        if i > fl:
            fl = i
    a.remove(fl)
    print(fl)
    x = x + 1
print(a)