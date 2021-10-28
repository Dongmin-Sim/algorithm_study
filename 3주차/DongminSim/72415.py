'''
문제 : 카드 짝 맞추기
출처 : https://programmers.co.kr/learn/courses/30/lessons/72415
카테고리 : #bfs, #brute-force
'''
from collections import deque
from itertools import permutations
from copy import deepcopy

board = []


def ctrl_move(r, c, k, t):
    global board
    cur_r, cur_c = r, c
    while True:
        nr = cur_r + k
        nc = cur_c + t

        #  맵을 벗어나는 경우 리턴
        if not (0 <= nr < 4 and 0 <= nc < 4):
            return cur_r, cur_c

        # 다른 카드를 만났을 경우
        if board[nr][nc] != 0:
            return nr, nc

        cur_c = nr
        cur_c = nc


def bfs(start, end):
    r, c = start  # 출발 좌표
    find_r, find_c = end  # 목표 좌표

    queue = deque()
    queue.append((r, c, 0))  # x, y, 거리

    visited = [[0]*4 for _ in range(4)]

    move = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while queue:

        r, c, dist = queue.popleft()
        print(r, c)
        if visited[r][c]:
            continue
        visited[r][c] = 1

        # 현재 좌표가 목표좌표와 같다면 그냥 리턴
        if r == find_r and c == find_c:
            return dist

        for dr, dc in move:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                queue.append((nr, nc, dist+1))
            nr, nc = ctrl_move(r, c, dr, dc)
            queue.append((nr, nc, dist+1))
    return -1


def solution(input_board, sr, sc):
    global board

    board = input_board

    # 카드들의 좌표값 저장 ex [[], [(1, 2), (3, 4)], [], ...]
    location = [[] for _ in range(7)]
    # 카드들의 종류가 담긴 리스트 ex) [1, 3, 5]
    nums = []

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if board[i][j] not in nums:
                    nums.append(board[i][j])
                location[board[i][j]].append((i, j))

    # 카드들의 순열
    per = list(permutations(nums, len(nums)))

    answer = float('inf')

    for i in range(len(per)):
        board = deepcopy(input_board)  # 지웠던 곳 다시 채우기
        cnt = 0
        r, c = sr, sc
        for j in per[i]:
            cursor_p1 = bfs((r, c), location[j][0])  # cursor -> p1
            cursor_p2 = bfs((r, c), location[j][1])  # cursor -> p2

            if cursor_p1 < cursor_p2:
                cnt += cursor_p1
                cnt += bfs(location[j][0], location[j][1])  # p1 -> p2
                r, c = location[j][1]  # cursor 재설정
            else:
                cnt += cursor_p2
                cnt += bfs(location[j][1], location[j][0])  # p2 -> p1
                r, c = location[j][0]

            board[location[j][0][0]][location[j][0][1]] = 0  # 카드 지우기
            board[location[j][1][0]][location[j][1][1]] = 0  # 카드 지우기

            cnt += 2  # enter

        answer = min(answer, cnt)
    return answer


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
