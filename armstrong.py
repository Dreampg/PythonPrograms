

y=int(input("enter  a number "))
sum=0
temp=y
while temp>0:
    rm=temp%10
    sum=sum+ rm*rm*rm
    temp//=10
if(y==sum):
    print("number is armstrong")
else:
    print("no. is not armstrong")