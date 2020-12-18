
input = open("input.txt", 'r')
password=[]
for line in input:
	password.append(line)

count = len(password)
print("Read in " + str(count) + " passwords")


record = []
bad_records = 0
brec_index = []
for i in range(0, count):
	field = password[i].split(' ')
	hyphen_index = field[0].find('-')
	
	min = int(field[0][0:hyphen_index])
	max = int(field[0][hyphen_index + 1:len(field[0])])
	char = field[1][0:1]
	passwd = field[2]
	record.append([min, max, char, passwd])
	print("Record " + str(i) + ": MIN=" + str(record[i][0]) + "  MAX=" + str(record[i][1]) + "  CHAR=" + record[i][2])
	
	char_count = 0
	for j in passwd:
		if j == char:
			char_count = char_count + 1
	print("char count = " + str(char_count))
	if (char_count < min) or (char_count > max):
		bad_records = bad_records + 1
		brec_index.append(i)
		
print("Good Record Count = " + str(count - bad_records))
print(brec_index)

	
	
