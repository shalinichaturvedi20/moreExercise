sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
split_value=[]
m=""
for c in sentence:
    if c=="":
        split_value.append(m)
        m=""
    else:
        m+=c
if m:
    split_value.append(m)
print(split_value)
