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
	
def sum_bags(bag,bag_rules):
	sum = 0
			
	for item in bag.contents:
		qty = item[0]
		
		for rule in bag_rules:
				if rule.color == item[1]:
					next_bag = rule
					break
		print(next_bag.color)
		sum = sum + qty * (sum_bags(next_bag, bag_rules) + 1)
	
	return sum
	
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
	if br.color == 'shiny gold':
		bag = br
		break
total = sum_bags(bag, bag_rules)
print(total)


