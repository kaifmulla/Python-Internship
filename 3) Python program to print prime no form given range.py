# Python program to print all prime no from given range
flag = 0
count = 0
for i in range(1,101):
    flag=0
    #d=2
    for d in range(2,i):
        if i%d == 0:
            flag = 1;
            break
    if flag == 0:
        print(i)
        count = count + 1
print(f"total prime nos are :- {count}")

