# fact=int(input("enter the number"))
# i=0
# while i<fact:
#    if fact < 0:
#       print("it is factorial number")
#    elif fact == 0:
#       print("The factorial of 0 is 1")
#    else:
#       for i in range(1,fact + 1):
#          fact = fact*i
#       print("The fact of",fact,"is",fact)



num = int(input("enter a number: "))
fac = 1.
for i in range(1, num + 1):
    fac = fac * i
print("factorial of ", num, " is ", fac)   