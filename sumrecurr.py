res=0
def add(x):
    if(x>0):
        add(x-1)
        global res
        res = res +x
    return(res)
    
x=int(input("enter the range: "))
print("addition of natural number from 1 to ",x," is ", add(x))
        