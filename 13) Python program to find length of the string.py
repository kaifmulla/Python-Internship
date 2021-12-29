#By using len function
str = input("Enter the string :- ")
a = len(str)
print(f"Length of the entered string is :- {a}")


#By using loop
print("By using loop")
a = input("Enter the string again :- ")
count = 0
for i in a:
    count += 1
print(f"Length of the string is :- {count}")