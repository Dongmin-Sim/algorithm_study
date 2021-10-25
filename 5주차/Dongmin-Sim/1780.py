'''
문제 : 종이의 개수
출처 : https://www.acmicpc.net/problem/1780
'''
import pprint


def same_paper(coordinates, Map):
    x1, y1, x2, y2 = coordinates
    first = Map[x1][y1]

    cur_x, cur_y = x1, x2
    cnt = 0
    while True:
        if first != Map[cur_x][cur_y]:
            return False, cnt, first

        cnt += 1

        if cur_x == x2 and cur_y == y2:
            break

        if cur_y < y2:
            cur_y += 1
            continue
        else:
            cur_x += 1
            cur_y = y1

    return True, cnt, first


def find_coordinate(n, coordinates) -> list:
    coordinate = []

    x1, y1, x2, y2 = coordinates

    # 마지막 쪼개는 경우

    # 한 변의 길이
    nn = n//3
    idx = 0
    cur_x, cur_y = x1, x2
    while True:
        coordinate.append((cur_x, cur_y, cur_x+nn-1, cur_y+nn-1))
        idx += 1

        if idx == 9:
            break

        if cur_y < y2:
            cur_y += nn
            continue
        else:
            cur_x += nn
            cur_y = y1

    return coordinate


def divde_conquer(n, coordinates, Map):
    a, b, c = 0, 0, 0
    # 모두 같은 종이로 되어 있는지 검사
    same_result = same_paper(coordinates, Map)

    # 만약 해당 종이가 모두 같다면
    if same_result[0]:
        cnt, paper_type = same_result[1], same_result[2]
        if paper_type == '-1':
            a += cnt
        elif paper_type == '0':
            b += cnt
        else:
            c += cnt

    # 만약 다르다면
    else:
        print("9등분")
        # 9개 좌표 구하기
        temp_list = find_coordinate(n, coordinates)

        # 9 등분한 결과를 다시 추가
        for coordinate in temp_list:
            temp_a, temp_b, temp_c = divde_conquer(n//3, coordinate, Map)
            a += temp_a
            b += temp_b
            c += temp_c

    return a, b, c


def solution():
    n = int(input())

    Map = []
    for i in range(n):
        Map.append(list(input().split()))

    a, b, c = divde_conquer(n, (0, 0, n-1, n-1), Map)
    print(a, b, c)


if __name__ == '__main__':
    solution()
