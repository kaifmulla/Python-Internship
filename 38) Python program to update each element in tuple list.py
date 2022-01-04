l = [(1,2,3),(4,5,6),(8,9,0)]
print(f"Your list is :- {l}")
a = int(input("Enter value which you want to update in tuple list :- "))
c = []
s = 0
ans = []
for i in l:
    if type(i) == tuple:
        i = list(i)
        c = []
        for j in i:
            s = j + a
            c.append(s)
        p = tuple(c)
        ans.append(p)
print("Your updated list is :- ")
print(ans)
        