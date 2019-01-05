

s=input("input the string: ")
new=""
for i in s:
    if i not in """!@#$%^&*()_-+=~`:;<>,.?/"'|\{}[]""":
        new=new + i
    
print(new)