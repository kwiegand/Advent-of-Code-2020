def get_val(new_val, old_val, mask):
    mask_len = len(mask)
    result = 0
    for i in range(0, mask_len):
        new_ones = (new_val >> i) & 1
        old_ones = (old_val >> i) & 1
        mask_bit = mask[mask_len - i - 1:mask_len -i]
        if mask_bit == '0':
            r_ones = 0
        elif mask_bit == '1':
            r_ones = 1
        else:
            r_ones = new_ones 

        result = result | (r_ones << i)
    print(result)
    return result
        


file = open('input.txt', 'r')
program = []

for line in file:
    ln = line
    ln.strip()
    
    l, r = ln.split(' = ')
    r = r.strip('\n')
    addr= 0
    if l == 'mask':
       addr = -1
    else:
        rbracket = l.find(']')
        addr = int(l[4:rbracket])
        r = int(r)
    program.append([addr,r])

print(program)

mask = ''
max_addr = 0
for line in program:
    if line[0] > max_addr:
        max_addr = line[0]

mem = [0] * (max_addr + 1)

for line in program:
    if line[0] == -1:
        mask = line[1]
    else:
        addr = line[0]
        mem[addr] = (get_val(line[1],mem[addr],mask))

print(sum(mem))





