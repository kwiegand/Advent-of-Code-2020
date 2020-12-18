input = open('input.txt', 'r')

pass_list = []
for line in input:
	row = line[0:7]
	col = line[7:10]
	
	row_b = ''
	for c in row:
		if c == 'B':
			val = '1'
		else:
			val = '0'
		row_b = row_b + val
	
	col_b = ''
	for c in col:
		
		if c == 'R':
			val = '1'
		else:
			val = '0'
		
		col_b = col_b + val
		
		
	int_row = int(row_b, 2)
	int_col = int(col_b ,2)
	
	seat_id = (int_row * 8) + int_col
	
	pass_list.append([int_row, int_col, seat_id])

high_seat_id = 0
seat_id = []
for p in pass_list:
	seat_id.append(p[2])

seat_id.sort()

first_seat = seat_id[0]
for i in range(0,len(seat_id)):
	if i < len(seat_id) -1:
		if seat_id[i+1] != seat_id[i] +1:
			print("FOUND SEAT AT ID = " + str(seat_id[i+1] - 1))