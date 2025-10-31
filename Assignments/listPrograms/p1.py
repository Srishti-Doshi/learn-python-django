# Count unique items in a list

lst = [1, 1, 2, 3 , 4, 5, 7, 3, 5]
templist = []

for i in lst:
    if i not in templist:
        templist.append(i)

print("unique items in lst is ",len(templist))