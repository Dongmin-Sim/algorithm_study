import sys
input = sys.stdin.readline

n, k = map(int, input().split())

if k < 5:
    print(0)
    exit()

if k == 26:
    print(n)
    exit()

words = []
for _ in range(n):
    words.append(set(input().rstrip()))

check = [True] * 26
for w in ['a', 'c', 'i', 'n', 't']:
    check[ord(w) - ord('a')] = False

ans = 0


def dfs(idx, cnt):
    global ans

    if cnt == k - 5:
        subcnt = 0
        for word in words:
            for w in word:
                if check[ord(w) - ord('a')]:
                    break
            else:
                subcnt += 1
        ans = max(ans, subcnt)
        return

    for i in range(idx, 26):
        if check[i]:
            check[i] = False
            dfs(i, cnt + 1)
            check[i] = True


dfs(0, 0)
print(ans)
