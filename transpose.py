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
m2=[]
for i in range(0,a1):
    m2.append([])
for i in range(0,a1):
    for j in range(0,b1):
        m2[i].append(j)
        m2[i][j]=0
#transpose
for i in range(0,a1):
    for j in range(0,b1):
        m2[i][j]=m1[j][i]
print("transpose matrix is ")
print(m2)
