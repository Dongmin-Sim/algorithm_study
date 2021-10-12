from collections import deque
import sys
input = sys.stdin.readline

s = int(input())
graph = dict()
q = deque()
q.append((1, 0))
graph[(1, 0)] = 0

while q:
    screen, clip = q.popleft()

    if screen < 0 or clip < 0:
        continue

    if screen == s:
        print(graph[(screen, clip)])
        break

    if (screen, screen) not in graph.keys():
        graph[(screen, screen)] = graph[(screen, clip)] + 1
        q.append((screen, screen))

    if (screen + clip, clip) not in graph.keys():
        graph[(screen + clip, clip)] = graph[(screen, clip)] + 1
        q.append((screen + clip, clip))

    if (screen - 1, clip) not in graph.keys() and screen > 0:
        graph[(screen - 1, clip)] = graph[(screen, clip)] + 1
        q.append((screen - 1, clip))