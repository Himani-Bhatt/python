x = int(input("enter first no:"))
y = int(input("enter second no:"))
print("1=add 2=sub 3=mul 4=div")
ch = int(input("enter your choice"))    
print("ans =")
if ch == 1:
	print(x + y)
	pass
elif ch == 2:
    print(x - y)
elif ch == 3:
    print(x * y)
elif ch == 4:
    print(x / y)
else:
    print("enter correct choice...!!!")            	