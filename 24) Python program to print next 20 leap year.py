cyr = 2021
count = 0

while count <= 19:
    if cyr % 4 == 0 and (cyr % 100 != 0 or cyr % 400 == 0):
        print(cyr)
        count = count + 1
    cyr = cyr + 1




