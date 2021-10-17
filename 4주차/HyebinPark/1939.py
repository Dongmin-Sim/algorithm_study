import sys
from collections import deque
input = sys.stdin.readline

def bfs(weight):
    q = deque()
    q.append(start)
    visited = set()
    visited.add(start)

    while q:
        s = q.popleft()
        for b, c in bridge[s]:
            if b not in visited and c >= weight:
                q.append(b)
                visited.add(b)

    if end in visited:
        return True
    else:
        return False


n, m = map(int, input().split())
bridge = [[] for _ in range(n + 1)]
minC, maxC = 1, 0

for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append([b, c])
    bridge[b].append([a, c])
    maxC = max(maxC, c)

start, end = map(int, input().split())

ans = 1
while minC <= maxC:
    mid = (minC + maxC) // 2

    if bfs(mid):
        ans = mid
        minC = mid + 1
    else:
        maxC = mid - 1
print(ans)