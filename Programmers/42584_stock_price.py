"""
https://programmers.co.kr/learn/courses/30/lessons/42584#

주식가격
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
"""
from collections import deque

def solution(prices):
    queue = deque()
    queue = deque(prices)
    [queue.append(i) for i in prices]

    answer = []

    while queue:
        curr_price = queue.popleft()
        
        res = 0
        for price in queue:
            if curr_price > price:
                res = 1
                break
            res += 1
            
        answer.append(res)
    return answer

print(solution([1,1, 1, 1,1]))