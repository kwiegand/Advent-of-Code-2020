input = open('input.txt', 'r')

first = True

grp_answer_list = []

list = []

for line in input:
	
	if first == True:
		first = False
		list = line.rstrip()
		
	if line[0] == '\n':
		first = True
		grp_answer_list.append(list)
	else:
		rec = line.rstrip()
		new_list = []
		for c in rec:
			if c in list:
				new_list.append(c)
		list = new_list
		
grp_answer_list.append(list)				

print(grp_answer_list)
count = 0
for ans in grp_answer_list:
	count = count + len(ans)
	print(count)
	
