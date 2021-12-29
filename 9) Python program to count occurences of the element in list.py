a = [1,2,3,3,3,3,4,5,6,6,7]
key = int(input("Enter the element which you want to find no of occurences :- "))
count = 0
for i in range(len(a)):
    if a[i] == key:
        count = count + 1
if count == 0:
    print("Your entered element is not present in the list....")
else:
    print(f"your element {key} occurence is {count} times")

