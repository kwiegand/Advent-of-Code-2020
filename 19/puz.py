def poss_sol(rules,rul_num):
    rule = rules[rul_num]
    
    rule_size = len(rule)
    sub_patt = []
    for sub in range(0,rule_size):
        r_size = len(rule[sub])
        r_patt = []
        for ritem in range(0,r_size):
            val = rule[sub][ritem]
            if rule[sub][ritem] == 'a' or rule[sub][ritem] == 'b':                
                return val
            else:
                p =  poss_sol(rules,val)           
                r_patt.append(p)   
        sub_patt.append(r_patt)             
    return sub_patt

file = open('test_input.txt', 'r')

proc_rules = True
messages = []
rules = {}

#process input
for line in file:
    if line == '\n':
        proc_rules = False
        continue

    if proc_rules == True:
        r = line.strip()
        num, rule = r.split(':')
        sublist = (rule.strip()).split(' | ')

        rsublist = []
        for l in sublist:
            l = l.strip("\"")
            rlist = l.split(' ')
            rsublist.append(rlist)

        rules[num] = rsublist

    else:
        
        messages.append(line.strip())
    
pos = poss_sol(rules,'0')


def find_pattern(pat):
    patt_mem = len(pat)
    
    pattern = ''   
    for p in range(0,patt_mem):
        if pat[p] == 'a' or pat[p] == 'b':
            pattern += pat[p]
            
        else:
            for subp in pat[p]:
                pattern += find_pattern(subp)
            print(pattern)
            
    return pattern

for m in messages:
    m_size = len(m)

    
    i = 0
    sub_i = 0
    while i < m_size:
        plist = []
        index =  0
        j = len(find_pattern(pos[0][sub_i]))
        substring = m[i:i+j]
        i = i + j
        sub_i += 1


