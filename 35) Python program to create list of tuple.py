#Python program to create list of tuple from given list having  number and its cube in each tuple
l = [1,2,3]
res = []
for i in l:
    v = i * i * i
    res.append((i,v))
print(res)


#by using pow function and list comprehension method
l = [2,3,4]
res1 = []
res1 = [(i,pow(i,3)) for i in l]
print(res1)