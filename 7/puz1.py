class Bag:
	def __init__(self, color):
		self.contents = []
		self.color = color
	def contains_bag(self, color):
		for b in self.contents:
			#determine if bag contains color directly
			if b[0].color == color:
				return True
			else:
				return b[0].contains_bag(color)
	
bag_rules = []
lr = Bag('Light Red')
do = Bag('Dark Orange')
bw = Bag('Bright White')
my = Bag('Muted Yellow')
sg = Bag('Shiny Gold')
dv = Bag('Dark Olive')
vp = Bag('Vibrant Plum')
fb = Bag('Faded Blue')
db = Bag('Dotted Black')

lr.contents = [[bw,1],[my,2]]
do.contents = [[bw,3],[my,2]]
bw.contents = [[sg,1]]
my.contents =[[sg,2],[fb,9]]
sg.contents = [[dv,1],[vp,2]]
dv.contents = [[fb,3],[db,4]]
vp.contents = [[fb,5],[db,4]]
fb.contents = []
db.contents = []


bag_rules.append(lr)
bag_rules.append(do)
bag_rules.append(bw)
bag_rules.append(my)
bag_rules.append(sg)
bag_rules.append(dv)
bag_rules.append(vp)
bag_rules.append(fb)
bag_rules.append(db)

bag_list = []

for br in bag_rules:
	if br.contains_bag('Shiny Gold'):
		bag_list.append(br.color)
print(bag_list)
