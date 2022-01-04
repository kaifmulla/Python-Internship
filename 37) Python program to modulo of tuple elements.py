t = (12,34,56,23)
t1 = (1,2,3,4)
res = []
res1 = ()

for i in range(len(t)):
    for j in range(len(t1)):
        if i == j:
            a = t[i] % t1[j]
            res.append(a)

res1 = tuple(res)
print(res)


#By another method
print("By another method..")
ans = tuple(s % k for s,k in zip(t,t1))
print(ans)