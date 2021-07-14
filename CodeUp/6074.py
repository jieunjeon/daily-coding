"""
https://codeup.kr/problem.php?id=6074&rid=0
6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기


# Problem description

본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
------

영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

예시
c = ord(input())
t = ord('a')
while t<=c :
  print(chr(t), end=' ')
  t += 1

참고
알파벳 문자 a의 정수값은 ord('a')로 알아낼 수 있다.
chr(정수값)을 이용하면 유니코드 문자로 출력할 수 있다.
print(..., end=' ') 와 같이 작성하면 값 출력 후 공백문자 ' '를 출력한다. 즉, 마지막에 줄을 바꾸지 않고 빈칸만 띄운다.
(end='\n'로 작성하거나 생략하면, 값을 출력한 후 마지막(end)에 줄바꿈(newline)이 된다.)


# example
input
f
output
a b c d e f
"""

"""
Time Complexity: O(n)
"""
def sol1():
  a = ord(input()) 
  b = ord('a')
  while a >= b:
    print (chr(b))
    b+=1

def sol2():
  char = ord(str(input())) 
  start = ord('a')
  for i in range(char-start+1): 
    print(chr(start + i), end=' ')

def sol3():
  char = ord(str(input())) 
  start = ord('a')
  while (char - start + 1) :
     print(chr(start), end=' ') 
     start += 1

  