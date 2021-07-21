"""
https://programmers.co.kr/learn/courses/30/lessons/64061
크레인 인형뽑기 게임

2019 카카오 겨울 인턴십 

"""
def solution(board, moves):
    """
    Time Complexity: O(n) where n is the number of the moves (we can ignore the grid since its always 5*5)
    """
    answer = 0
    bucket = []
    
    for move in moves:
        for r, c in enumerate(board):
            if c[move-1] > 0: # use move as an index
                bucket.append(c[move-1])
                board[r][move-1] = 0
                if  bucket[-1:] == bucket[-2:-1]: # after the move, check the bucket if the last one & second last one is the same
                    answer += 2
                    bucket = bucket[:-2]
                break # 1 turn over
    return answer