#a03p02a
l1 = print("l1=",list(range(1,11)))

#a03p02b
l2 = print("l2 =",list(range(10,101,10)))

#a03p02c
l3 = ['python','django','flask','string','function','classes']
print("l3 = \n",l3)

#a03p02d
l4 = {"l1":l1,"l2":l2,"l3":l3}
print(l4)

#a03p02e
main_list = [l1,l2,l3]
print("main_list =",main_list)

#a03p02f
l5 = l1 * 2
print(l5)

#a03p02g
main_list.append(l5)
print(main_list)

#a03p02h
print("occurences of int 1in the main_list =",main_list.count(1))