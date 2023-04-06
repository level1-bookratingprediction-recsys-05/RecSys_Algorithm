# idea
----
1. 두 카드 뭉치의 첫 카드를 보고 해당하는 것이 있으면 pop    
2. 둘 다 없음 stop   

# code
----
```
def solution(cards1, cards2, goal):
    answer = ''
    from collections import deque
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    
    for w in goal:
        if cards1:
            c1 = cards1[0]
            if c1 == w: 
                cards1.popleft()
                continue
        if cards2:
            c2 = cards2[0]
            if c2 == w:
                cards2.popleft()
                continue
        return 'No'
    
    return 'Yes'
  
