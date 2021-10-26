import copy
INF = int(1e9)

# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]


def watch(y, x, direction, tmp):
    for d in direction:
        nx = x
        ny = y

        while True:
            nx += dx[d]
            ny += dy[d]
            # 맵을 벗어나지 않고 벽을 만나지 않으면
            if nx >= 0 and nx < m and ny >= 0 and ny < n and tmp[ny][nx] != 6:
                # 감시한 길은 #으로
                if tmp[ny][nx] == 0:
                    tmp[ny][nx] = '#'
            # 맵 밖을 나가거나, 벽을 만나면 종료
            else:
                break


def dfs(office, cnt):
    global ans

    tmp = copy.deepcopy(office)

    if cnt == cctv_cnt:
        c = 0
        # 사각지대 계산
        for i in tmp:
            c += i.count(0)
        ans = min(ans, c)
        return

    # cctv의 좌표, 종류
    y, x, cctv = q[cnt]

    for i in direction[cctv]:
        watch(y, x, i, tmp)
        dfs(tmp, cnt + 1)
        tmp = copy.deepcopy(office)


n, m = map(int, input().split())
office = []
cctv_cnt = 0
# cctv의 좌표와 종류
q = []
ans = INF

for i in range(n):
    input_data = list(map(int, input().split()))
    office.append(input_data)
    for j in range(len(input_data)):
        if input_data[j] != 0 and input_data[j] != 6:
            cctv_cnt += 1
            q.append([i, j, input_data[j]])

dfs(office, 0)
print(ans)
