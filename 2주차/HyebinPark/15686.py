import sys
from itertools import combinations
input = sys.stdin.readline


########### dfs로 풀기
def dfs(idx, cnt):
    global ans

    if idx > len(chicken):
        return

    if cnt == m:
        sumval = 0
        for h in house:
            minval = int(1e9)
            for i, ch in enumerate(chicken):
                if check[i]:
                    continue
                minval = min(minval, abs(ch[0] - h[0]) + abs(ch[1] - h[1]))
            sumval += minval
        ans = min(ans, sumval)

    check[idx] = False
    dfs(idx + 1, cnt + 1)

    check[idx] = True
    dfs(idx + 1, cnt)


n, m = map(int, input().split())
graph, house, chicken = [], [], []
ans = int(1e9)

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1: house.append([i, j])
        elif graph[i][j] == 2: chicken.append([i, j])

check = [True] * (len(chicken) + 1)
dfs(0, 0)
print(ans)




########### combinations로 풀기

# for chi in combinations(chicken, m):
#     minval = 0
#     for h in house:
#         chidist = [abs(c[0] - h[0]) + abs(c[1] - h[1]) for c in chi]
#         minval += min(chidist)
#     ans = min(ans, minval)
# print(ans)