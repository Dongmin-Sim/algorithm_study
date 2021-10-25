import sys
input = sys.stdin.readline

def isSame(x, y, n):
    temp = graph[x][y]

    for i in range(n):
        for j in range(n):
            if graph[x+i][y+j] != temp:
                return False
    return True

def divide(x, y, n):
    if isSame(x, y, n):
        ans[graph[x][y] + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide(x + i * n//3, y + j * n//3, n//3)

num = int(input())
graph = []
ans = [0] * 3

for _ in range(num):
    graph.append(list(map(int, input().split())))

divide(0, 0, num)
print(*ans, sep = '\n')
