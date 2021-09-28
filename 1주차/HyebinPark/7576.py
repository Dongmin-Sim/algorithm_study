import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while q:
        x, y = q.popleft()
        for i, j in d:
            nx = x + i
            ny = y + j

            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                q.append((nx, ny))
                tomato[nx][ny] = tomato[x][y] + 1


m, n = map(int, input().split())
tomato = []
for _ in range(n):
    tomato.append(list(map(int, input().split())))

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque()

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i, j))

bfs()
ans = 0
for t in tomato:
    for i in t:
        if i == 0:
            print(-1)
            exit(0)
        ans = max(ans, i)
print(ans - 1)