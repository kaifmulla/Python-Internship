#By using min function
a = [1,2,3,4,5,6,7,0,8]
largest = max(a)
print(f"minimum element is {largest}")

#By using sort function
a = [1,2,3,4,5,6,7,0,8]
a.sort()
largest = a[-1]
print(f"minimum element is {largest}")

#By using loop
lst = [43,23,54,86,12,67,86,2]
print("Your list is :- ",lst)
largest = lst[0]
for i in lst:
    if i > largest:
        largest = i
print(f"{largest} is the smallest element in the list")


        
