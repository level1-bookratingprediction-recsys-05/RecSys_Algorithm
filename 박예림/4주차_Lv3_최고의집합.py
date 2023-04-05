# https://school.programmers.co.kr/learn/courses/30/lessons/12938
def solution(n, s):
    q, r = divmod(s, n) # s를 n으로 나눈 몫, 나머지
    
    if q == 0:
        return [-1]
    
    elif r == 0:
        return [q] * n
    
    else:
        return [q] * (n - r) + [q + 1] * r
