# Problem
-----
![image](https://user-images.githubusercontent.com/89527573/235088730-6d8a21a1-b6a1-43bc-9f38-feb1e75efcbb.png)

# Idea
----
1. 각 자리에 갈 수 있는 점프 범위가 있다.
2. 내가 이 자리에서 끝까지 도달할 수 있을 지는 앞에 블럭들에게 달려있다. 
3. 그럼 뒤에서 부터 체크를 하면 어떨까?
4. 그러면 앞에 있는 블록들의 정보를 이용해 지금 이 자리에서는 끝까지 갈 수 있을지 없을지 알 수 있다.
5. 처음은 뒤에서 부터 시작해 현재 점프 범위 >= 마지막 인덱스이면 이 블록으로 갈 수 있다면 끝까지 갈 수 있다는 뜻
6. 그러면 last를 이 블록에다 저장해놓고 다음 블록은 현재 점프 범위 >= last 가 되면 끝까지 갈 수 있다. 
7. 이러면 O(n)으로 풀 수가 있다. 

# Solution
----
```
class Solution:
        
    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        dp = [False] * len(nums)
        dp[-1] = True

        last_true = len(nums) - 1
        for curr_idx in range(len(nums)-2, -1, -1):
            if nums[curr_idx] == 0:
                dp[curr_idx] = False
            else:
                if curr_idx + nums[curr_idx] >= len(nums) -1: 
                    dp[curr_idx] = True
                    last_true = curr_idx
                else:
                    jump_range = nums[curr_idx]
                    dp[curr_idx] = False
                    if curr_idx + jump_range >= last_true:
                        dp[curr_idx] = True
                        last_true = curr_idx
        return dp[0]
