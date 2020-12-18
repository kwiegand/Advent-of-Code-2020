def in_window(val, lower, upper):
    
        if val < lower or val > upper:
            return False
        else:
            return True

file = open('input.txt', 'r')


#field_list['name', range1[lower, upper], range2[lower, upper]]
field_list = []
o_ticket_list = []
my_ticket_list = []

ticket_section = 0

for line in file:

    if line == '\n' or line == 'your ticket:\n' or line == 'nearby tickets:\n':
        ticket_section += 1
    elif ticket_section == 0:
        colon = line.find(':')
        name = line[0:colon]
        
        range_list = line[colon + 1: len(line)]
        range_list = range_list.strip()
        range_list = range_list.split('or')
        r1= range_list[0].split('-')
        r2 = range_list[1].split('-')
        range1 = [int(r1[0]), int(r1[1])]
        range2 = [int(r2[0]), int(r2[1])]

        field_list.append([name,range1, range2])
    elif ticket_section == 2:
        
        numbers = line.split(',')
        for n in numbers:
            val = int(n)
            my_ticket_list.append(val)

    elif ticket_section == 4:
        num_list = []
        numbers = line.split(',')
        for n in numbers:
            val = int(n)
            num_list.append(val)
        o_ticket_list.append(num_list)

inv_num = []

for t in o_ticket_list:
    for n in t:
        found = False

        for f in field_list:
            found = found or in_window(n,f[1][0],f[1][1]) or in_window(n,f[2][0],f[2][1])
        
        if found == False:
            inv_num.append(n)

print("PUZ1: ", end = '')
print(sum(inv_num))
    
val_tickets = []
for t in o_ticket_list:
    t_valid = True
    for n in t:
        found = False

        for f in field_list:
            found = found or in_window(n,f[1][0],f[1][1]) or in_window(n,f[2][0],f[2][1])
        
        
        if found == False:
            t_valid = False
    if t_valid == True:
        val_tickets.append(t)

pos_t_fields = []

for t in val_tickets:
    pos_fields = []
    for n in t:
        
        name_list = []
        for f in field_list:            
            name = f[0]
            if in_window(n,f[1][0],f[1][1]) or in_window(n,f[2][0],f[2][1]):
                name_list.append(name)
        pos_fields.append(name_list)    
    pos_t_fields.append(pos_fields)


f_cnt = len(pos_t_fields[0])
t_cnt = len(pos_t_fields)

def get_common(d_list):
    p_fields = []
    for f in field_list:
        add = True
        for t in d_list:
            if f[0] not in t:
                add = False
        if add == True:
            p_fields.append(f[0])
    return p_fields

det_fields = [0]*f_cnt

done = False
while not done:
    for fi in range(0,f_cnt):
        if det_fields[fi] == 0:
            d_list = []
            for ti in range(0,t_cnt):
                d_list.append(pos_t_fields[ti][fi])
            c_list = get_common(d_list)
            for ti in range(0,t_cnt):
                pos_t_fields[ti][fi] = c_list
            
            if len(c_list) == 1:
                det_fields[fi] = 1
                for fd_index in range(0,len(field_list)):
                    if field_list[fd_index][0] == c_list[0]:
                        break
                del field_list[fd_index]
                det_fields[fi] = 1
                print("Removed FI " + str(fi))
    all_ones = True
    for f in pos_t_fields[0]:
        if len(f) > 1:
            all_ones = False
            break
    if all_ones == True:
        done = True
d_vals = []
for i in range(0,len(pos_t_fields[0])):
    s = pos_t_fields[0][i][0].split(' ')
    if s[0] == 'departure' :
        d_vals.append(my_ticket_list[i])
        print(pos_t_fields[0][i])

prod = 1

for v in d_vals:
    prod = prod * v
print(prod)