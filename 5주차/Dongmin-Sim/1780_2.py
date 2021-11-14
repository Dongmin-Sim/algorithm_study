def same_paper(x, y, n):
    global matrix

    paper_type = matrix[x][y]

    for i in range(n):
        for j in range(n):
            # 종이가 같지 않다.
            if paper_type != matrix[x+i][y+j]:
                return False, paper_type
    # 모두 같은 종류의 종이이다.
    return True, paper_type


def divide_conquer(x, y, n):
    global answer
    flag, paper_type = same_paper(x, y, n)
    if flag:
        # 종이가 모두 같다면 그냥 더해주면됨.
        answer[paper_type + 1] += 1
    else:
        for i in range(3):
            for j in range(3):
                divide_conquer(x+(i * n//3), y+(j * n//3), n//3)
    return


def solution():
    global matrix, answer

    n = int(input())
    matrix = []
    answer = [0] * 3  # [-1, 0, 1]

    for i in range(n):
        matrix.append(list(map(int, input().split())))

    divide_conquer(0, 0, n)
    print(*answer, sep='\n')


if __name__ == "__main__":
    solution()
