# List product excluding duplicates
#find the product (multiplication result) of all the unique elements in a list.

# lst = [1, 2, 3, 4, 4, 1, 5]
lst = [1,2,3,4,3,2]
product = 1

templist = []

for i in lst:
    if i not in templist:
        templist.append(i)
        product = product * i

print(product)