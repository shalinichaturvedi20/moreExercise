list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
i=0
z=[]
while i<len(list1):
    c=list1[i]
    if c in list1:
        z.append(c)
    i=i+1 
print(z)       




