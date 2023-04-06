# idea
---- 
1. 합이 같으면서 최대의 곱 -> 숫자 간의 차이가 적은 것들   
2. 일단 다 똑같이 숫자 분배 후   
3. 나머지를 다  1 1 1 1 1 로 없어질 때까지 분배   
# code 
----
```
def solution(n, s):
    answer = []
    if s < n: return [-1]
    
    base_n = s // n
    leftover = s % n
    answer = [base_n] * n
    if leftover == 0: return answer
    else:
    
        i = 0
        while leftover > 0:
            answer[i] += 1
            leftover -= 1
            i += 1
    answer.sort()
    return answer
