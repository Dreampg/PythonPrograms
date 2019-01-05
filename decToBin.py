
def binary(x):
    if(x>0):
        q=x
        binary(q//2)
        remainder= x%2
        x=x//2
        global s
        if(remainder==0):
            print('0',end="")
        else:
            print('1',end="")

x=int(input("enter the number"))
binary(x)