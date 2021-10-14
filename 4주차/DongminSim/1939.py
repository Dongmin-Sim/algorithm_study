'''
문제 : 중량제한
출처 : https://www.acmicpc.net/problem/1939
'''
from collections import deque


def bfs(n, m, graph, start, end):
    '''
    start -> end로 가는 모든 경로 중, (가장 낮은 중량제한 값을 기준) 가장 최댓값
    '''

    return


def solution():
    n, m = map(int, input().split())
    graph = [[] * n]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    start, end = map(int, input().split())

    print(bfs(n, m, graph, start, end))


if __name__ == '__main__ ':
    solution()
