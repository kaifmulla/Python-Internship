def checkperfect(no):
    sum = 0
    for i in range(1,no-1):
        if no % i == 0:
            sum = sum + i
    if sum == no:
        return 1
    else:
        return 0


a = int(input("Enter the number which you want to check it is perfect or not :- "))
print("Entered number is :- ",a)
ans = checkperfect(a)
if ans == 1:
    print(f"{a} is a perfect no")
else:
    print(f"{a} is not a perfect number")



