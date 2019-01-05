lower=int(input("entyer lower limit"))
upper=int(input("enter upper limit"))
print("multiplication table")
for i in range(lower,upper+1):
    for j in range(1,11):
        mul=i*j
        print(i,"*",j,"=",mul)
