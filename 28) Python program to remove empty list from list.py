a = [1,2,[3,4],[],7,90,[],[4,5],45,[]]
print("your original list is :- ",a)
for i in a:
    if i == []:
        a.remove(i)
print("After removing empty list :- ",a)

#By another method if we want to remove all the list from list
print("By another method")
b = [1,2,[3,4],[],7,90,[],[4,5],45,[]]
print("Given list is :- ",b)
dummy = []
for x in b:
    if type(x) == list:
        dummy.append(x)
print(dummy)