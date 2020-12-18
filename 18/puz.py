def eval_expr(expression):
    l = int(expression[0])
   

    expr_size = len(expression)
    i = 1
    while i < expr_size:
        op = expression[i]
        r = int(expression[i+1])

        if op == '+':
            l = l + r
        elif op == "*":
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
