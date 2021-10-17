'''
문제 : 전깃줄
출처 : https://www.acmicpc.net/problem/2565
카테고리 : #DP, #LIS #가장-긴-증가하는-수열
'''


def LIS(n, line):
    dp = [1] * (n)

    line.sort()
    for i in range(n):
        for j in range(i):
            if line[i][1] > line[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    return n - max(dp)


def solution():
    n = int(input())
    line = []

    for i in range(n):
        s, e = map(int, input().split())
        line.append((s, e))

    print(LIS(n, line))


if __name__ == '__main__':
    solution()
