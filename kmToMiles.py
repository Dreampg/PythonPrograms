def miles(y):
    fact= 0.621371
    m= y* fact
    return(m)
km= float(input("enter the distance in kilometers: "))
print("the distance in miles are: ",miles(km))