

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
        
def get_addr(addr, mask):
    mask_len = len(mask)
    string_address = ''
    result = []
    
    
    for i in range(0, mask_len):
        ones = str((addr >> i) & 1) 
        r_ones = 0

        mask_bit = mask[mask_len - i - 1:mask_len -i]
        if mask_bit == '0':
            r_ones = ones
        elif mask_bit == '1':
            r_ones = '1'
        else:
            r_ones = 'X'

        string_address = r_ones + string_address 
        x_count = 0
    for c in string_address:
        if c == 'X':
            x_count += 1

    result = [''] * 2**x_count
    x_index = 0

    for c in string_address:
        if c == 'X':
            toggle_bit = '0'
            toggle_count = 2**x_index

            for i in range(0,len(result)):
                result[i] =result[i] + toggle_bit
                toggle_count -= 1
                if toggle_count == 0:
                    if toggle_bit == '0':
                        toggle_bit = '1'
                    else:
                        toggle_bit = '0'
                    toggle_count = 2**x_index
            x_index += 1
        else:
            for i in range(0,len(result)):
                result[i] = result[i] + c
        



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

mem_addr = []
vals = []
mask = ''



for line in program:
    if line[0] == -1:
        mask = line[1]
    else:
        addr = get_addr(line[0],mask)
        for a in addr:
            if a in mem_addr:
                index = mem_addr.index(a)
                vals[index]= line[1]
            else:
                mem_addr.append(a)
                vals.append(line[1])


print(sum(vals))





