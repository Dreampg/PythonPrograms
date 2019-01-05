def hcf(x,y):
    if(x<y):smaller=x
    else:smaller=y
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    return(hcf)

a= int(input("enter the first number: "))
b= int(input("enter the second number: "))
print("hcf of ",(a,b)," is ",hcf(a,b))