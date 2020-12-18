def eval_expr(expression):
    #evaluate + operations first
    i = 1
    add_reduced = expression.copy()
    while i < len(add_reduced):
        op = add_reduced[i]
        

        if op == '+':
            l = int(add_reduced[i-1])
            r = int(add_reduced[i+1])
            res = l + r
            del add_reduced[i-1]
            del add_reduced[i-1]
            add_reduced[i-1] = res
        else:    
            i += 2

    l = int(add_reduced[0])
    i = 1

    while i < len(add_reduced):
        op = add_reduced[i]
        r = int(add_reduced[i+1])

        if op == '*':
            l = l * r
        i += 2
    return l

def reduce_expr(expression):
    final_exp = []
    size_e = len(expression)
    i = 0
    while i < size_e:
        if expression[i] == '(':
            p_count = 1
            j = i
            while p_count > 0: 
                j += 1               
                if expression[j] == ')':
                    p_count -= 1
                elif expression[j] == '(':
                    p_count += 1
                
            r_expr = []
            r_expr = reduce_expr(expression[i+1:j])
            exp_result = eval_expr(r_expr)
            final_exp.append(exp_result)
            i = j
        else:
            final_exp.append(expression[i])
        i += 1


    return final_exp


file = open("input.txt")
r = []
for line in file:
    trimmed = line.strip()
    tokens = []

    for c in trimmed:
        if c != ' ':
            tokens.append(c)
    f_expr = reduce_expr(tokens)
    
    r.append(eval_expr(f_expr))
    
print(sum(r))
