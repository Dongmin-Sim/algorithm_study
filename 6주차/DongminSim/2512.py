'''
문제 : 예산
출처 : https://www.acmicpc.net/problem/6236
카테고리 : #binary-search
'''


def solution(n, requests, budget):
    start, end = 0, max(requests)

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in range(n):
            total += min(mid, requests[i])

        if total <= budget:
            start = mid + 1
        else:
            end = mid - 1

    return end


if __name__ == "__main__":
    n = int(input())
    requests = list(map(int, input().split()))
    budget = int(input())

    if sum(requests) <= budget:
        print(max(requests))
    else:
        print(solution(n, requests, budget))
