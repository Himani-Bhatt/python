l1 = [1,2,3,4,'hello',[20,12,6],'python']
print("l1 =",l1)
d1 = {"abc":"cde","efg":"hij"}
print("d1 =",d1)
main_list = []
main_list.append(l1)
print(main_list)
main_list.extend(d1)
print(main_list)

for i in main_list:

	if type(i) == dict:
		print(d1.keys())
		print(d1.values())