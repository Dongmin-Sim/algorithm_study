'''
문제 : 게임
출처 : https://www.acmicpc.net/problem/1072
'''


def solution(x, y):
    global ans
    initial_winrate = (y * 100) // x

    start, end = 1, x

    while start <= end:
        win = (start + end) // 2
        current_winrate = ((y + win) * 100) // (x + win)

        if current_winrate > initial_winrate:
            ans = min(ans, win)
            end = win - 1
        else:
            start = win + 1

        # print("current_winrate:", current_winrate, end=' ')
        # print("initial winrate:", initial_winrate, end=' ')
        # print('ans:', ans, 'win:', win)

    return ans


if __name__ == "__main__":
    x, y = map(int, input().split())
    ans = float('inf')

    solution(x, y)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

    '''
    실수 연산
    '''
    print(29/50)

    print(29/50*100)
