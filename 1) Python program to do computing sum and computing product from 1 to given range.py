# Python program that asks the user for a number n and gives them the possibility to choose the computing sum and computing the product of 1,2,3,.....n.
lst = []
n = int(input("Enter the value of n"))
sum = 0
mult = 1
for i in range(1,n+1):
    lst.append(i)

    sum = sum + i
    mult = mult * i
   
usrinp = int(input("Enter 1 for computing sum and 2 for computing product"))

if(usrinp==1):
    print(f"Sum is :- {sum}")
else:
    print(f"Multiplication is :- {mult}")






