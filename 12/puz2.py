north = 0
east = 1
south = 2
west = 3

direction = ([1,0], [0,1], [-1,0], [0,-1])

move_commands = ['N', 'S', 'E', 'W', 'F']

def move(dir, pos, count):
    
    pos[0] = dir[0]*count + pos[0]
    pos[1] = dir[1]*count + pos[1]

def update_position(position, waypoint, command, count):
    
    if command == 'N':
        waypoint[0] = waypoint[0] + count
    elif command == 'S':
        waypoint[0] = waypoint[0] - count
    elif command == 'E':
        waypoint[1] = waypoint[1] + count
    elif command == 'W':
        waypoint[1] = waypoint[1] - count
    elif command == 'F':
        move(waypoint,position,count)    
        
    elif command == 'L' or command == 'R':
        update_waypoint(waypoint,count,command)
    
    return

def update_waypoint(waypoint, angle, lr):
    adj = int((angle / 90) % 4)
    next = [0,0]
    if (lr == 'L'):
        for i in range(0,adj):
            next[0] = waypoint[1]
            next[1] = -waypoint[0]
            waypoint[0] = next[0]
            waypoint[1] = next[1]
    else:
        for i in range(0,adj):
            next[0] = -waypoint[1]
            next[1] = waypoint[0]
            waypoint[0] = next[0]
            waypoint[1] = next[1]

    return








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
waypoint = [1,10]

for c in command_list:
    update_position(position,waypoint,c[0],c[1])

print(position)
print(abs(position[0]) + abs(position[1]))