#By using min and max function
print("By using min max function")
t = (1,2,3,4,5,6,1)
print(min(t))
print(max(t))

#by using loop
print("By using loop")
t = (1,2,3,4,5,6,7,8,9)
s = t[0]
g = t[0]
for i in t:
    if i < s:
        s = i
    if i > g:
        g = i
print(f"minimum is :- {s}")
print(f"maximun is :- {g}")

#count particular element 
print("Count occurences of particular element")
print("By using count function")

t = (1,2,3,4,5,6,7,8,9,1)
i = int(input("Enter the element which you want to count:- "))
print(t.count(i))

#by using loop
print("By using loop")
count = 0
for x in t:
    if i == x:
        count = count + 1
print(f"Your entered element is occured {count} times")



