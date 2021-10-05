import sys
input = sys.stdin.readline

def dfs(x, y):
    if y == c - 1:
        return True

    graph[x][y] = 'x'

    for dx, dy in d:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.':
            if dfs(nx, ny):
                return True
    return False

r, c = map(int, input().split())
graph = []
ans = 0

for _ in range(r):
    graph.append(list(input().rstrip()))

d = [(-1, 1), (0, 1), (1, 1)]

for i in range(r):
    if dfs(i, 0):
        ans += 1
print(ans)