a = [1,2,3,4,5,6,7]
b = []
b = a
print(b)

#Another method using for loop
lst = [9,7,6,5,4,3,2]
cp = []
for i in range(len(lst)):
    cp.append(lst[i])               #here we are just appending the single element in empty list
print(cp)