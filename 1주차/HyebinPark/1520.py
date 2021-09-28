import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i, j in d:
            nx = x + i
            ny = y + j
            if 0 <= nx < m and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

m, n = map(int, input().split())
graph = []
dp = [[-1] * n for _ in range(m)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(m):
    graph.append(list(map(int, input().split())))
print(dfs(m-1, n-1))