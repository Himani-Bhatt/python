a = [1,2,'h',3,4]
print("list 1=",a)
b = ['himani','abcd',5,6,['hello',7,8]]
print("list 2=",b)
a.append(5)
print("after append list 1=",a)
a.extend(b)
print("after extend list 1=",a)