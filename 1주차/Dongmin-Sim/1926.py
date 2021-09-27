'''
문제 : 그림
https://www.acmicpc.net/problem/1926
'''
import sys


def bfs(x, y, n, m, Map, count, visited, d):

    visited[x][y] = count

    # 4방향 탐색
    for dx, dy in d:
        nx = dx + x
        ny = dy + y

        # 구역을 벗어나면 pass
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 이미 방문했으면 pass
        if visited[nx][ny] != False:
            continue
        if Map[nx][ny] == 0:
            continue

        bfs(nx, ny, n, m, Map, count+1, visited, d)


def solution(n: int, m: int, Map: list):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    d = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    region = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j] != False or Map[i][j] == 0:
                continue
            else:
                bfs(i, j, n, m, Map, 1, visited, d)
                region += 1

    return region, visited


def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(n)]

    region, visited = solution(n, m, Map)

    print(region)
    print(max(map(max, visited)))


if __name__ == '__main__':
    main()
