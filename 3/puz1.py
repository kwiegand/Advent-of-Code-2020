input = open("input.txt", 'r')
x = 0
y = 0

path = [[1,1],[3,1],[5,1],[7,1],[1,2]]
path_count = len(path)

path_pointer = -1
trees = 0
map = []
for line in input:
	row = []
	for char in line.rstrip():
		row.append(char)
	width = len(row)
	map.append(row)
line_count = len(map)
product = 1
for p in path:
	trees = 0
	x = 0
	y = 0
	while(y < line_count):
			
		if map[y][x] == '#':
			trees = trees + 1
			#map[y][x] = 'X'
		#else:
			#map[y][x] = 'O'
		#for char in map[y]:
		#	print(char , end='')
		#print()		
		x = (x + p[0]) % width
		y = y + p[1]
	print("****************************************************")
	print("TREES HIT = " + str(trees))
	product = product * trees
	
print("PRODUCT=" + str(product))
