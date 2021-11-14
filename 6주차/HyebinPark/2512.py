import sys
input = sys.stdin.readline

n = int(input())
numlst = list(map(int, input().split()))
m = int(input())

numlst.sort()

start, end = numlst[0], numlst[-1]
ans = 0

if start > m // len(numlst):
    print(m // len(numlst))
    exit(0)

while start <= end:
    mid = (start + end) // 2

    result = 0
    for num in numlst:
        if num > mid:
            result += mid
        else:
            result += num

    if result > m:
        end = mid - 1
    else:
        ans = max(mid, ans)
        start = mid + 1
print(ans)
