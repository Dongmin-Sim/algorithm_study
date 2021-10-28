def dfs(depature, answer):
    global tickets_book
    answer.append(depature)

    # 해당 공항에서 출발하는 티켓이 없을 경우
    if depature not in tickets_book:
        return answer
    # 해당 공항에서 출발하는 티켓을 모두 사용한 경우
    if min(tickets_book[depature].values()) != 0:
        return answer

    # 해당 공항에서 출발하는 티켓(알파벳 순)에 방문처리 후 dfs
    for next_arrival in sorted(tickets_book[depature].keys()):
        if tickets_book[depature][next_arrival] == 0:
            tickets_book[depature][next_arrival] += 1
            answer = answer + dfs(next_arrival, [])
        else:
            continue

    return answer


def solution(tickets):
    global tickets_book

    tickets_book = {}

    for departure, arrival in tickets:
        temp = {arrival: 0}
        if departure not in tickets_book:
            tickets_book[departure] = temp
        else:
            d = tickets_book[departure]
            d[arrival] = 0

    answer = dfs('ICN', [])

    return answer
