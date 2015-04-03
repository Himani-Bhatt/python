p = ['mercury','venus','earth','mars','jupiter','saturn','uranus','naptune']
print(p)
q = input("Enter panet name:")
if q in p[0:4]:
    print("u entered inner planet")
else:
	print("u entered outer planet.")
