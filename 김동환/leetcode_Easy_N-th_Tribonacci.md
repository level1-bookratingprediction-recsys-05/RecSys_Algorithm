![image](https://user-images.githubusercontent.com/89527573/235091525-8243e887-8c9a-4b29-b3fe-e7d159b9a52d.png)

# Idea
----
1. 이 계산을 위해서는 3개의 수가 필요
2. 스택을 이용해서 마지막 수는 빼고 최근 수는 더하는 형식으로 하면 n, n+1, n+2를 계속 업데이트할 수 있다. 

# Solution
----
````
from collections import deque
class Solution:
    
    def tribonacci(self, n: int) -> int:
        q = deque([0,1,1])
        if n == 0: return 0
        elif (n == 1) or (n == 2): return 1
        curr = 2
        last_two = 2
        last = 2
        while curr < n:
            curr += 1
            new = q[0] + q[1] + q[2]
            q.popleft()
            q.append(new)
   
        return q[-1]
