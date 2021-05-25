def harshad_num(num):
    i=s=0
    n=num
    while num>i:
        rem=num%10
        s=s+rem
        num=num//10
    if (n%s==0):
        print(n,"is a harshad number")
    else:
        print(n,"is not a harshad number")
harshad_num(13)                
