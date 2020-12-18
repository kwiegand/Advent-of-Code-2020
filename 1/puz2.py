expenses = []
input = open("input.txt", 'r')
for line in input:
	expenses.append(int(line))
found_answer = False
answer = [0,0,0]
answer_index = [0,0,0]
index = 0
for i in range(0,len(expenses)):
	for j in range(i + 1, len(expenses)):
		for y in range(i + 2, len(expenses)):
			
			#print("i = " + str(i) + "    j = " + str(j) + "      y = " + str(y))
			a = expenses[i]
			b = expenses[j]
			c = expenses[y]
			sum = a + b + c
			#print(str(a) + " + " + str(b) + " + " + str(c) + " = " + str(sum))
			if sum == 2020:
				found_answer = True
				answer = [a, b ,c]
				answer_index = [i, j, y]
print(answer)
print(answer_index)
print("Product = " + str(answer[0] * answer[1] * answer[2]))