def sqlist(a):
    ls = []
    for i in range(1,a+1):
        i = i * i
        ls.append(i)
    print(f"Your list is :- {ls}")


a = int(input("Till where you want the list of square :- "))
sqlist(a)