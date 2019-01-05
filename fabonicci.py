a=0
b=1
y=int(input("enter the no of terms"))
if y<=0:
    print("entr a positive no")
elif y==1 :
    print('fabonicci sereis is',a)
else:
    print("fabonicci of ",y," terms is\n ",0,"\n",1)
    for i in range(0,y-2):
        
        fab= a+b
        a=b
        b=fab
        print(fab)
        