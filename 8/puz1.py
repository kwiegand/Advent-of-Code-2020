class CPU:
	def __init__(self):
		self.PC = 0
		self.ACC = 0
		self.prog = []
		self.bp = []
		
	def exec_step(self):
		self.bp.append(self.PC)
		#fetch
		#instr = self.fetch(self.prog[self.PC])
		#decode & execute
		self.decode(self.prog[self.PC])
		
	
	def acc(self, operand):
		self.ACC = self.ACC + operand
		self.PC = self.PC + 1
		
	def jmp(self, operand):
		self.PC = self.PC + operand
		
	def nop(self):
		self.PC = self.PC + 1
		
	def fetch(self,code):
		code.strip()
		parse = code.split(' ')
		operand = int(parse[1])
		return [parse[0],operand]
		
	
	def decode(self,instr):
		print(instr)
		if instr[0] == 'acc':
			self.acc(instr[1])
		elif instr[0] == 'jmp':
			self.jmp(instr[1])
		elif instr[0] == 'nop':
			self.nop()
		
	def dump(self):
		print("PC = ", end='')
		print(self.PC, end='')
		print("    ACC= ", end='')
		print(self.ACC)
		
	
cpu = CPU()
infile = open('input.txt' ,'r')
for line in infile:
	line.strip()
	parse = line.split(' ')
	operand = int(parse[1])
	cpu.prog.append([parse[0],operand])
	

swapped_instr = []
cur_instr = 0
swapped = False
old_inst = ''
while(1):

	
	if swapped == False:
		if cpu.PC not in swapped_instr:
			if cpu.prog[cpu.PC][0] == 'nop':
				cpu.prog[cpu.PC][0] = 'jmp'
				cur_instr = cpu.PC
				old_inst = 'nop'
				swapped = True
			elif cpu.prog[cpu.PC][0] == 'jmp':
				cpu.prog[cpu.PC][0] = 'nop'
				cur_instr = cpu.PC
				old_inst = 'jmp'
				swapped = True
			swapped_instr.append(cur_instr)
	
	if (cpu.PC in cpu.bp) or (cpu.PC > len(cpu.prog)) or (cpu.PC < 0):
		#restore and restart
		print("RESTORED")
		cpu.dump()
		cpu.prog[cur_instr][0] = old_inst
		cpu.PC = 0
		cpu.ACC = 0
		cpu.bp = []
		swapped = False
		
	if cpu.PC == len(cpu.prog):
		break
	print(cpu.PC)
	cpu.exec_step()

cpu.dump()
print("FINISHED")