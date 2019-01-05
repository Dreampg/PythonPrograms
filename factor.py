def factor(x):
    if(x<=0):print("enter a positive number")
    elif(x==1):print("factor is 1")
    else:
        print("factors of ",x," are: ")
        for i in range(1,x+1):
            if(x%i==0): print(i,end=",")
    return("finish!!!!")

a= int(input("enter the number"))
factor(a)