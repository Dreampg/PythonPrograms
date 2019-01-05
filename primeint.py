f=1
lower=int(input("entyer lower limit"))
upper=int(input("enter upper limit"))
for i in range(lower,upper+1):
    f=1
    for j in range(2,i):
        if(i%j==0):
            f=0
            break
    if(f==1):
        print(i)
