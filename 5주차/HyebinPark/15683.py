import sys
from collections import deque
input = sys.stdin.readline

def dfs(cnt):
    global ans
    if cnt == cctvCnt:
        temp = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] and not graph[i][j]:
                    temp += 1
        return temp

    x, y = cctv[cnt][0], cctv[cnt][1]
    for i in range(4):
        dir = []
        if graph[x][y] == 1:
            dir.append(i)
        elif graph[x][y] == 2:
            dir.append(i)
            dir.append((i + 2) % 4)
        elif graph[x][y] == 3:
            dir.append(i)
            dir.append((i + 1) % 4)
        elif graph[x][y] == 4:
            dir.append(i)
            dir.append((i + 1) % 4)
            dir.append((i + 2) % 4)
        elif graph[x][y] == 5:
            dir.append(i)
            dir.append((i + 1) % 4)
            dir.append((i + 2) % 4)
            dir.append((i + 3) % 4)

        q = deque()
        for i in dir:
            nx = x + d[i][0]
            ny = y + d[i][1]

            while 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] and graph[nx][ny] != 6:
                    visited[nx][ny] = False
                    q.append((nx, ny))
                elif graph[nx][ny] == 6:
                    break
                nx += d[i][0]
                ny += d[i][1]

        ans = min(ans, dfs(cnt + 1))

        while q:
            qx, qy = q.popleft()
            if not graph[qx][qy]:
                visited[qx][qy] = True

        if graph[x][y] == 5:
            break

    return ans

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[True] * m for _ in range(n)]
cctv = []
cctvCnt = 0
ans = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] and graph[i][j] != 6:
            cctv.append((i, j))
            visited[i][j] = False
            cctvCnt += 1
        if not graph[i][j]:
            ans += 1

dfs(0)
print(ans)