"""
https://programmers.co.kr/learn/courses/30/lessons/81302?language=python3
2021  카카오 채용연계형 인턴십

거리두기 확인하기

Problem description:
개발자를 희망하는 죠르디가 카카오에 면접을 보러 왔습니다.

코로나 바이러스 감염 예방을 위해 응시자들은 거리를 둬서 대기를 해야하는데 개발 직군 면접인 만큼
아래와 같은 규칙으로 대기실에 거리를 두고 앉도록 안내하고 있습니다.

대기실은 5개이며, 각 대기실은 5x5 크기입니다.
거리두기를 위하여 응시자들 끼리는 맨해튼 거리1가 2 이하로 앉지 말아 주세요.
단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.

제한사항
places의 행 길이(대기실 개수) = 5
places의 각 행은 하나의 대기실 구조를 나타냅니다.
places의 열 길이(대기실 세로 길이) = 5
places의 원소는 P,O,X로 이루어진 문자열입니다.
places 원소의 길이(대기실 가로 길이) = 5
P는 응시자가 앉아있는 자리를 의미합니다.
O는 빈 테이블을 의미합니다.
X는 파티션을 의미합니다.
입력으로 주어지는 5개 대기실의 크기는 모두 5x5 입니다.
return 값 형식
1차원 정수 배열에 5개의 원소를 담아서 return 합니다.
places에 담겨 있는 5개 대기실의 순서대로, 거리두기 준수 여부를 차례대로 배열에 담습니다.
각 대기실 별로 모든 응시자가 거리두기를 지키고 있으면 1을, 한 명이라도 지키지 않고 있으면 0을 담습니다.


입출력 예
places	result
[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	[1, 0, 1, 1, 1]
"""
from collections import deque

def bfs(row, col, place):
    
    dr = [0, 0, -1, 1] 
    dc = [-1, 1, 0, 0] 
    
    visited = [[0]*5 for _ in range(5)] # also use this to track the distance
    
    q = deque()   
    q.append((row, col))
    row_i, col_i = row, col
    
    while q:
        row, col = q.popleft()
        for i in range(4): # for every direction
            nr = row + dr[i]
            nc = col + dc[i]
            if row_i == nr and col_i == nc:
                continue
            if nr < 0 or nc < 0 or nr > 4 or nc > 4 or visited[nr][nc] != 0 or place[nr][nc] == 'X': # if coordinates are not valid or is a border (칸막이)
                continue
                
            if place[nr][nc] == 'O':
                q.append((nr, nc))
                visited[nr][nc] += visited[row][col] + 1 # should add up accumulated distance
            elif place[nr][nc] == 'P':
                visited[nr][nc] += visited[row][col] + 1
                if visited[nr][nc] <= 2:
                    return False # not social distanced
    return True # social distanced
            
      
def solution(places):
    answer = []
    #DFS
    
    #BFS
    for place in places:
        isSocialDistanced = 1
        for i, row in enumerate(place):
            for j, col in enumerate(row):
                if col == 'P' and not bfs(i, j, place):
                    isSocialDistanced = 0
                    break
            if not isSocialDistanced:
                break
        answer.append(isSocialDistanced)
                        
    return answer

  