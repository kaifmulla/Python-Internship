a = input("Enter the string :- ")
print("Enter which location character you want to remove :- ")
i = int(input())
b = ""
for x in range(len(a)):
    if x != i:
        b = b + a[x]
print(b)


