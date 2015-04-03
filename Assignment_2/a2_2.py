n = int(input("Enter no:"))
c =int(n/2) 
for i in range(2,c):
    if n % i == 0:
        print("this is not prime no")
    break 	
       