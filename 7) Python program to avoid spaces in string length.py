c = input("Enter the string :- ")
a = len(c)
print(f"Length of original string is :- {a}")
count =  0
for i in range(a):
    if c[i] != " ":
        count = count + 1
print(f"Avoiding spaces the length of string is :- {count}")
