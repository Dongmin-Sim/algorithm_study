'''
문제 : 괄호 추가하기
출처 : https://www.acmicpc.net/problem/16637
카테고리 : #Brute-force
'''


def dfs(op_cnt, sub_total):
    global answer, nums, op

    if op_cnt == len(op):
        answer = max(answer, int(sub_total))
        return

    first = str(eval(sub_total + op[op_cnt] + nums[op_cnt + 1]))
    dfs(op_cnt + 1, first)

    if op_cnt + 1 < len(op):
        second = str(
            eval(nums[op_cnt + 1] + op[op_cnt + 1] + nums[op_cnt + 2]))
        second = str(eval(sub_total + op[op_cnt] + second))

        dfs(op_cnt + 2, second)


def solution():
    global answer, nums, op
    n = int(input())
    exp = list(input())

    nums, op = [], []
    for e in exp:
        nums.append(e) if e.isdigit() else op.append(e)

    answer = -float('inf')
    dfs(0, nums[0])
    print(answer)


if __name__ == "__main__":
    solution()
