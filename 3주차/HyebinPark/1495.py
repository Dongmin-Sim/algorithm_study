import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
voldiff = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        if dp[i][j]:
            if j + voldiff[i] <= m:
                dp[i+1][j+voldiff[i]] = 1
            if j - voldiff[i] >= 0:
                dp[i+1][j-voldiff[i]] = 1

ans = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        ans = i
        break
print(ans)