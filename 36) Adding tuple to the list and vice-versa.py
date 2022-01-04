#Adding tuple to the list..
l = [98,87,76,65]
a = (1,2,3,4)
b = (12,34,45,56)
l = l + list(a)
print(l)

#Adding list to the tuple..
print("Adding list to the tuple")
l = [1,2,3]
t = (4,5,6)
res = tuple(l + list(t))  #Here we have done typecasting of tuple to list and list to tuple
print(res)