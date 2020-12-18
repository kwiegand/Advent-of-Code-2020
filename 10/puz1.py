def factorial(n):
    factorial = 1
    if n > 0:
        for i in range(1,(n+1)):
            factorial = factorial * i
    else:
            factorial = 1
    return factorial

file = open('input.txt', 'r')

adapter_list = [0]
for line in file:
    adapter_list.append(int(line))

adapter_list.sort()

cnt1 = 0
cnt3 = 0

base = 0
next = 0
ctotal = 0
while base < len(adapter_list):
    next = next + 1

    if next <= len(adapter_list):
        difference = adapter_list[next] - adapter_list[base]
        cnt1 = cnt1 + 1
        if difference == 3:
            base = next 
            if cnt1 > 1:
                ctotal = ctotal + factorial(cnt1 -1)
            cnt1 = 0
        if difference > 3:
            base = next - 1
            next = base
    else:
        base = next
    

for i in range(1,len(adapter_list)):
    difference = adapter_list[i] - adapter_list[i-1]
    if difference == 1:
       cnt1 = cnt1 + 1
    elif difference == 3:
        cnt3 = cnt3 + 1

cnt3 = cnt3 + 1
print(cnt1)
print(cnt3)
print(cnt1 * cnt3)

