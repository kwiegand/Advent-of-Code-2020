input = open('input.txt', 'r')

first = True

grp_answer_list = []

list = []

for line in input:
	if first == True:
		first = False
		list = []
	
	if line[0] == '\n':
		first = True
		grp_answer_list.append(list)

	else:
		rec = line.rstrip()
		for c in rec:
			if c not in list:
				list.append(c)
grp_answer_list.append(list)				

count = 0
for ans in grp_answer_list:
	count = count + len(ans)
	print(count)
	
