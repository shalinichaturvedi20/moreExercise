list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1]
i=0
z=[]
while i<len(list1):
    c=list1[i]
    if c  in list2:
        z.append(c)
    i=i+1 
print(z)   








