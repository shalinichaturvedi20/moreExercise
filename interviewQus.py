name=["shalini","neha","sagreeka","amisha",]
age=[20,21,19,23]
clas=["10th","12th","7th","9th"]
f={}
z=[]
i=0
while i<len(name):
    new={"name": name[i],"age":age[i],"clas":clas[i]}
    f.update(new)
    z.append(new)
    i=i+1
print(z)


num1={"a":200,"b":400,"c":600,"d":200,"g":100}
num2={"a":300,"b":500,"c":800,"e":300,"g":200}
for key in num1:
    if key in num2:
        num2[key]=num1[key]+num2[key]
    else:
        num2[key]=num1[key]
print(num2)            

 

