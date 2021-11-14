# https://www.acmicpc.net/problem/12018
import sys
import heapq


def read(): return sys.stdin.readline().rstrip()


n, m = map(int, read().split())
answer = 0
mileages_sum = 0
subject = []

for i in range(n):
    P, L = map(int, read().split())
    mileages = list(map(int, read().split()))

    if L > P:
        heapq.heappush(subject, 1)
    else:
        mileages.sort()
        index = P - L
        heapq.heappush(subject, mileages[index])

for _ in range(len(subject)):
    mileages_sum += heapq.heappop(subject)

    if m >= mileages_sum:
        answer += 1
    else:
        break

print(answer)
