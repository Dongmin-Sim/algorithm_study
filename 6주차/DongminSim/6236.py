'''
문제 : 용돈관리
출처 : https://www.acmicpc.net/problem/6236
'''
import sys


def solution(m, plan):
    start, end = min(plan), sum(plan)

    while start <= end:
        num = m - 1
        mid = (start + end) // 2
        budget = mid

        # 시뮬레이션
        for daily_req in plan:
            if budget < daily_req:
                budget = mid
                num -= 1

            budget -= daily_req

        # budget가 적은 경우 -> budget을 늘려줘야 함.
        # 인출 횟수보다 많이 인출한 경우 or
        if num < 0 or mid < max(plan):
            start = mid + 1
        # budget가 큰 경우 -> budget을 줄여줘야 함.
        else:
            end = mid - 1
            ans = mid

    return ans


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    plan = []

    for _ in range(n):
        plan.append(int(input()))

    print(solution(m, plan))
