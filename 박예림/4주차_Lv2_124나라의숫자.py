# https://school.programmers.co.kr/learn/courses/30/lessons/12899#
def solution(n):
    answer = ''
    
    while True:
        Q = n // 3
        R = n % 3
        
        if R == 1:
            answer = '1' + answer
        elif R == 2:
            answer = '2' + answer
        elif R == 0:
            answer = '4' + answer
            n -= 1
            
        if Q == 0 or (Q == 1 and R == 0): break
        
        n = n // 3
        print(answer)

    return answer
