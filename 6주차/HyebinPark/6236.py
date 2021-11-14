import sys
input = sys.stdin.readline

n, m = map(int, input().split())
money = []

for _ in range(n):
    money.append(int(input()))

start, end = max(money), sum(money)

while start <= end:
    mid = (start + end) // 2

    result = mid - money[0]
    cnt = 1
    for i in range(1, n):
        if result >= money[i]:
            result -= money[i]
        else:
            result = mid - money[i]
            cnt += 1

    if cnt <= m:
        end = mid - 1
    else:
        start = mid + 1

print(mid)