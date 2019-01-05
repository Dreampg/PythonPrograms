import cmath
def solve(a,b,c):
    d=(b**2)-(a*4*c)
    sol1=(-b+cmath.sqrt(d))/(2*a)
    sol2=(-b-cmath.sqrt(d))/(2*a)
    return(sol1,sol2)

a=float(input("enter a: "))
b=float(input("enter b: "))
c=float(input("enter c: "))
print("solutions are ",solve(a,b,c))