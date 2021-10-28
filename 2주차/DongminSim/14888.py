'''
문제 : 연산자 끼워넣기
출처 : https://www.acmicpc.net/problem/14888
카테코리 : #dfs
'''
import sys


def dfs(cnt, result, pl, mi, mul, div):
    global n, nums, min_val, max_val
    if cnt == n:
        max_val = max(max_val, result)
        min_val = min(min_val, result)
        return

    if pl:
        dfs(cnt+1, result + nums[cnt], pl-1, mi, mul, div)
    if mi:
        dfs(cnt+1, result - nums[cnt], pl, mi-1, mul, div)
    if mul:
        dfs(cnt+1, result * nums[cnt], pl, mi, mul-1, div)
    if div:
        if result < 0:
            dfs(cnt+1, -(-result // nums[cnt]), pl, mi, mul, div-1)
        else:
            dfs(cnt+1, result // nums[cnt], pl, mi, mul, div-1)


def solution():
    global n, nums, min_val, max_val
    n = int(input())
    nums = list(map(int, input().split()))
    plus, minus, multiple, divide = map(int, input().split())

    min_val, max_val = float('inf'), -float('inf')

    dfs(1, nums[0], plus, minus, multiple, divide)
    print(min_val, max_val)


if __name__ == "__main__":
    solution()
