class Bag:
	def __init__(self, color):
		self.contents = []
		self.color = color
		
def contains_bag(bag, br, color):
	found = False
	for b in bag.contents:
		#determine if bag contains color directly
		if b[1] == color:
			found = True
		else:
			for rule in br:
				if rule.color == b[1]:
					next_bag = rule
					break
			found = found or contains_bag(next_bag,br,color)
	return found
	
input = open('input.txt', 'r')
	
bag_rules = []

for line in input:
	contain = line.split(' contain ')
	bag = contain[0].split(' ')
	color = bag[0] + ' ' + bag[1]
	bag = Bag(color)

	a = contain[1].strip()
	a = a.strip('.')
	contents = a.split(', ')
	
	for b in contents:
		token = b.split(' ')
		
		if token[0] != 'no':
			qty = int(token[0])
			color = token[1] + ' ' + token[2]
			bag.contents.append([qty,color])
	bag_rules.append(bag)
	
list = []
for br in bag_rules:
	if contains_bag(br, bag_rules, 'shiny gold'):
		list.append(br.color)
print(list)
print(len(list))



