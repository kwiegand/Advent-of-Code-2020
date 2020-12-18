
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
	
	pos1 = int(field[0][0:hyphen_index])
	pos2 = int(field[0][hyphen_index + 1:len(field[0])])
	char = field[1][0:1]
	passwd = field[2]
	
	pos1_val = passwd[pos1 - 1]
	pos2_val = passwd[pos2 - 1]

	if ((pos1_val == char) and (pos2_val == char)) or ((pos1_val != char) and (pos2_val != char)):
		bad_records = bad_records + 1
		brec_index.append(i)
		
print("Good Record Count = " + str(count - bad_records))
print(brec_index)

	
	
