expenses = []
input = open("input.txt", 'r')
for line in input:
	expenses.append(int(line))
found_answer = False
answer = [0,0]
answer_index = [0,0]
index = 0
for i in range(0,len(expenses)):
	for j in range(i, len(expenses) - 1):
		print("i = " + str(i) + "    j = " + str(j))
		a = expenses[i]
		b = expenses[j + 1]
		sum = a + b
		print(str(a) + " + " + str(b) + " = " + str(sum))
		if sum == 2020:
			found_answer = True
			answer = [a, b]
			answer_index = [i, j + 1]
print(answer)
print(answer_index)
print("Product = " + str(answer[0] * answer[1]))