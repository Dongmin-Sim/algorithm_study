import sys
input = sys.stdin.readline

x, y = map(int, input().split())

start, end = 1, 1000000000
ans = int(1e9)
z = y * 100 // x

if z >= 99:
    print(-1)
    exit(0)

while start <= end:
    mid = (start + end) // 2

    if ((y+mid) * 100 // (x+mid)) > z:
        end = mid - 1
        ans = min(mid, ans)
    else:
        start = mid + 1

print(ans)