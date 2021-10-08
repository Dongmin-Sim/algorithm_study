'''
문제 : 여행경로
출처 : https://programmers.co.kr/learn/courses/30/lessons/43164
카테고리 : #dfs
'''
from collections import defaultdict


def dfs(departure, answer, ticket_num):
    global tickets_book

    if len(answer) == ticket_num + 1:
        return answer

    for idx, arrival in enumerate(tickets_book[departure]):
        tickets_book[departure].pop(idx)

        # 해당 arrival 방문
        ans = answer[:]
        ans.append(arrival)

        temp = dfs(arrival, ans, ticket_num)

        if temp:
            return temp

        tickets_book[departure].insert(idx, arrival)


def solution(tickets):
    global tickets_book

    ticket_num = len(tickets)
    tickets_book = defaultdict(list)

    for departure, arrival in tickets:
        tickets_book[departure].append(arrival)

    for ticket in tickets_book:
        tickets_book[ticket].sort()

    answer = dfs("ICN", ["ICN"], ticket_num)

    return answer
