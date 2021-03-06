
def count_adj(map, x_size, y_size, seat_coord):
    count = 0;

    #0deg
    r = seat_coord[0]
    c = seat_coord[1]

    count = 0
    #0deg U
    if r > 0:
        if map[r-1][c] == '#':
            count = count + 1

    #45deg UR
    if r > 0 and c < x_size - 1:
        if map[r-1][c+1] == '#':
            count = count + 1

    #90deg R
    if c < x_size - 1:
        if map[r][c+1] == '#':
            count = count + 1

    #135deg BR
    if c < x_size - 1 and r < y_size -1:
        if map[r+1][c+1] == '#':
            count = count + 1
    #180deg B
    if r < y_size -1:
        if map[r+1][c] == '#':
            count = count + 1

    #225deg BL
    if r < y_size -1 and c > 0:
        if map[r+1][c-1] == '#':
            count = count + 1

    #270deg L
    if c > 0:
        if map[r][c-1] == '#':
            count = count + 1

    #315deg UL
    if c > 0 and r > 0:
        if map[r-1][c-1] == '#':
            count = count + 1
    
    return count




def seat_proc(map,x_size, y_size):
    
    next_map = map.copy()
    for r in range(0,y_size):
        next_map[r]= next_map[r].copy()
    
    for r in range(0, y_size):
        for c in range(0, x_size):
            #if seat is empty

            if map[r][c] == 'L':
                #and no occupied seats adjacent
                if count_adj(map,x_size,y_size,[r,c]) == 0:
                    next_map[r][c] = '#'

            #if seat empty
            elif map[r][c] == '#':
                #and four or more seats adj are occupied
                if count_adj(map,x_size,y_size,[r,c]) >= 4:
                    next_map[r][c] = 'L'
    return next_map

def maps_equal(map1, map2):
    m_equal = True
    for r in range(0,y_size):
        for c in range(0,x_size):
            if map1[r][c] != map2[r][c]:
                m_equal = False
                break
        if m_equal == False:
            break
    return m_equal


file = open('input.txt', 'r')

map = []


for line in file:
    row = line
    row = row.strip()
    col = []
    for c in row:
        col.append(c)
    
    map.append(col)
    

x_size = len(map[0])
y_size = len(map)

print(x_size)
print(y_size)

m_equal = False
while(not m_equal):
    
    
    n_map = seat_proc(map,x_size,y_size)

    m_equal = maps_equal(n_map,map)
    
    #copy old map
    for r in range(0,y_size):
        new_r = n_map[r].copy()
        map[r]= new_r
    
n_map = seat_proc(map,x_size,y_size)
for row in map:
    for c in row:
        print(c, end='')
    print('')
count = 0
for r in map:
    for c in r:
        if c == '#':
            count = count + 1

print(count)