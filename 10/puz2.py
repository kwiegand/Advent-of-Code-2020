def factorial(n):
    factorial = 1
    if n > 0:
        for i in range(1,(n+1)):
            factorial = factorial * i
    else:
            factorial = 1
    return factorial

def find_combinations(lst):
    
    size = len(lst)
    tries = 2**(size - 2)
    poss_list = []
    t_list = []
    for i in range(0,tries):
        tlist = lst[1:size-1]
        for j in range(0,size-2):
            if (i >> j) & 1:
                tlist[j] = 0
        poss_list.append(lst[0:1] + tlist +lst[size -1:size])    
        print(poss_list)
    
    combinations = 0
    for p in poss_list:
        valid = True
        for i in range(0,len(p)):
            if i == 0 or p[i] != 0:
                for j in range(i+1,len(p)):
                    if p[j] !=0:
                        if p[j] - p[i] > 3:
                            valid = False
                            break
                        else:
                            break
                if valid == False:
                    break
        if valid == True:
            combinations = combinations + 1
    

    print(combinations)

    return combinations



file = open('input.txt', 'r')

adapter_list = [0]
for line in file:
    adapter_list.append(int(line))

adapter_list.sort()
adapter_list.append(max(adapter_list)+3)

cnt1 = 0

base = 0
next = 2
ctotal = 0
vl = []
ones = []
twos = []
combs = []
prod = []
start = True
for i in range(1, len(adapter_list)-1):
    
    if ((adapter_list[i] - adapter_list[i-1]) == 2 and (adapter_list[i+1] - adapter_list[i]) == 2 ) or ((adapter_list[i+1] - adapter_list[i]) == 3) or ((adapter_list[i] - adapter_list[i-1]) == 3):
        vl.append(adapter_list[base:i+1])
        prod.append(find_combinations(adapter_list[base:i+1]))
        base = i
        
print(prod)
print(vl)
product = 1
for p in prod:
    product = p * product
print(product)



