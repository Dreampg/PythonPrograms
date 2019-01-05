terms= int(input("enter the number of terms"))
for i in range(0,terms):
    x= lambda i :2**i
    print("2 raised to the power ",i," is ",x(i))
    