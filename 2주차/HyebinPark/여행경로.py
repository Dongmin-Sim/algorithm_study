def solution(tickets):
    answer = []
    visited = ['ICN']
    tickets.sort(key = lambda x: x[1])
    dictickets = {}
    for fr, to in tickets:
        if fr not in dictickets:
            dictickets[fr] = [to]
        else:
            dictickets[fr].append(to)

    while visited:
        now = visited[-1]

        if now not in dictickets or dictickets[now] == []:
            answer.append(visited.pop())
        else:
            visited.append(dictickets[now].pop(0))
    return answer[::-1]

print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]))
