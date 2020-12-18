class Passport:
	def __init__(self):
		self.ecl = ''
		self.hcl = ''
		self.byr = ''
		self.iyr = ''
		self.pid = ''
		self.cid = ''
		self.hgt = ''
		self.eyr = ''
		
		self.hgt_unit = ''
	def is_valid(self):
		if      self.ecl != '' \
			and self.hcl != ''\
			and self.byr != ''\
			and self.iyr!= ''\
			and self.pid != ''\
			and self.hgt != ''\
			and self.eyr != ''\
		:
			return True
		else:
			return False
	
	def set_byr(self,byr):
		ibyr = int(byr)
		if ibyr >= 1920 and ibyr <= 2002:
			self.byr = ibyr
			
	def set_iyr(self,iyr):
		iiyr = int(iyr)
		if iiyr >= 2010 and iiyr <= 2020:
			self.iyr = iiyr
	
	def set_eyr(self,eyr):
		ieyr = int(eyr)
		if ieyr >= 2020 and ieyr <= 2030:
			self.eyr = ieyr
			
	def set_hgt(self,hgt):
		val_len = len(hgt)
		val = 0
		if val_len > 2:
			self.hgt_unit = hgt[val_len - 2:val_len]
			val = int(hgt[0:val_len - 2])
		if self.hgt_unit == 'in':
			if val >= 59 and val <=76:
				self.hgt = hgt
		elif self.hgt_unit == 'cm':
			if val >= 150 and val <=193:
				self.hgt = hgt
			
	def set_hcl(self,hcl):
		char_list = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
		if len(hcl) == 7:
			val = hcl[1:7]
			valid = True
			if hcl[0] =='#':
				for c in val:
					if c not in char_list:
						valid = False
			
			if valid == True:
				self.hcl = hcl
	
	def set_pid(self, pid):
		if len(pid) == 9:
			try:
				int(pid)
				self.pid = pid
				return;
			except:
				return;
			
	def set_ecl(self,ecl):
		val_ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
		if len(ecl) == 3:
			if ecl in val_ecl:
				self.ecl = ecl
				
				
	def print_passport(self):
		print("HCL=" + self.hcl, end=' ')
		print("ECL=" + self.ecl, end=' ')
		print("BYR=" + str(self.byr), end=' ')
		print("IYR=" + str(self.iyr), end=' ')
		print("PID=" + self.pid, end=' ')
		print("CID=" + self.cid, end=' ')
		print("HGT=" + self.hgt, end=' ')
		print("EYR=" + str(self.eyr), end=' ')
		print()
		

input = open("input.txt", 'r')
frl = True

passport_list = []
for line in input:
	if frl == True:
		frl = False
		cur_passport = Passport()
	
	record = line.split(' ')
	if record[0] == '\n':
			frl = True
			passport_list.append(cur_passport)
	else:
		for field in record:
			key_val = field.rstrip().split(':')
			
			if key_val[0] == 'ecl':
				cur_passport.set_ecl(key_val[1])
			elif key_val[0] == 'hcl':
				cur_passport.set_hcl(key_val[1])
			elif key_val[0] == 'byr':
				cur_passport.set_byr(key_val[1])
			elif key_val[0] == 'iyr':
				cur_passport.set_iyr(key_val[1])
			elif key_val[0] == 'pid':
				cur_passport.set_pid(key_val[1])
			elif key_val[0] == 'cid':
				cur_passport.cid = key_val[1]
			elif key_val[0] == 'hgt':
				cur_passport.set_hgt(key_val[1])
			elif key_val[0] == 'eyr':
				cur_passport.set_eyr(key_val[1])


valid = 0
for p in passport_list:
	if p.is_valid():
		valid = valid + 1
	else:
		p.print_passport()

pp_count = len(passport_list)
print("Processed " + str(pp_count) + " passports")
print("Valid = " + str(valid))
	