import sys
input = sys.stdin.readline

def dfs(cnt, result, pl, mi, mul, div):
    global max_, min_
    if cnt == n:
        max_ = max(max_, result)
        min_ = min(min_, result)
        return

    if pl:
        dfs(cnt+1, result + num[cnt], pl-1, mi, mul, div)
    if mi:
        dfs(cnt+1, result - num[cnt], pl, mi-1, mul, div)
    if mul:
        dfs(cnt+1, result * num[cnt], pl, mi, mul-1, div)
    if div:
        if result < 0:
            dfs(cnt+1, -(-result // num[cnt]), pl, mi, mul, div-1)
        else:
            dfs(cnt+1, result // num[cnt], pl, mi, mul, div-1)

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
max_, min_= -12345678990, 12345678990

dfs(1, num[0], op[0], op[1], op[2], op[3])
print(max_)
print(min_)
