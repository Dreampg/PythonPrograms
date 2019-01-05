

a=int(input("enter the lower limit of interval"))
b=int(input("enter the upper limit of interval"))

for y in range(a,b):
    sum=0
    temp=y
    while temp>0:
        rm=temp%10
        sum=sum+ rm*rm*rm
        temp//=10
    if(y==sum):
        print(y," is armstrong.")
    