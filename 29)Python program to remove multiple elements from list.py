a = [1,2,3,2,3,3,4,4,4,5,6,7,7,7,8]
c = []
for i in a:
    if i not in c:          #(not in) is used to remove duplicate here 
        c.append(i)
print(c)

    
 #Another example of removing  multiple elements from list    
print("Another example of removing  multiple elements from list") 
y = [1,2,3,2,3,3,4,4,4,5,6,7,7,7,7,8]
n = int(input("How many elements do you want to remove from list :- "))
x = []
dummy = []
for i in range(0,n):
    d = int(input("Enter which elements :- "))
    dummy.append(d)
print(dummy)

for i in y:
    print(i,end = " ")
    if i not in dummy:
        x.append(i)
print(x)