import sys
from collections import deque

def bfs(a, b):
    global cnt
    cnt += 1
    visited[a][b] = 0
    queue = deque()
    queue.append((a, b))

    while queue:
        x, y = queue.popleft()
        for i in d:
            nx = x + i[0]
            ny = y + i[1]
            if 0 <= nx < n and 0 <= ny < m and paint[nx][ny] == 1 and visited[nx][ny]:
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = 0



input = sys.stdin.readline
n, m = map(int, input().split())
paint = []
cntlst = []
visited = [[1] * m for _ in range(n)]
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    paint.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if paint[i][j] == 1 and visited[i][j]:
            cnt = 0
            bfs(i, j)
            cntlst.append(cnt)

if len(cntlst) == 0:
    print(0)
    print(0)
else:
    print(len(cntlst))
    print(max(cntlst))