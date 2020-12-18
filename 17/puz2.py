def print_cube(slices,zdim):
    slice_num = 0
    for slice in slices:
        print("z=" + str(slice_num))
        for row in slice:
            print (row)
        slice_num += 1

def expand_w(cubes):
    size_xy = len(cubes[0][0][0])
    size_z = len(cubes[0])
    new_row = ['.'] * size_xy
    #add cube into each new world
    new_w_f = []
    new_w_b = []

    for i in range(0, size_z):
        new_slice_f = []
        new_slice_b = []
        for j in range(0,size_xy):
            new_slice_f.append(new_row.copy())
            new_slice_b.append(new_row.copy())
        new_w_f.append(new_slice_f)
        new_w_b.append(new_slice_b)

    cubes.insert(0,new_w_f)
    cubes.append(new_w_b)


def expand_z(cubes):
    #add 2 slices to cube
    size_xy = len(cubes[0][0][0])
    new_row = ['.'] * size_xy
    
    for w in cubes:
        new_slicef = []
        new_sliceb = []
        for i in range(0,size_xy):
            new_slicef.append(new_row.copy())
            new_sliceb.append(new_row.copy())
        w.insert(0,new_slicef)
        w.append(new_sliceb)

def count_active(cubes):
    count = 0 
    for cube in cubes:
        for slice in cube:
            for row in slice:
                for elem in row:
                    if elem == '#':
                        count += 1
    return count

def expand_xy(cubes):
    size_xy = len(cubes[0][0][0])
    new_size_xy = size_xy + 2
    new_row = ['.'] * new_size_xy
    for w in cubes:
        for slice in w:
            for row in slice:
                #expand row to left and right
                row.insert(0,'.')
                row.append('.')
            #add row at top and bottom
            
            slice.insert(0,new_row.copy())
            slice.append(new_row.copy())

def get_val(cubes,x,y,z,w):
    #size_xy = len(slices[0][0])
    #size_z = len(slices)
    return cubes[w][z][y][x]


def get_active_count(cubes,x,y,z,w):
    lim = [-1,0,1]
    size_xy = len(cubes[0][0][0])
    size_z = len(cubes[0])
    size_w = len(cubes)
    if get_val(cubes,x, y, z, w) == '#':
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
                            for off_w in lim:
                                w_loc = w + off_w
                                if w_loc >=0 and w_loc < size_w:                           
                                    if get_val(cubes,x_loc, y_loc, z_loc, w_loc) == '#':
                                        count += 1
    return count            





file = open('input.txt', 'r')

cubes = []
slices = []
z_dim = 0
init_slice = []
for line in file:
    row = line.strip()
    row = list(row)
    init_slice.append(row)

slices.append(init_slice)
cubes.append(slices)
print_cube(slices,z_dim)





for cycle in range(1,7):
    expand_w(cubes)
    expand_z(cubes)
    expand_xy(cubes)
    #print_cube(slices,cycle)
    size_xy = len(cubes[0][0][0])
    size_z = len(cubes[0])
    size_w = len(cubes)

    next_cube_set = []
    for w in range(0,size_w):
        #build next cube:
        next_cube = []

        for z in range(0,size_z):
            new_slice = []
            for y in range(0,size_xy):
                new_row = []
                for x in range(0,size_xy):
                    adj = get_active_count(cubes,x,y,z,w)
                    val = get_val(cubes,x,y,z,w)
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
        #print_cube(next_cube,cycle)
        
        next_cube_set.append(next_cube)
    cubes = next_cube_set
    


print(count_active(cubes))