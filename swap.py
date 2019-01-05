def swap(x,y):
    x,y=y,x
    return(x,y)
x=float(input("enter the number"))
y=float(input("enter the number"))
print("Before swap","x= ",x," y ",y)

print("After swap","x,y are: ",swap(x,y))