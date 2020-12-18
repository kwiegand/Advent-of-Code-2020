
def bin_search(o_lst, val):
    top = len(o_lst) - 1
    bottom = 0
    found = False

    while (top - bottom) > 1:
        cur = int((top - bottom)/2) + bottom

        cur_val = o_lst[cur]

        if val == cur_val:
            found = True
            break
        elif val > cur_val:
            bottom = cur + 1
        else:
            top = cur - 1
    
    if not found:
        if val > o_lst[top]:
            o_lst.insert(top + 1,val)
            cur = top + 1
        elif val < o_lst[bottom]:
            o_lst.insert(bottom, val)
            cur = bottom
        elif val == o_lst[bottom]:
            cur = bottom
            found = True
        elif val == o_lst[top]:
            cur = top
            found = True
        else:
            o_lst.insert(top,val)
            cur = top
    

    return [cur, found]  


s_list = [0,3,6]

end = 30000000

cache = [0,1,3,16,17,19]
cache_lp = [5,1,2,3,0,4]

size = len(cache)


#cache = [0,3,6]
#cache_lp = [0,1,2]
exists = False
last = 0

while size < end:
    if last != 0:
        index, exists = bin_search(cache, last)
    else:
        index = 0
        exists = True
    if exists:
        pos = cache_lp[index]
        cache_lp[index] = size - 1
        last = size - pos - 1
        found = True
    else:
        cache_lp.insert(index, size -1)
        last = 0
                
    
    size += 1
    #print(last)
print("PUZ1: " ,end='')
print(last)