"""
https://programmers.co.kr/learn/courses/30/lessons/81301
숫자 문자열과 영단어

Problem Description:
네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.


입출력 예
s	result
"one4seveneight"	1478
"23four5six7"	234567
"2three45sixseven"	234567
"123"	123
"""

numbers = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def solution1(s):
    """
    Time Complexity: O(n) where n is the length of the string
    Space Complaxity: O(n) 
    """
    answer = ''
    tmp = ''
    
    for char in s:
        if char.isdigit():
            answer += char
        else:
            tmp += char
            if tmp in numbers:
                answer += numbers[tmp]
                tmp = ''
    return int(answer)


def solution2(s):
    answer = s
    for key, value in numbers.items():
        answer = answer.replace(key, value)
    return int(answer)