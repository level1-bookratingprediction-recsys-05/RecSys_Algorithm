from collections import deque

def solution(n, m, section):
    answer = 0
    section = deque(section)
    end = section[0] + m - 1
    t = 1
    while section:
        now = section.popleft()
        if now <= end: continue
        else: 
            t += 1
            end = now + m - 1 
        if end > n: break
    return t
