file = open('input.txt', 'r')

e_depart= int(file.readline())
bus_notes = file.readline()

bus_notes.strip()
tmp = bus_notes.split(',')

bus_list = []
for e in tmp:
    if e != 'x':
        bus_list.append(int(e))

print(bus_list)

bus_found = False
cur_time = e_depart
while not bus_found:
    for b in bus_list:
        if cur_time % b == 0:
            bus_found = True
            break
    if not bus_found:
        cur_time += 1

print(cur_time)
print(b)
wait_time = cur_time - e_depart
print(b * wait_time)
