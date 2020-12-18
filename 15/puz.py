
s_list = [0,3,6]
o_list = s_list.copy()
size = len(s_list)
end = 100
first = True
skip_next = False
maxval = max(s_list)
while size < end:
    
    last = s_list[size - 1]
    found = False


    if first:
        l_olist = False
        first = False
    else:        
        l_olist = last in o_list
    
 
    if last != maxval:
        for i in range(0,size - 1):
            
            if not l_olist and (last > size - 2 - i):
                break        
            elif s_list[size - 2 - i] == last:
                found = True
                break

    if found == True:
        diff = i + 1
        s_list.append(diff)
        if diff > maxval:
            maxval = diff
    else:
        s_list.append(0)
    size += 1
    print("LAST = ", end = '')
    print(last, end= '')
    print("        APPENDED: ", end = '')
    print(s_list[size- 1], end = '')
    print("     SIZE = ", end = '')
    print(size - 1)
print("PUZ1: " ,end='')
print(s_list[end - 1])
