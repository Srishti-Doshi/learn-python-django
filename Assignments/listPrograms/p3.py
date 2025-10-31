# Extract list elements with Frequency greater than K

lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5 ,5, 6, 6, 6, 6, 6, 6, 6, 6,]
templst = []
finallst = []
k = 2

for i in lst:
    count = lst.count(i)
    if count > k:
        templst.append(i)

for i in templst:
    if i not in finallst:
        finallst.append(i)

print(finallst)