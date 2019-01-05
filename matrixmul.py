#matrix 1
a1=int(input("enter rows for matrix 1"))
b1=int(input("enter column for matrix 1"))
m1=[]
for i in range(0,a1):
    m1.append([])
for i in range(0,a1):
    for j in range(0,b1):
        m1[i].append(j)
        m1[i][j]=int(input())
print(m1)
#matrix 2
a2=int(input("enter rows"))
b2=int(input("enter column"))
m2=[]
for i in range(0,a2):
    m2.append([])
for i in range(0,a2):
    for j in range(0,b2):
        m2[i].append(j)
        m2[i][j]=int(input())
print(m2)
#multiplication
add=0
for i in range(0,a1):
    for j in range(0,b2):
        for k in range(0,a2):
            add=add+m1[i][k]*m2[k][j]
        m2[i][j]=add
        add=0
for i in range(0,a2):
    for j in range(0,b2):
        print(m2[i][j],end="  ")


