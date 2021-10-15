import sys
input = sys.stdin.readline

n = int(input())
elec = []

for _ in range(n):
    elec.append(list(map(int, input().split())))

elec.sort(key = lambda x: x[0])

dp = [1] * n
for i in range(n):
    for j in range(i):
        if elec[i][1] > elec[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(n - max(dp))
