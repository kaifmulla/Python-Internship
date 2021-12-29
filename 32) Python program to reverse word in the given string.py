str = input("Enter the word which you want to reverse :- ")
print(f"Your word is :- {str}")
rev = ""
for i in str:
    rev = i + rev
print(f"Your reverse word is :- {rev}")

#Using function also we can reverse the string

def reverse(s):                                  #while using function in program you must declare and give defination first i.e at start
    rev = ""
    for i in s:
        rev = i + rev
    return rev

s = input("Enter the value of another string :- ")
print(f"Your another entered string is :- {s}")

print("Your Reversed string is :- ")
print(reverse(s))

#Another method to reverse the string

print("Another Method to reverse the string")
st = input("Enter your string again :- ")
revers = ""
for i in range(len(st)):
    revers = revers + st[-(i+1)]
print(f"Your reversed string is :- {revers}")


