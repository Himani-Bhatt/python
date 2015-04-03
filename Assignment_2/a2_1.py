ch = input("enter choice(+ - * /):")
x = int(input("enter 1 no:"))
y = int(input("enter 2 no:"))
if ch == '+':
    print("ans =",x+y)
    break
elif ch == '-':
    print("ans =",x-y)
    break
elif ch == '*':
    print("ans =",x*y)
    break
elif ch == '/':
	print("ans =",x/y)
	break
else:
	print("error")
	break