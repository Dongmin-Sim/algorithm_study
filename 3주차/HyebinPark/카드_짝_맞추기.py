from collections import deque

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def move(b, x, y, dx, dy):
    nx = x + dx
    ny = y + dy

    if 0 <= nx < 4 and 0 <= ny < 4:
        if b[nx * 4 + ny] == '0':
            return move(b, nx, ny, dx, dy)
        else:
            return nx, ny
    else:
        return x, y


def solution(board, r, c):
    bstr = ''
    for i in range(4):
        for j in range(4):
            bstr += str(board[i][j])

    q = deque([])
    q.append((r, c, bstr, 0, -1))
    visited = set()

    while q:
        x, y, b, cnt, enter = q.popleft()
        idx = 4 * x + y

        if (x, y, b, enter) in visited:
            continue
        visited.add((x, y, b, enter))

        if b.count('0') == 16:
            return cnt

        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 4 and 0 <= ny < 4:
                q.append((nx, ny, b, cnt + 1, enter))

        for dx, dy in d:
            nx, ny = move(b, x, y, dx, dy)
            if nx == x and ny == y:
                continue
            q.append((nx, ny, b, cnt + 1, enter))

        if b[idx] != '0':
            if enter == -1:
                q.append((x, y, b, cnt + 1, idx))
            else:
                if enter != idx and b[enter] == b[idx]:
                    b = b.replace(b[enter], '0')
                    q.append((x, y, b, cnt + 1, -1))


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
