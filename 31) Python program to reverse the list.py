#Reversing the list with using the reverse function
a = [2,3,5,7,1]
a.reverse()
print(a)

#Reversing the list using loop

lst = [23,34,45,32,54,65,76]
print(lst)
b = []
for x in range(len(lst)-1,-1,-1):
    b.append(lst[x])                    #here we are appending the single single element in the list empty list b
print(b)
