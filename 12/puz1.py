

north = 0
east = 1
south = 2
west = 3

direction = ([1,0], [0,1], [-1,0], [0,-1])

move_commands = ['N', 'S', 'E', 'W', 'F']

def move(dir, pos, count):
    
    pos[0] = dir[0]*count + pos[0]
    pos[1] = dir[1]*count + pos[1]



def update_position(position, heading, command, count):
    dir = None

    if command in move_commands:
        if command == 'N':
            dir = direction[north]
        elif command == 'S':
            dir = direction[south]
        elif command == 'E':
            dir = direction[east]
        elif command == 'W':
            dir = direction[west]
        elif command == 'F':
            dir = direction[heading]
        
        move(dir,position, count)
        
    elif command == 'L' or command == 'R':
        heading = update_heading(heading,count,command)
    
    return heading

def update_heading(heading, angle, lr):
    adj = int((angle / 90) % 4)

    if (lr == 'L'):
        heading = (heading + (adj * 3)) % 4

    else:
        heading = (heading + adj) % 4

    return int(heading)

file = open('input.txt', 'r')
command_list = []
for line in file:
    row = line
    row.strip()

    command = row[0]
    count = int(row[1: len(row)])
    command_list.append([command,count])

position = [0,0]
heading = east

for c in command_list:
    heading = update_position(position,heading,c[0],c[1])

print(position)
print(abs(position[0]) + abs(position[1]))