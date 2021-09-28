import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([0, 0, 1])

    while q:
        x, y, c = q.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][c]

        for i, j in d:
            nx = x + i
            ny = y + j

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and c:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])

                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    q.append([nx, ny, c])
    return -1

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

visited = [[[0] * 2 for _ in range(m)] for __ in range(n)]
visited[0][0][1] = 1
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

print(bfs())