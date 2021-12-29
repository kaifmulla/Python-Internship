str = input("Enter your string :- ")
print(f"Your string is :- {str}")
rev = "" 
for i in str:
    rev = i + rev
print(f"Reversed string is :- {rev}")

if str == rev:
    print("Your string is palindrome")
else:
    print("Your entered string is not palindrome")


