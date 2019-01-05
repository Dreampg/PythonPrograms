def square(x):
    y= x**2
    return y

x= int(input("enter the limit"))
for i in range(0,x):
    print("square of ",i," is ",square(i))