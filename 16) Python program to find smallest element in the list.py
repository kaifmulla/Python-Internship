#By using min function
a = [1,2,3,4,5,6,7,0,8]
smallest = min(a)
print(f"minimum element is {smallest}")

#By using sort function
a = [1,2,3,4,5,6,7,0,8]
a.sort()
smallest = a[0]
print(f"minimum element is {smallest}")

#By using loop
lst = [43,23,54,86,12,67,86,2]
print("Your list is :- ",lst)
smallest = lst[0]
for i in lst:
    if i < smallest:
        smallest = i
print(f"{smallest} is the smallest element in the list")


        
