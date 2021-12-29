a = "mohammad"
b = len(a)//2
for i in range(len(a)):
    if i < b:
        print(a[i].upper(),end = "")
    else:
        print(a[i],end = "")

#By another method
print("By another method")
strr = "abcdef"
halfup = ""
for i in range(len(strr)//2):
    if strr[i] == strr[i].lower():
        halfup = halfup + strr[i].upper()
print(i)
halfup = halfup + strr[i+1:]
print(halfup)


