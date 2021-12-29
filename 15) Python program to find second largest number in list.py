a = [1,2,3,4,5,6,7]
firstlargest = 0
secondlargest = 0
for i in a:
    if i > firstlargest:
        secondlargest = firstlargest
        firstlargest = i
    elif i > secondlargest:
        secondlargest = i
print(f"First Largest :- {firstlargest}")
print(f"Second Largest :- {secondlargest}")

