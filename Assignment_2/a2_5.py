x = input("""m = male & f = female
	enter ur gender:""")
y = float(input("Enter ur current salary:"))
if y <= 1000:
	if x == 'm':
		print("ur bonus =",0.05*y)
		pass
	else:
	    print("ur bonus=",0.055*y)
	pass
else:
    print("ur bonus =",0.05*y)
        
