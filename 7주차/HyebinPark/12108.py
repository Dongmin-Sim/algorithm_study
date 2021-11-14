import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
h = []

for _ in range(n):
    p, l = map(int, input().split())
    mile = list(map(int, input().split()))

    if l > p:
        heapq.heappush(h, 1)
    else:
        mile.sort(reverse = True)
        heapq.heappush(h, mile[l-1])

result, ans = 0, 0
for _ in range(len(h)):
    result += heapq.heappop(h)

    if m >= result:
        ans += 1
    else:
        break

print(ans)