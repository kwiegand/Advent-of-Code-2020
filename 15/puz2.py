
s_list = [0,3,6]
o_list = s_list.copy()
size = len(s_list)
end = 30000000
first = True
skip_next = False
maxval = max(s_list)

cache = [0,3]
cache_lp = [0,1]
last = s_list[size - 1]
while size < end:
    
    if last in cache:
        ci = cache.index(last)
        pos = cache_lp[ci]
        last = size - pos - 1
        cache_lp[ci] = size - 1
        
    else:  
        cache.append(last)
        cache_lp.append(size - 1)
        last = 0
    
    size += 1
    #print(last)
print("PUZ1: " ,end='')
print(last)
