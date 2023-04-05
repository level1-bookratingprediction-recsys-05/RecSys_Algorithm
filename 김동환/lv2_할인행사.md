# idea
----
1. 10일 동안의 아이템 수량을 알아야함
2. 매번 10개 조사하면 시간 복잡도 크므로 슬라이딩 윈도우
3. 저장해놓은 데이터에 나가는 것과 들어오는 것만 갱신
4. 추가하고 뺄 때 -> 조건 충족 혹은 불충족하는지 검사

# code
-----
```
from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    left = 0
    right = 9
    done = set()
    std = defaultdict(int)
    dic = defaultdict(int)
    for item, num in zip(want, number): std[item] = num
    for item in want: dic[item] = 0
    for item in discount[left:right+1]: dic[item] += 1
    for item in std:
        if dic[item] >= std[item]: done.add(item)


    while right < len(discount):
        
        if len(done) == len(want): answer += 1
        
        pop_item = discount[left]
        dic[pop_item] -= 1
        if pop_item in std:
            if dic[pop_item] < std[pop_item]: done.discard(pop_item)
        left += 1
        
        right += 1
        if right < len(discount):
            add_item = discount[right]
            dic[add_item] += 1
            if add_item in std:
                if dic[add_item] >= std[add_item] : done.add(add_item)
        
    return answer


    
