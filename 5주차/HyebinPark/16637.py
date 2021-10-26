import sys
input = sys.stdin.readline

n = int(input())
formula = input()

ops = []
def opiter(idx, flag, subop):
    if idx == (n - 1) // 2:
        ops.append(subop)
        return

    if flag:
        opiter(idx+1, False, subop + [0])
    else:
        opiter(idx+1, True, subop + [1])
        opiter(idx+1, False, subop + [0])

opiter(0, False, [])

ans = -2 ** 31

for op in ops:
    q = []
    i = 0
    while i < n:
        if i % 2 == 0:
            q.append(formula[i])
        else:
            if op[(i-1) // 2]:
                left = q.pop()
                right = formula[i+1]
                q.append(str(eval(left + formula[i] + right)))
                i += 1
            else:
                q.append(formula[i])

        i += 1

    pre = q.pop(0)
    for i in range(0, len(q), 2):
        pre = str(eval(pre + q[i] + q[i+1]))

    ans = max(ans, int(pre))
print(ans)
