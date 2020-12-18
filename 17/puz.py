def print_cube(slices,zdim):
    slice_num = 0
    for slice in slices:
        print("z=" + str(slice_num))
        for row in slice:
            print (row)
        slice_num += 1

def expand_z(slices):
    #add 2 slices to cube
    size_xy = len(slices[0][0])
    new_row = ['.'] * size_xy
    new_slicef = []
    new_sliceb = []
    for i in range(0,size_xy):
        new_slicef.append(new_row.copy())
        new_sliceb.append(new_row.copy())
    slices.insert(0,new_slicef)
    slices.append(new_sliceb)

def count_active(slices):
    count = 0 
    for slice in slices:
        for row in slice:
            for elem in row:
                if elem == '#':
                    count += 1
    return count

def expand_xy(slices):
    size_xy = len(slices[0][0])
    new_size_xy = size_xy + 2
    new_row = ['.'] * new_size_xy
    for slice in slices:
        for row in slice:
            #expand row to left and right
            row.insert(0,'.')
            row.append('.')
        #add row at top and bottom
        
        slice.insert(0,new_row.copy())
        slice.append(new_row.copy())

def get_val(slices,x,y,z):
    #size_xy = len(slices[0][0])
    #size_z = len(slices)
    return slices[z][y][x]
def set_val(slices,x,y,z, val):
    slices[z][y][x] = val

def get_active_count(slices,x,y,z):
    lim = [-1,0,1]
    size_xy = len(slices[0][0])
    size_z = len(slices)
    if get_val(slices,x, y, z) == '#':
        count = -1
    else:
        count = 0
    for off_x in lim:
        x_loc = x + off_x
        if  x_loc >= 0 and  x_loc < size_xy:            
            for off_y in lim:
                y_loc = y + off_y
                if y_loc >= 0 and y_loc < size_xy:
                    for off_z in lim:
                        z_loc = z + off_z
                        if z_loc >=0 and z_loc < size_z:                            
                            if get_val(slices,x_loc, y_loc, z_loc) == '#':
                                count += 1
    return count            





file = open('input.txt', 'r')


slices = []
z_dim = 0
init_slice = []
for line in file:
    row = line.strip()
    row = list(row)
    init_slice.append(row)

slices.append(init_slice)

print_cube(slices,z_dim)





for cycle in range(1,7):
    expand_z(slices)
    expand_xy(slices)
    print_cube(slices,cycle)
    size_xy = len(slices[0][0])
    size_z = len(slices)

    #build next cube:
    next_cube = []

    for z in range(0,size_z):
        new_slice = []
        for y in range(0,size_xy):
            new_row = []
            for x in range(0,size_xy):
                adj = get_active_count(slices,x,y,z)
                val = get_val(slices,x,y,z)
                if val == '#':
                    if adj == 2 or adj == 3:
                        new_row.append('#')
                    else:
                        new_row.append('.')
                elif val == '.' and adj == 3:
                    new_row.append('#')
                else:
                    new_row.append(val)
            new_slice.append(new_row)
        next_cube.append(new_slice)
    
    #print("cycle=" + str(cycle))
    #print(count_active(slices))
    print_cube(next_cube,cycle)
    
    slices = next_cube
    


print(count_active(slices))