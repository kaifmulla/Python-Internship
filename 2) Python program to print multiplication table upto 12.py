# Python program to print multiplication table upto 12
n = 13
for i in range(1,n):
    print("")
    for j in range(1,11):
        print("%-5d X %5d = %5d" % (i, j, i * j))
        #print(i*j,end = " ")
        #print('\t')
print('\t')