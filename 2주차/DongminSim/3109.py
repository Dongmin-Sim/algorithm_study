'''
문제 : 빵집
출처 : https://www.acmicpc.net/problem/3109
카테고리 : #dfs, #brute-force 
'''

import sys


def dfs(x: int, y: int, d: list) -> bool:
    global r, c, maps

    maps[x][y] = 'x'

    if y == c-1:
        return True

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if maps[nx][ny] == 'x':
            continue
        # 다음 좌표에 대해 dfs 수행한 결과가 True라면 return True
        if dfs(nx, ny, d):
            return True
    return False


def solution():
    global r, c, maps
    input = sys.stdin.readline

    r, c = map(int, input().split())
    answer = 0
    maps = []

    for _ in range(r):
        maps.append(list(input().strip()))

    d = [(-1, 1), (0, 1), (1, 1)]

    for x in range(r):
        if dfs(x, 0, d):
            answer += 1

    print(answer)


if __name__ == "__main__":
    solution()
