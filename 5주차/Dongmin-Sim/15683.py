'''
문제 : 감시
출처 : https://www.acmicpc.net/problem/15683
카테고리 : #구현
'''
from collections import defaultdict

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def min_blind_spot(n: int, m: int, Map: list, cctv: defaultdict):
    cctv_type = cctv.keys()

    return


def solution():
    n, m = map(int, input().split())
    Map = []

    cctv = defaultdict(list)

    for i in range(n):
        Map_temp, temp = [], list(map(int, input().split()))

        for j, elem in enumerate(temp):
            if elem != 0 and elem != 6:
                cctv[elem].append((i, j))

            Map_temp.append(elem)

        Map.append(Map_temp)

    print(min_blind_spot(n, m, Map, cctv))


if __name__ == '__main__':
    solution()
