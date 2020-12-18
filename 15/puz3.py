
s_list = [0,3,6]
o_list = s_list.copy()
size = len(s_list)
end = 30000000
first = True
skip_next = False


cache = [0,3]
cache_lp = [0,1]
cache_size = 2
hcontig = 0
last = s_list[size - 1]
while size < end:
    found = False
    cache_size = len(cache)
    if last <= hcontig:
        pos = cache_lp[last]
        cache_lp[last] = size - 1
        last = size - pos - 1
        found = True
    else:
        contig = True
        for i in range(hcontig+1,cache_size):
            if contig == True:
                if i == cache[i]:
                    hcontig = i
                else:
                    contig = False
            if last == cache[i]:
                pos = cache_lp[i]
                cache_lp[i] = size - 1
                last = size - pos - 1
                found = True
                break
            elif last < cache[i]:
                cache.insert(i,last)
                cache_lp.insert(i,size-1)
                last = 0
                found = True
                break

    if not found:
        cache.append(last)
        cache_lp.append(size - 1)
        last = 0
        
    
    size += 1
    #print(last)
print("PUZ1: " ,end='')
print(last)
