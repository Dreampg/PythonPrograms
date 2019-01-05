a=0
b=1
l=int(input("enter limit of sreies"))
print("fibbonicci series is")
print(a)
print(b)
for i in range(0,l):
    s=a+b
    print(s)
    a=b
    b=s
