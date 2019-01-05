a=0
b=1
s=0
def f(x):
    if(x>=1):
        global s,a,b
        f(x-1)
        s=a+b
        a=b
        b=s
        print(s)

length= int(input("enter the number of terms"))
print("fabonacci series is: ")
print(a)
print(b)
f(length-2)