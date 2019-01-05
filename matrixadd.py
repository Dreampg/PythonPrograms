a=int(input("enter rows"))
b=int(input("enter column"))
m=[]
for i in range(0,a):
    m.append([])
for i in range(0,a):
    for j in range(0,b):
        m[i].append(j)
        m[i][j]=int(input())
print(m)
add=0
for i in range(0,a):
    for j in range(0,b):
        add=add+m[i][j]
print("sum of elements of matrix=",add)
            
