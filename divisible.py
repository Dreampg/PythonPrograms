def divide(x,y):
    if(y==0):print("division is not possible")
    elif(x%y!=0): print("not divisible")
    else: print("division is possible")
a= int(input("enter the first number"))
b= int(input("enter the second number"))
divide(a,b)