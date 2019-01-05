x=int(input("enter the number greater than 2: "))
flag=0
for i in range(2,x):
    if x%i==0:
        print("number is not prime")
        flag=1
        break
        
   
if(flag==0):
    print("number is prime")        