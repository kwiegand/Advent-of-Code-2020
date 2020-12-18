class ShiftReg:
    def __init__(self, size):
        self.size = size
        self.register = [0]*size
        
    def shift_in(self,num):
        shift_out = self.register[0]
        self.register = self.register[1:self.size]
        self.register.append(num)
        return shift_out
        
def sums_to(sum, sr):
    found = False
    for i in range(0,sr.size-1):
        num1 = sr.register[i]

        for j in range(i+1, sr.size):
            num2 = sr.register[j]
            if (num1 + num2) == sum:
                found = True
                break
        
        if found == True:
            break
    return found

def find_cont_range(sum,stream):
    index = -1
    max_offset = 0

    for i in range(0,len(stream)):
        temp_sum = stream[i]

        for j in range(i+1,len(stream)):
            temp_sum = temp_sum + stream[j]
            if temp_sum == sum:
                index = i
                max_offset = j - i
                break
            elif temp_sum > sum:
                break

        if index > 0:
            break
    return [index,max_offset]



file = open('input.txt', 'r')
regsize = 25

sr = ShiftReg(regsize)
stream = []
key = 0
for line in file:
    stream.append(int(line))

for i in range(0,regsize):
    sr.shift_in(stream[i])

for i in range(regsize,len(stream)):
    next = stream[i]
    if not sums_to(next,sr):
        key = next
        break
    else:
        sr.shift_in(next)

code = find_cont_range(key,stream)
print(code)

vals = stream[code[0] : code[0]+code[1] + 1]
print(vals)
ans = (max(vals)) + min(vals)
print(ans)



