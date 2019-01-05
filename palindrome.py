s= input("enter the string")
if(len(s)==0):print("string is empty")
else:
    reverse=s[::-1]
    
if(s==reverse):
    print("palindrome")
else:
    print("not palindrome")
    