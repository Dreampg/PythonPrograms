x=int(input("enter the first number"))
y=int(input("enter the second number"))
z=int(input("enter the third number"))

    
a=list((x,y,z))
a.sort()
for i in a:
    num=i
print('the largest of ',x,y,z," is ",num)    