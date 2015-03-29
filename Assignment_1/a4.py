n = int(input('''which operation whould you like to perform?
1 = And
2 = or 
3 = Not
4 = Nand (Not+And)
5 = Nor (Not+Or)
ur choice:''' ))
a = bool(int(input("Enter boolean no1:")))
b = bool(int(input("Enter boolean no2:")))            	

while 0<n<6:
    if n == 1:
	    print("ans = ",a and b)
	    break
    elif n == 2:
        print("Ans =",a or b)
        break
    elif n == 3:
        print("Ans: a =",not a )
        print("Ans: b =",not b)
        break
    elif n == 4:
        print("Ans = ",not(a and b)) 
        break
    elif n == 5:
        print("Ans = ",not(a or b))
        break
    else:
        print("Enter valid choice...!!!")  
        break
    pass
	

		
