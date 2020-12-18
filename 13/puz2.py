def find_match(sched,mult,offset):
    i = 0    
    seq_found = False
    while not seq_found:
        curr_time = offset + (mult * i)
        match = True
        for b in sched:
            index = sched.index(b)                
            if (curr_time + index) % b != 0:
                match = False
                break
        if match:
            seq_found = True
        else:
            i += 1
    
    return curr_time


file = open('input.txt', 'r')

e_depart= int(file.readline())
bus_notes = file.readline()

bus_notes.strip()
tmp = bus_notes.split(',')

bus_list = []
for e in tmp:
    if e != 'x':
        bus_list.append(int(e))
    else:
        bus_list.append(1)

print(bus_list)

print("puz2--------------")

max_bus = max(bus_list)
max_pos = bus_list.index(max_bus)

prev_index = 0
offset = bus_list[0]
prod = bus_list[0]

for i in range(1,len(bus_list)):
    offset = find_match(bus_list[0:i+1],prod,offset)
    prod = prod * bus_list[i]


print(offset)


